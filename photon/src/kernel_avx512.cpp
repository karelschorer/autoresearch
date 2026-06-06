// Variant: avx512
// ---------------
// Autoresearch iteration #3.
//
// AVX-512 has first-class mask registers (k0-k7), so the whole kernel becomes
// one masked-multiply: build a 16-bit lane mask from the filter bytes, then
// `maskz_mul` multiplies where the mask is set and writes a hard 0.0f
// elsewhere — fusing the select and the arithmetic into a single uop stream
// over 16 lanes. Like the AVX2 variant it is a true select (inf/NaN-safe),
// but at double the width and without a separate AND.
#include "photon/kernel.h"
#include <immintrin.h>

extern "C" void PhotonVectorMultiplyFilter(const float* __restrict__ src,
                                           float* __restrict__ dest,
                                           const uint8_t* __restrict__ filter,
                                           float factor,
                                           size_t size) {
    const __m512 vfactor = _mm512_set1_ps(factor);
    const __m512i one = _mm512_set1_epi32(1);

    size_t i = 0;
    for (; i + 16 <= size; i += 16) {
        __m512  s    = _mm512_loadu_ps(src + i);
        __m128i bytes = _mm_loadu_si128(reinterpret_cast<const __m128i*>(filter + i));
        __m512i wide = _mm512_cvtepu8_epi32(bytes);          // 16 bytes -> 16x int32
        __mmask16 m  = _mm512_cmpeq_epi32_mask(wide, one);   // lane selected?
        // maskz: lane = m ? s*factor : 0.0f
        _mm512_storeu_ps(dest + i, _mm512_maskz_mul_ps(m, s, vfactor));
    }
    // scalar tail
    for (; i < size; ++i) {
        dest[i] = (filter[i] == 1) ? src[i] * factor : 0.0f;
    }
}

extern "C" const char* PhotonVariantName(void) { return "avx512 (masked-multiply, 16 lanes)"; }
