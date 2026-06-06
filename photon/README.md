# Photon kernel + autoresearch loop

A small, self-contained study: a **Photon-style** (Databricks) columnar
primitive, plus an **autoresearch** loop that optimizes it against a fixed,
un-gameable benchmark.

The kernel is the "multiply a float column by a scalar under a selection
bitmask" primitive — exactly the shape of operation Photon's vectorized engine
compiles for a *project-under-selection* node:

```cpp
dest[i] = (filter[i] == 1) ? src[i] * factor : 0.0f;
```

## Layout

```
photon/
  include/photon/kernel.h      the one function the loop may rewrite (C linkage)
  bench/photon_eval.cpp        FIXED eval: correctness gate + Google Benchmark
  src/kernel_baseline.cpp      scalar + branch (starting point)
  src/kernel_branchless.cpp    branch -> mask-multiply (auto-vectorizable)
  src/kernel_avx2.cpp          explicit 8-lane masked select (inf/NaN-safe)
  src/kernel_avx512.cpp        explicit 16-lane masked-multiply
  autoresearch/run.py          the loop: build x gate x benchmark x rank
  CMakeLists.txt               builds one eval binary per variant
  RESEARCH.md                  findings + interpretation
```

## How the loop works

`bench/photon_eval.cpp` is the **fitness function and never changes.** Each
`src/kernel_*.cpp` is a candidate hypothesis providing one definition of
`PhotonVectorMultiplyFilter`. For every candidate the loop:

1. **builds** the eval linked against that candidate,
2. **gates on correctness** — the binary's `main()` runs `VerifyCorrectness`
   and exits non-zero if the output diverges from the scalar baseline, so a
   candidate that "optimizes" by changing the math is *rejected, not scored*,
3. **benchmarks** median throughput over 1024/4096/16384-element batches, and
4. **ranks** survivors by geometric-mean throughput vs. the baseline.

The loop sweeps three compiler **regimes** (`scalar`, `release`,
`release512`) because the winner is not stable across them — and that
instability is the actual result.

## Run it

```bash
# dependency: Google Benchmark  (Ubuntu: apt-get install -y libbenchmark-dev)

# the full autoresearch sweep (recommended: pin a core for low noise)
taskset -c 0 python3 photon/autoresearch/run.py

# or build/run a single variant by hand via CMake
cmake -S photon -B photon/build -DCMAKE_BUILD_TYPE=Release
cmake --build photon/build -j
./photon/build/photon_eval_avx512
```

## TL;DR of the findings (full writeup in [RESEARCH.md](RESEARCH.md))

The eval invites three "obvious" optimizations. The loop tested them:

- **Branch elimination** — *red herring.* The filter patterns (`i%2`, `i%3`)
  are predictable, so there are no mispredictions to remove; the branchless
  rewrite is slower everywhere.
- **Hand-written SIMD** — *net negative* at `-O3`. The compiler already
  auto-vectorizes the branch; the intrinsics merely reproduce it, worse.
- **Vector width** — *the only real win,* and a single flag
  (`-mprefer-vector-width=512`) captures it for free, making the
  auto-vectorized baseline beat the hand-written AVX-512.

Recommended optimization, by payoff-per-risk: `-O3 -march=native`
(~5.9× over scalar) → `-mprefer-vector-width=512` (~8% more) → *stop*; the
intrinsics aren't worth their maintenance cost on this kernel. The kept
intrinsic variants are still useful as inf/NaN-safe reference selects and as a
marker of the bandwidth ceiling the kernel hits at 16384 elements.
