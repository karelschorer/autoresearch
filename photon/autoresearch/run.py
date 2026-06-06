#!/usr/bin/env python3
"""
autoresearch — the optimization loop around the Photon kernel.

This is the "auto" half of the project. It treats the eval harness
(bench/photon_eval.cpp) as a fixed, un-gameable fitness function and each
src/kernel_<variant>.cpp as a candidate hypothesis. The twist is that "how fast
is this kernel?" has no single answer — it depends on the *compiler regime* the
target is built under. So the loop sweeps a small matrix of (variant x regime):

  variants  baseline | branchless | avx2 | avx512   (the hypotheses)
  regimes   scalar   | release    | release512      (the build environments)

For every cell it:
  1. compiles the eval linked against that candidate under that regime,
  2. runs the correctness gate (the binary exits non-zero if its output
     diverges from the scalar baseline — math-changing cheats are rejected,
     not scored),
  3. records median throughput (Google Benchmark JSON), and
  4. prints a per-regime ranking + the speedup over that regime's baseline.

The whole point: the ranking is *not stable across regimes*, and that
instability is the research result (see RESEARCH.md).

Run from anywhere:  python3 photon/autoresearch/run.py
"""
import json
import math
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


def geomean(values):
    vals = [v for v in values if v > 0]
    if not vals:
        return 0.0
    return math.exp(sum(math.log(v) for v in vals) / len(vals))

ROOT = Path(__file__).resolve().parents[1]          # photon/
OUT = ROOT / "build" / "autoresearch"
INC = ROOT / "include"
EVAL = ROOT / "bench" / "photon_eval.cpp"

CXX = os.environ.get("CXX", "g++")
VARIANTS = ["baseline", "branchless", "avx2", "avx512"]
SIZES = [1024, 4096, 16384]

# Build regimes. Flag control is exact here (no CMake) because the regime *is*
# the independent variable of the experiment.
REGIMES = {
    # No auto-vectorization, no AVX: the "unoptimized scalar with branching"
    # world the eval's comments assume. Branch behavior is visible here.
    "scalar":     ["-O2", "-fno-tree-vectorize", "-mno-avx", "-mno-sse4.2"],
    # Realistic default deployment: compiler auto-vectorizes to 256-bit.
    "release":    ["-O3", "-march=native", "-funroll-loops"],
    # Same, but allow the compiler/intrinsics to use 512-bit vectors.
    "release512": ["-O3", "-march=native", "-funroll-loops",
                   "-mprefer-vector-width=512"],
}

# Variants that need real SIMD won't build/run under the scalar regime's
# -mno-avx; the loop simply records them as N/A there.
NEEDS_AVX = {"avx2", "avx512"}


def host_has_avx512() -> bool:
    try:
        info = Path("/proc/cpuinfo").read_text()
        return "avx512f" in info
    except OSError:
        return False


def compile_cell(variant, regime, flags):
    OUT.mkdir(parents=True, exist_ok=True)
    binary = OUT / f"eval_{regime}_{variant}"
    cmd = [CXX, *flags, f"-I{INC}",
           str(EVAL), str(ROOT / "src" / f"kernel_{variant}.cpp"),
           "-lbenchmark", "-lpthread", "-o", str(binary)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        return None, proc.stderr
    return binary, None


def run_cell(binary):
    """Returns (per_size_items_per_sec, name) or (None, reason)."""
    proc = subprocess.run(
        [str(binary), "--benchmark_format=json",
         "--benchmark_min_time=0.30s",
         "--benchmark_repetitions=5",
         "--benchmark_report_aggregates_only=true"],
        capture_output=True, text=True)
    if proc.returncode != 0:
        return None, "correctness gate failed"

    name = "?"
    m = re.search(r"\[VARIANT\] (.+)", proc.stdout)
    if m:
        name = m.group(1).strip()
    data = json.loads(proc.stdout[proc.stdout.find("{"):])
    per_size = {}
    for b in data["benchmarks"]:
        if b.get("aggregate_name") != "median":
            continue
        ms = re.search(r"/(\d+)", b["name"])
        if ms:
            per_size[int(ms.group(1))] = b.get("items_per_second", 0.0)
    return (per_size, name)


def main():
    print("=" * 74)
    print("autoresearch: sweeping PhotonVectorMultiplyFilter over variant x regime")
    print("=" * 74)
    if not host_has_avx512():
        print("note: host lacks AVX-512; avx512 variant will be skipped.")
    if shutil.which("taskset"):
        print("tip: for lower noise run under `taskset -c 0`.")

    results = {}  # results[regime][variant] = (per_size, name)
    for regime, flags in REGIMES.items():
        print(f"\n### regime '{regime}'  ({' '.join(flags)})")
        results[regime] = {}
        for variant in VARIANTS:
            if variant in NEEDS_AVX and "-mno-avx" in flags:
                print(f"  [N/A]    {variant}: needs AVX (disabled in this regime)")
                continue
            if variant == "avx512" and not host_has_avx512():
                print(f"  [N/A]    {variant}: host has no AVX-512")
                continue
            binary, err = compile_cell(variant, regime, flags)
            if binary is None:
                print(f"  [build]  {variant}: compile failed\n    {err.strip()[:200]}")
                continue
            per_size, name = run_cell(binary)
            if per_size is None:
                print(f"  [REJECT] {variant}: {name}")
                continue
            results[regime][variant] = (per_size, name)
            print(f"  [PASS]   {variant}: {name}")

    # ---- report -------------------------------------------------------
    # Rank by geometric mean across the three batch sizes (standard for a
    # benchmark suite). Single-size ranking is misleading: 16384 is L2-
    # bandwidth-bound and noisy, while 1024/4096 are compute-bound — geomean
    # keeps one noisy cell from deciding the winner.
    print("\n" + "=" * 74)
    print("RESULTS  (median items/sec per size; speedup = geomean vs. that")
    print("          regime's baseline geomean)")
    print("=" * 74)
    for regime in REGIMES:
        rows = results[regime]
        if not rows:
            continue
        base = rows.get("baseline", (None,))[0]
        ref = geomean([base.get(s, 0) for s in SIZES]) if base else None
        print(f"\n  regime '{regime}'")
        print(f"    {'variant':<11}" + "".join(f"{s:>13}" for s in SIZES)
              + f"{'geomean':>13}   spd")
        print("    " + "-" * 76)
        ranked = sorted(rows.items(),
                        key=lambda kv: geomean([kv[1][0].get(s, 0) for s in SIZES]),
                        reverse=True)
        for variant, (per_size, _name) in ranked:
            gm = geomean([per_size.get(s, 0) for s in SIZES])
            cells = "".join(f"{per_size.get(s,0)/1e9:>10.2f} G" for s in SIZES)
            spd = f"{gm/ref:>6.2f}x" if ref else "   ref"
            tag = "  <-- best" if variant == ranked[0][0] else ""
            print(f"    {variant:<11}{cells}{gm/1e9:>10.2f} G   {spd}{tag}")

    print("\nsee photon/RESEARCH.md for the interpretation of why the winner"
          "\nchanges between regimes.")


if __name__ == "__main__":
    main()
