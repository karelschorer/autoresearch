#pragma once
#include <cstddef>
#include <cstdint>

// =====================================================================
// Photon-style columnar primitive: "multiply-by-factor under a selection
// bitmask". This is the single function the autoresearch loop is allowed
// to rewrite. Every candidate variant in src/ provides a definition of it
// with C linkage so the (fixed) eval harness can link against exactly one
// implementation at a time.
//
//   dest[i] = (filter[i] == 1) ? src[i] * factor : 0.0f
//
// Contract the eval enforces (see bench/photon_eval.cpp):
//   * Bit-identical output to the scalar baseline on the test vector.
//   * No mutation of src / filter.
// =====================================================================
extern "C" void PhotonVectorMultiplyFilter(const float* __restrict__ src,
                                           float* __restrict__ dest,
                                           const uint8_t* __restrict__ filter,
                                           float factor,
                                           size_t size);

// Human-readable name of the linked variant, for the autoresearch report.
extern "C" const char* PhotonVariantName(void);
