# Autoresearch log — optimizing `PhotonVectorMultiplyFilter`

The target is a Photon-style columnar primitive: *multiply a float column by a
scalar under a selection bitmask*.

```cpp
dest[i] = (filter[i] == 1) ? src[i] * factor : 0.0f;
```

The eval (`bench/photon_eval.cpp`) is the fixed, un-gameable fitness function:
it gates on bit-identical output vs. the scalar baseline, then times the kernel
over 1024 / 4096 / 16384-element micro-batches with `DoNotOptimize` +
`ClobberMemory` so the loop can't be optimized away.

The eval's comments propose the "obvious" wins — *vectorize, kill branch
mispredictions, use intrinsics*. The autoresearch loop tested each hypothesis
instead of assuming it. The headline result: **most of those wins are either
already captured by the compiler or actively counterproductive on this eval.**

> Numbers below are medians of 5 reps, `g++ 13.3`, x86-64 with AVX-512, pinned
> with `taskset -c 0`. Absolute throughput is machine-specific; the *ratios*
> and the *direction* of each effect are the reproducible result. Re-run with
> `python3 photon/autoresearch/run.py`.

## The candidates (hypotheses)

| variant | idea |
|---|---|
| `baseline` | scalar loop with a per-element branch (the starting point) |
| `branchless` | replace the branch with `src*factor*filter[i]` (mask is 0/1) |
| `avx2` | explicit 8-lane masked **select** (inf/NaN-safe, not multiply-by-zero) |
| `avx512` | explicit 16-lane `maskz_mul` (select + multiply fused) |

## The regimes (the independent variable)

"How fast is this kernel?" has no single answer — it depends on how the target
is compiled. So the loop sweeps three build regimes:

| regime | flags | meaning |
|---|---|---|
| `scalar` | `-O2 -fno-tree-vectorize -mno-avx` | the literal "unoptimized scalar+branch" world the eval assumes |
| `release` | `-O3 -march=native -funroll-loops` | realistic default; compiler auto-vectorizes to **256-bit** |
| `release512` | `release` + `-mprefer-vector-width=512` | compiler allowed to auto-vectorize to **512-bit** |

## Results (median items/sec, geomean across the three batch sizes)

| regime | baseline | branchless | avx2 | avx512 | winner |
|---|---|---|---|---|---|
| `scalar`     | **2.32 G** | 1.97 G (0.85×) | — | — | baseline |
| `release`    | 13.66 G | 8.39 G (0.61×) | 10.02 G (0.73×) | **13.89 G (1.02×)** | avx512 (marginal) |
| `release512` | **14.75 G** | 10.42 G (0.71×) | 10.08 G (0.68×) | 13.84 G (0.94×) | baseline |

## Findings

### 1. Branch elimination is a red herring *on this eval*
The eval's filter patterns are `i%2` and `i%3` — periodic and **predictable**,
so the branch predictor nails them and there are almost no mispredictions to
remove. The `branchless` rewrite is *slower* in every regime (0.61×–0.91×)
because the int→float conversion of the mask byte sits on the critical path and
buys nothing back. The "eliminate branch mispredictions" advice only pays off
on *random* selectivity, which this eval never exercises.

### 2. The compiler already vectorizes the branch — to 256 bits
Inspecting the `release` assembly for `baseline` shows `ymm` registers, no
`zmm`: `g++ -O3 -march=native` auto-vectorizes the branched loop but defaults
to **256-bit** width (`-mprefer-vector-width=256`, chosen to avoid AVX-512
frequency throttling). So at `-O3` the hand-written `avx2` variant is just
*reproducing what the compiler already did* — and does it slightly worse
(0.73×), because the compiler schedules the surrounding code better.

### 3. The only real win is **vector width**, and a build flag captures it for free
The explicit `avx512` variant beats the `release` baseline (1.02× geomean,
~1.11× on the L1-resident 1024/4096 sizes) purely because it uses 512-bit
vectors. But add the single flag `-mprefer-vector-width=512` and the
*auto-vectorized baseline* jumps to **19.7 G/s @1024** and wins the
`release512` regime outright — now the hand-written intrinsics are *0.94×*,
i.e. slower than the compiler. **The entire payoff of the SIMD rewrite was a
vector-width flag**, with zero source change and zero correctness risk.

### 4. Big batches are bandwidth-bound — vector width stops mattering
At 16384 elements the working set (64 KB src + 64 KB dest) spills L1 into L2,
so the kernel becomes load/store-bandwidth-bound. Throughput collapses to
~8–9 G/s for *every* variant regardless of vector width — the per-size columns
show all four converging at 16384. Wider vectors only help while the data is
L1-resident.

## Conclusion (what autoresearch actually recommends)

For this kernel and eval, ranked by payoff-per-risk:

1. **Enable auto-vectorization** (`-O3 -march=native`): ~5.9× over scalar. Free.
2. **Allow 512-bit width** (`-mprefer-vector-width=512`): another ~8% on
   compute-bound batches. One flag, no code, no correctness risk.
3. **Hand-written intrinsics**: *net negative* once (1) and (2) are set, and
   they add maintenance + portability cost. Not recommended here.

The senior-engineer takeaway the loop surfaced: **profile and read the
generated assembly before rewriting.** Two of the three "obvious" optimizations
this eval invites (branch removal, hand SIMD) lose to a stock compiler, and the
one that wins is a build-configuration change, not an algorithm change. The
intrinsic variants are kept in-tree anyway because (a) they are inf/NaN-safe
*selects* rather than multiply-by-zero, which matters for real columnar data the
eval doesn't test, and (b) they document the ceiling the compiler is hitting.
