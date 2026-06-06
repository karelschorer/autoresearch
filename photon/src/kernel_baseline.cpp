// Variant: baseline
// -----------------
// The unoptimized starting point. Scalar loop with a data-dependent branch
// on every element. On the eval's filter patterns (i%2, i%3) the branch is
// highly unpredictable, so the CPU eats branch-misprediction stalls. This is
// the implementation the autoresearch loop is trying to beat.
#include "photon/kernel.h"

extern "C" void PhotonVectorMultiplyFilter(const float* __restrict__ src,
                                           float* __restrict__ dest,
                                           const uint8_t* __restrict__ filter,
                                           float factor,
                                           size_t size) {
    for (size_t i = 0; i < size; ++i) {
        if (filter[i] == 1) {
            dest[i] = src[i] * factor;
        } else {
            dest[i] = 0.0f;
        }
    }
}

extern "C" const char* PhotonVariantName(void) { return "baseline (scalar+branch)"; }
