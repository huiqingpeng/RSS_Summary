---
title: "CUDA 13.2 Introduces Enhanced CUDA Tile Support and New Python Features"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/cuda-13-2-introduces-enhanced-cuda-tile-support-and-new-python-features/"
published: "2026-03-09"
fetched: "2026-03-10T11:21:33.802259"
---

CUDA 13.2 arrives with a major update: NVIDIA CUDA Tile is now supported on devices of compute capability 8.X architectures (NVIDIA Ampere and NVIDIA Ada), as well as 10.X and 12.X architectures (NVIDIA Blackwell). In an upcoming release of the CUDA Toolkit, all GPU architectures starting with Ampere will be fully supported. If you’re using Ampere, Ada, or Blackwell GPU architectures, check out the cuTile Python Quickstart guide to get started with CUDA Tile.
This post explores the CUDA 13.2 release, which boosts developer productivity with a variety of new Python additions, including profiling in CUDA Python and debugging Numba kernels. The math libraries provide expanded support for high-performance emulated libraries, and CUDA Core Compute Libraries (CCCL) continue to add both performance and feature improvements, providing C++ developers with a high-performance, modern interface to GPU programming.
cuTile Python
cuTile Python, the Python DSL expression of the CUDA Tile programming model, is releasing a number of feature enhancements. These include enhanced language support for the following:
- Recursive functions
- Closures with capture (nested functions, lambda functions)
- Custom reduction and scan functions
- Allowing assignments with type annotations
- Enhanced array support for
Array.slice
to create a view on a subarray
We’ve also provided an easy installation path. The following pip install command will install cuTile Python and pull in all the needed dependencies without requiring a separate system-wide installation of the CUDA Toolkit.
pip install cuda-tile[tileiras]
Core enhancements
Core enhancements in CUDA 13.2 are detailed in this section.
memcpy
with attributes
A previous release of CUDA (12.8) introduced batched memcpy
APIs. These allow you to specify batches of memcopies to be called with a single function call. You can also specify attributes to better control and optimize the memory transfers.
These APIs enable more control over your memory transfers. However, if you have only a single transfer and also want to use the attribute features, you need to call a batched API and then use batch size of 1. This is a bit cumbersome.
To simplify this use case, two new API functions have been added, cudaMemcpyWithAttributesAsync
and cudaMemcpy3DWithAttributesAsync
. These functions allow you to take advantage of using attributes in your memory calls, without requiring use of the more involved batched interface.
And to simplify your programming, if you already use cudaMemcpyAsync
for your transfer and you want to use attributes, you can continue using cudaMemcpyAsync
. It’s overloaded with the same argument list as cudaMemcpyWithAttributesAsync
.
Per-context local memory footprint reduction in Windows
Local memory (LMEM) on GPUs is allocated on a per thread basis and used for register spilling, stack variables, and the like. Starting with CUDA 13.2 and CUDA Driver R595, running on Windows in driver mode WDDM, LMEM usage has been significantly reduced. The effects of this change will be seen primarily in memory-constrained vGPU environments.
Query the properties of a memory pool
CUDA provides the ability to use memory pools for efficient memory management. CUDA 13.2 introduces an API to query the properties of a memory pool from the memory pool handle. These properties are obtained by calling cudaMemPoolGetAttribute
with the appropriate flags.
One use case for this new feature is creating a memory pool of the same type as a memory pool already created. For example, when using CUDA Graphs, the API cudaGraphAddMemAllocNode
accepts pool properties as a parameter. You can use the properties of a current memory pool to create a new pool with the same properties.
Windows compute drivers default to MCDM instead of TCC
On Microsoft Windows systems, starting with CUDA driver version R595, on compatible systems, GPUs that previously started by default in TCC will now start by default in MCDM. This change should address compatibility issues with some systems where users would have a yellow bang on their TCC GPUs at startup due to some incompatibility with OS/System features. For users with a dependency on TCC, it’s still available for now and can be enabled by using nvidia-smi -dm 1 -g <GPU ID>
.
Going forward we intend to progressively permanently transition to MCDM as it brings features that were previously reserved to GPUs in WDDM mode:
- WSL2: MCDM GPUs will show up in WSL2 and be able to run CUDA in WSL
- Containers: Native (and WSL) containers are supported
- Advanced memory management API:
cuMemCreate
,cudaMallocAsync
, and all their related APIs are now supported - RDMA through the same interface as WDDM RDMA that was released in CUDA Toolkit 13.1
- Memory oversubscription and trim notification.
Because of some extra overhead in MCDM we are aware that right now submission latency is slightly higher than on TCC and we are actively working on bringing it on par (both on WDDM and MCDM) with TCC and Linux native to ensure WDDM/MCDM would become a suitable and future proof driver model for all our GPUs on Windows.
CUDA_DISABLE_PERF_BOOST
CUDA Toolkit 13.2 and CUDA driver versions 580 and later added a new environment variable, CUDA_DISABLE_PERF_BOOST
. This allows for disabling the default behavior of boosting the GPU to a higher power state when running CUDA applications. Setting this environment variable to 1 will disable the boost. Disabling the performance boost may result in power savings when using features like NVENC/NVDEC.
CUDA Graphs polymorphic function to obtain graph node parameters
CUDA Graphs provide you the ability to create a workflow of GPU operations, like kernel launches and memory copies, as a single unit, rather than a series of individual commands. CUDA 13.2 adds a new polymorphic API function cudaGraphNodeGetParams
that allows you to obtain the parameters of the graph node. This is a companion function to existing polymorphic functions like cudaGraphNodeSetParams
, cudaGraphAddNode
, and cudaGraphExecNodeSetParams
.
Compilers
CUDA 13.2 brings new compiler updates, including support for new host compilers such as Visual Studio 2026, ARM C Language Extension support for gcc, and a single unified toolkit for Tegra and Desktop GPUs, which reduces overheads for containers and libraries.
Embedded devices
Previously, in CUDA 13.0 (and NVIDIA JetPack 7.0), the unified CUDA for Arm was introduced, streamlining development for Arm platforms by unifying the CUDA Toolkit across server-class and embedded devices such as NVIDIA Jetson Thor.
Starting from CUDA 13.2 (and in the upcoming JetPack 7.2—stay tuned), the same Arm SBSA CUDA Toolkit can be used across all Arm targets. This release also supports NVIDIA Jetson Orin devices on the same CUDA SBSA toolkit. For developers, this means reduced duplication in CI pipelines, simplified container management, and elimination of subtle bugs and inconsistencies that previously came from juggling different SDKs.
CUDA 13.2 and JetPack 7.2 introduce NVIDIA Multi-Instance GPU (MIG) support, allowing the GPU integrated with Jetson Thor to be partitioned into two fully isolated instances, each with dedicated memory, cache, and compute resources. This capability is particularly valuable for mixed-criticality applications, such as humanoid robotics. In these cases, developers can isolate safety-critical workloads (motor control and safety systems, for example) from noncritical processing tasks.
Without MIG, safety‑critical and noncritical workloads running on the same GPU, such as a low‑latency motor control alongside heavier perception or language models, compete for shared resources. A bursty task with high memory bandwidth demand can steal capacity from safety‑critical kernels, causing jitter and missed latency deadlines for control and safety systems.
With MIG, critical and noncritical workloads run on separate GPU instances, each with dedicated compute, memory, and bandwidth. This isolation delivers predictable latency and quality of service for control and critical tasks, while keeping the GPU highly utilized by concurrently running heavier perception or language workloads on the other instance.
Math libraries
CUDA 13.2 introduces improvements for math libraries including NVIDIA cuBLAS and NVIDIA cuSOLVER.
NVIDIA cuBLAS
A new experimental API with Grouped GEMM now supports MXFP8 for NVIDIA Blackwell GPUs. Prior support (in CUDA 13.1) included FP8 and BF16/FP16 Blackwell GPU support. Grouped GEMMs for the noted datatypes with CUDA Graphs support provides a host-synchronization-free implementation with device-side shapes for speedups of up to 4x over a multistream GEMM implementation in the mixture of experts (MoE) use case.
NVIDIA cuSOLVER
cuSOLVERD APIs for FP64‑emulated calculations have been introduced. This enables platforms with a high ratio of INT8‑to‑FP64 throughput to achieve significant performance gains, particularly for compute‑intensive workloads. The benefits of emulation are most apparent in key APIs for QR, LU, and Cholesky factorizations. To more about the latest advances in emulation techniques from NVIDIA, see Unlocking Tensor Core Performance with Floating Point Emulation in cuBLAS.
Figure 1 shows the results of FP64‑emulated GDEQRF, DGETRF, and DPOTRF on NVIDIA B200 systems. The performance benefits increase with matrix size and can reach up to 2x for QR, the most compute‑intensive of the three operations, when matrix sizes approach 80K.
Developer tools
Developer tools new to this release are detailed in this section.
NVIDIA Nsight Python
NVIDIA Nsight Python is a new kernel profiling interface that brings the power of NVIDIA profiling tools directly to Python developers. With this release, you can seamlessly profile CUDA kernels launched through Python frameworks across multiple configurations directly from Python.
Using just a few decorators, users can automatically configure, profile, and plot kernel performance comparisons. Nsight Python also provides access to the performance data in common Python data structures for advanced analysis. Download Nsight Python from PyPI. You can also contribute to the NVIDIA/nsight-python GitHub repo and visit the NVIDIA Developer Forum with any questions or issues.
@nsight.analyze.plot("02_paramater_sweep.png")
@nsight.analyze.kernel(configs=sizes, runs=10)
def benchmark_matmul_sizes(n: int) -> None:
"""
Benchmark matrix multiplication across different sizes.
The 'n' parameter comes from the configs list.
"""
a = torch.randn(n, n, device="cuda")
b = torch.randn(n, n, device="cuda")
with nsight.annotate("matmul"):
_ = a @ b
Numba-CUDA debugging
For the first time, debugging Numba-CUDA kernels running on a GPU is now possible with CUDA-GDB command-line debugging and NVIDIA Nsight Visual Studio Code Edition. Users can set breakpoints, step through statements, and inspect program state, as with host and native CUDA debuggers. This initial support has a limited feature set and the team is actively looking for feedback to improve it. To learn more, check out the Numba-CUDA debugging documentation and reach out for help or feedback on the Developer Forum.
NVIDIA Nsight Tools updates
NVIDIA Nsight Compute 2026.1 includes a new report clustering and merging tool accessible from the File > Merge Reports menu. This helps users understand data from repeated experiments, separate profiling sessions, or multiprocess applications generating multiple reports.
A new Register Dependency correlation window on the Source page helps users identify source line dependencies to quickly locate bottlenecks. The CUDA Graphs viewer tool window has been significantly improved to show graphs as they are built and profiled in the interactive profiling mode and visually correlates collected results to graph nodes. Nsight Compute is included in the CUDA Toolkit and is available as a standalone download.
NVIDIA Nsight Cloud includes updates to the Nsight Operator for Kubernetes along with Nsight Streamer Kubernetes and Docker containers for accessing and viewing Nsight tool reports from within a Cluster.
NVIDIA Nsight Copilot is a free AI-powered CUDA coding assistant that is now available to everyone with an NVIDIA Developer account.
NVIDIA Nsight Systems 2026.1 includes:
- PyTorch profiling improvements to display shape and training parameters for forward and backward extension modules
- Support for Python 3.14 in the Python sampling feature
- A new option to capture metrics of GPUDirect Storage DMA operations
CCCL
CUDA 13.2 ships with the 3.2 version of CCCL. Highlights include new modern CUDA C++ runtime APIs and new optimized algorithms, including Top-K.
Modern CUDA C++ runtime
CCCL 3.2 broadly introduces new idiomatic C++ interfaces for core CUDA runtime and driver functionality.
If you’ve written CUDA C++ you’ve likely built (or adopted) some form of convenience wrappers around today’s C-like APIs such as cudaMalloc
or cudaStreamCreate
.
The new APIs added in CCCL 3.2 are meant to provide the productivity and safety benefits of C++ for core CUDA constructs so you can spend less time reinventing wrappers and more time writing kernels and algorithms.
Highlights include:
- New convenient vocabulary types for core CUDA concepts (
cuda::stream
,cuda::event
,cuda::arch_traits
) - Easier memory management with Memory Resources and
cuda::buffer
- More powerful and convenient kernel launch with
cuda::launch
Example (vector add, revisited):
cuda::device_ref device = cuda::devices[0];
cuda::stream stream{device};
auto pool = cuda::device_default_memory_pool(device);
int num_elements = 1000;
auto A = cuda::make_buffer<float>(stream, pool, num_elements, 1.0);
auto B = cuda::make_buffer<float>(stream, pool, num_elements, 2.0);
auto C = cuda::make_buffer<float>(stream, pool, num_elements, cuda::no_init);
constexpr int threads_per_block = 256;
auto config = cuda::distribute<threads_per_block>(num_elements);
auto kernel = [] __device__ (auto config, cuda::std::span<const float> A,
cuda::std::span<const float> B,
cuda::std::span<float> C){
auto tid = cuda::gpu_thread.rank(cuda::grid, config);
if (tid < A.size())
C[tid] = A[tid] + B[tid];
};
cuda::launch(stream, config, kernel, config, A, B, C);
Try this example live on Compiler Explorer.
Stay tuned for a deeper dive into the design goals and intended usage patterns, and how these new APIs fit alongside existing CUDA APIs.
New algorithms
Algorithms new to CUDA 13.2 are detailed in this section.
Top-K selection
CCCL 3.2 introduces cub::DeviceTopK
(for example, cub::DeviceTopK::MaxKeys
) to select the K largest (or smallest) elements without sorting the entire input. For workloads where K is small, this can deliver up to 5x speedups over a full radix sort, and can reduce memory consumption when you don’t need sorted results.
Top‑K is an active area of ongoing work for CCCL. The roadmap includes planned segmented Top‑K as well as block‑scope and warp‑scope Top‑K variants. To learn more about what’s planned and share your most important Top‑K use cases, see NVIDIA/cccl GitHub Issue #5673.
Fixed-size segmented reduction
CCCL 3.2 now provides a new cub::DeviceSegmentedReduce
variant that accepts a uniform segment_size
, eliminating offset iterator overhead in the common case when segments are fixed-size. This enables optimizations for both small segment sizes (up to 66x) and large segment sizes (up to 14x).
// New API accepts fixed segment_size instead of per-segment begin/end offsets
cub::DeviceSegmentedReduce::Sum(d_temp, temp_bytes, input, output,
num_segments, segment_size);
In Figure 4, the new fixed-size variant shows significant speed-up for both small and large segments compared to the existing implementation that specifies begin and end offsets for each segment.
More new algorithms in CCCL 3.2
Segmented Scan: cub::DeviceSegmentedScan
provides a segmented version of a parallel scan that efficiently computes a scan operation over multiple independent segments.
Binary Search: cub::DeviceFind::[Upper/LowerBound]
performs a parallel search for multiple values in an ordered sequence.
Search: cub::DeviceFind::FindIf
searches the unordered input for the first element that satisfies a given condition. Thanks to its early-exit logic, it can be up to 7x faster than searching the entire sequence.
CUDA Python
CuPy now supports CUDA 13.0 and 13.1, and wheels are available in PyPI for CUDA 12 and CUDA 13. This means it’s easier than ever to install CuPy without a system-wide CUDA Toolkit.
pip install cupy-cuda12x
pip install cupy-cuda13x
CuPy now implements the CUDA Stream Protocol, enabling direct stream sharing with PyTorch, JAX, and other frameworks that support the protocol. This means zero-copy interoperability without manual pointer management.
# Share a CuPy stream with PyTorch
pytorch_stream = torch.cuda.ExternalStream(cupy_stream)
# Or import an external stream into CuPy
cupy_stream = cupy.cuda.Stream.from_external(pytorch_stream)
Support has been added to ml_dtypes.bfloat16
, which brings native reduced-precision computation to CuPy, a type commonly used in AI training and inference. Performance has improved in some core operations through fast-path optimizations for generalized ufuncs, array operators, and scalar handling. Support for multithreaded applications has improved. CuPy arrays can now be viewed as cuda::std::mdspan
objects through ndarray.mdspan
with control over 32-bit and 64-bit indexing. This provides users with more control over arithmetic operations and performance.
cuda.core 0.6 introduces NVML bindings (cuda.bindings.nvml
) for GPU monitoring and management, and new nvFatbin bindings (cuda.bindings.nvfatbin
) for fat binary manipulation. The new cuda.core.system
module provides Pythonic access to system information such as device thermal monitoring, and CPU/GPU affinity, built on top of NVML.
Support for building CUDA Graphs has graduated from the experimental namespace and it is available under the main cuda.core
namespace. This enables developers to capture sequences of operations and replay them with minimal overhead, and supports advanced patterns such as conditional execution (if_cond
and while_loop
), fork-join. The following code shows how the API works:
# Build a graph by capturing operations
gb = device.create_graph_builder()
gb.begin_building()
# Capture kernel launches in the graph (not executed)
launch(gb, LaunchConfig(grid=256, block=256), kernel_a, data_ptr)
launch(gb, LaunchConfig(grid=256, block=256), kernel_b, data_ptr)
launch(gb, LaunchConfig(grid=256, block=256), kernel_c, data_ptr)
# Finalize and instantiate the graph
graph = gb.end_building().complete()
# Launch the graph into an existing CUDA Stream
graph.launch(stream)
For more information, see the cuda.core.GraphBuilder
docs and examples.
Get started with CUDA 13.2
CUDA 13.2 simplifies high-performance development by continuing to elevate Python as a first-class citizen and introducing productivity-focused language features that bridge the gap between ease of use and peak GPU performance.
Download the CUDA 13.2 Toolkit to get started.
Acknowledgments
Thanks to the following NVIDIA contributors: Jake Hemstad, Becca Zandstein, Jackson Marusarz, Mridula Prakash, Rekha Mukund, Daniel Rodriquez, Bo Dong, Andy Terrel, Raphael Boissel, and Rob Armstrong.
