cmake_minimum_required(VERSION 3.16)
project(photon_autoresearch CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

find_package(benchmark REQUIRED)

# Optimization flags shared by every variant. -march=native lets even the
# scalar/branchless variants use whatever SIMD the host advertises, so the
# explicit-intrinsics variants have to earn their keep against an
# auto-vectorizing compiler rather than against -O0.
set(PHOTON_OPT_FLAGS -O3 -march=native -funroll-loops)

# One eval binary per candidate kernel. The harness (bench/photon_eval.cpp) is
# identical across all of them; only the linked kernel changes.
set(PHOTON_VARIANTS baseline branchless avx2 avx512)

foreach(variant ${PHOTON_VARIANTS})
  add_executable(photon_eval_${variant}
    bench/photon_eval.cpp
    src/kernel_${variant}.cpp)
  target_include_directories(photon_eval_${variant} PRIVATE include)
  target_compile_options(photon_eval_${variant} PRIVATE ${PHOTON_OPT_FLAGS})
  target_link_libraries(photon_eval_${variant} PRIVATE benchmark::benchmark)
endforeach()
