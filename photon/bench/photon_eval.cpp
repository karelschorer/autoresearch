#include <benchmark/benchmark.h>
#include <vector>
#include <numeric>
#include <iostream>
#include <cassert>
#include "photon/kernel.h"

// =====================================================================
// FIXED EVAL HARNESS — the un-gameable scoring gate.
//
// The target algorithm `PhotonVectorMultiplyFilter` is NOT defined here; it
// is linked in from one of the candidate variants under src/. The autoresearch
// loop rewrites/swaps that variant; this file never changes, so every
// candidate is judged against identical correctness and timing rules.
// =====================================================================

// =====================================================================
// STEP 1: CORRECTNESS & VERIFICATION GATING (Un-gameable)
// =====================================================================
bool VerifyCorrectness(size_t test_size) {
    std::vector<float> src(test_size, 42.0f);
    std::vector<float> dest_baseline(test_size, 0.0f);
    std::vector<float> dest_agent(test_size, 0.0f);
    std::vector<uint8_t> filter(test_size);

    // Generate an alternating bitmask filter pattern
    for (size_t i = 0; i < test_size; ++i) {
        filter[i] = (i % 2 == 0) ? 1 : 0;
    }

    // Run baseline
    for (size_t i = 0; i < test_size; ++i) {
        if (filter[i] == 1) dest_baseline[i] = src[i] * 2.5f;
    }

    // Run the agent's updated code
    PhotonVectorMultiplyFilter(src.data(), dest_agent.data(), filter.data(), 2.5f, test_size);

    // Assert that the agent didn't alter the math output
    for (size_t i = 0; i < test_size; ++i) {
        if (dest_baseline[i] != dest_agent[i]) {
            return false; // Fail immediately if results diverge
        }
    }
    return true;
}

// =====================================================================
// STEP 2: HIGH-RESOLUTION PERFORMANCE BENCHMARK
// =====================================================================
static void BM_PhotonVectorProcessing(benchmark::State& state) {
    const size_t size = state.range(0);

    std::vector<float> src(size, 1.5f);
    std::vector<float> dest(size, 0.0f);
    std::vector<uint8_t> filter(size);
    for (size_t i = 0; i < size; ++i) filter[i] = (i % 3 == 0) ? 1 : 0;

    // The core execution timing loop
    for (auto _ : state) {
        PhotonVectorMultiplyFilter(src.data(), dest.data(), filter.data(), 1.1f, size);

        // CRITICAL Anti-Cheating Guardian: Forces the compiler to materialize
        // the destination memory, preventing it from optimizing the whole loop away.
        benchmark::DoNotOptimize(dest.data());
        benchmark::ClobberMemory();
    }

    state.SetItemsProcessed(state.iterations() * size);
}

// Register the benchmark to run over typical database micro-batch sizes
BENCHMARK(BM_PhotonVectorProcessing)->Arg(1024)->Arg(4096)->Arg(16384);

// =====================================================================
// STEP 3: EXECUTION ORCHESTRATION PIPELINE
// =====================================================================
int main(int argc, char** argv) {
    std::cout << "[VARIANT] " << PhotonVariantName() << "\n";

    // 1. Guard against functional bugs
    if (!VerifyCorrectness(4096)) {
        std::cerr << "[CRITICAL ERROR] Code optimization broke correctness metrics!\n";
        return 1; // Exit with error so the git auto-commit hooks fail
    }
    std::cout << "[SUCCESS] Correctness check passed. Commencing performance tests...\n";

    // 2. Execute Google Benchmark framework to read processing latency
    ::benchmark::Initialize(&argc, argv);
    ::benchmark::RunSpecifiedBenchmarks();
    return 0;
}
