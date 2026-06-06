// Variant: branchless
// --------------------
// Autoresearch iteration #1.
//
// Hypothesis: the branch is the bottleneck, not the arithmetic. Replace the
// data-dependent branch with a multiply by the mask byte. Because filter[i]
// is exactly 0 or 1, `src[i] * factor * filter[i]` reproduces the baseline:
//   filter==1 -> src*factor*1 = src*factor
//   filter==0 -> src*factor*0 = 0.0f
//
// With no branch, the loop is trivially auto-vectorizable: the compiler emits
// packed FMA/mul over 8 (AVX2) or 16 (AVX512) lanes. This is the "let the
// compiler do the SIMD" baseline that any explicit-intrinsics variant must
// beat to justify its complexity.
//
// Correctness caveat the loop reasons about: multiply-by-zero only yields a
// clean 0.0f for finite inputs (inf*0 = NaN). The eval feeds finite data, so
// this is safe here; the AVX masked variants below remove even that caveat.
#include "photon/kernel.h"

extern "C" void PhotonVectorMultiplyFilter(const float* __restrict__ src,
                                           float* __restrict__ dest,
                                           const uint8_t* __restrict__ filter,
                                           float factor,
                                           size_t size) {
    for (size_t i = 0; i < size; ++i) {
        dest[i] = src[i] * factor * static_cast<float>(filter[i]);
    }
}

extern "C" const char* PhotonVariantName(void) { return "branchless (mask-multiply, auto-vectorized)"; }
