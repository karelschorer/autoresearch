// Variant: avx2
// -------------
// Autoresearch iteration #2.
//
// Explicit AVX2: process 8 floats per iteration. The mask bytes are widened
// 0/1 -> 32-bit, compared against 1 to form a lane mask, and the multiplied
// values are bitwise-AND'd with that mask. This is a *select*, not a
// multiply-by-zero, so it is correct even for inf/NaN source data — the
// robustness the branchless variant lacked — while still being branch-free.
//
// This mirrors how Databricks' Photon engine compiles a "project under
// selection vector" node: SIMD multiply + masked store over a column batch.
#include "photon/kernel.h"
#include <immintrin.h>

extern "C" void PhotonVectorMultiplyFilter(const float* __restrict__ src,
                                           float* __restrict__ dest,
                                           const uint8_t* __restrict__ filter,
                                           float factor,
                                           size_t size) {
    const __m256 vfactor = _mm256_set1_ps(factor);
    const __m256i one = _mm256_set1_epi32(1);

    size_t i = 0;
    for (; i + 8 <= size; i += 8) {
        // 8 source lanes * factor
        __m256 v = _mm256_mul_ps(_mm256_loadu_ps(src + i), vfactor);
        // widen 8 mask bytes (0/1) to 8x int32, build all-ones/all-zero lane mask
        __m128i bytes = _mm_loadl_epi64(reinterpret_cast<const __m128i*>(filter + i));
        __m256i wide = _mm256_cvtepu8_epi32(bytes);
        __m256  mask = _mm256_castsi256_ps(_mm256_cmpeq_epi32(wide, one));
        // bitwise select: keep v where mask set, else 0.0f
        _mm256_storeu_ps(dest + i, _mm256_and_ps(v, mask));
    }
    // scalar tail
    for (; i < size; ++i) {
        dest[i] = (filter[i] == 1) ? src[i] * factor : 0.0f;
    }
}

extern "C" const char* PhotonVariantName(void) { return "avx2 (masked select, 8 lanes)"; }
