---
title: "Achieving Single-Digit Microsecond Latency Inference for Capital Markets"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/achieving-single-digit-microsecond-latency-inference-for-capital-markets/"
published: "2026-04-02"
fetched: "2026-04-03T07:14:10.030475"
---

In algorithmic trading, reducing response times to market events is crucial. To keep pace with high-speed electronic markets, latency-sensitive firms often use specialized hardware like FPGAs and ASICs. Yet, as markets grow more efficient, traders increasingly depend on advanced models such as deep neural networks to enhance profitability. Because implementing these complex models on low-level hardware requires significant investment, general-purpose GPUs offer a practical, cost-effective alternative.
The NVIDIA GH200 Grace Hopper Superchip in the Supermicro ARS-111GL-NHR server has achieved single-digit microsecond latencies in the STAC-ML Markets (Inference) benchmark, Tacana suite (audited by STAC), providing performance comparable to or better than specialized hardware systems.
This post details these record-breaking results and provides a deep dive into the custom-tailored solutions required for low-latency GPU inference. It also walks you through an open source reference implementation and a tutorial for getting started.
STAC-ML benchmarking in financial services
Deep neural networks with long short-term memory (LSTM) are widely used for time series forecasting in capital markets. The STAC-ML (Markets) Inference benchmark measures LSTM model latency—the time between receiving new input and generating the output. It includes three models of increasing complexity (LSTM_A, LSTM_B, and LSTM_C), where LSTM_B is about six times greater than LSTM_A, and LSTM_C is roughly 200 times greater than LSTM_A. The benchmark features two suites: Tacana, which tests inference on a sliding window that updates each time step, and Sumaco, which tests inference on entirely new data for each operation.
The STAC-ML Markets (Inference) Tacana benchmark processes sliding window inputs, generating a single regression output, zt, at each iteration.
STAC-ML has emerged as a crucial benchmark for financial institutions leveraging machine learning (ML) in trading. It rigorously measures the speed and reliability of a technology stack when running models on live market data under realistic, production-like conditions. By standardizing key metrics—such as latency, throughput, and efficiency for LSTM and other time series models—STAC-ML enables banks, hedge funds, and market makers to conduct objective, apples-to-apples comparisons of competing hardware and software solutions prior to deployment.
For trading desks situated in co-located data centers, where winning or losing an order can be decided in microseconds, STAC-ML results are essential. They validate that a platform can meet strict latency budgets for demanding use cases like high-frequency market making, short-term price prediction, and automated hedging.
Furthermore, because the benchmark is designed and governed by practitioners from leading financial firms, its scores carry significant weight in the technology selection process, helping firms manage risk for the rollout of new ML-driven trading strategies and justify major investment decisions.
NVIDIA key STAC-ML results
NVIDIA demonstrated the following latencies (99th percentile) on a Supermicro ARS-111GL-NHR with a single NVIDIA GH200 Grace Hopper Superchip in FP16 precision for STAC-ML Tacana.
LSTM_A and p99 latency:
- 4.70 microseconds with one model instance
- 4.67 microseconds with two model instances
- 4.61 microseconds with four model instances
- 4.67 microseconds with eight model instances
LSTM_B and p99 latency:
- 7.10 microseconds with one model instance
- 6.88 microseconds with two model instances
- 7.10 microseconds with four model instances
LSTM_C and p99 latency:
- 15.80 microseconds with one model instance
Note that the observed latencies remain highly consistent when scaling from 1 to 4–8 number of model instances (NMIs) for both LSTM_A and LSTM_B. This stability highlights the importance of green contexts in maintaining predictable performance for latency-sensitive applications. For more details, see STAC-ML Markets (Inference) on a Supermicro ARS-111GL-NHR with NVIDIA GH200 Grace Hopper Superchip.
Seamless integration of NVIDIA GH200 Grace Hopper Superchip
The NVIDIA GH200 Grace Hopper Superchip expands the powerful 64-bit Arm processor ecosystem by supporting a diverse range of containers, application binaries, and operating systems—all running effortlessly on Grace Hopper with no modifications required. It seamlessly integrates with the full NVIDIA software stack, including NVIDIA HPC and AI platforms.
Comparison to previous submissions
NVIDIA previously submitted optimized results for both throughput and latency (Sumaco and Tacana benchmarks), as detailed in NVIDIA A100 Aces Throughput, Latency Results in Key Inference Benchmark for Financial Services Industry. In this earlier Tacana work, the sliding window approach enables more efficient handling of recurrency through precomputation. We refactored the problem to perform computations across all time steps using a fixed number of matrix-matrix multiplications (GEMMs) and an initial precomputation, enabling competitive performance.
Recent benchmark submissions on FPGA for Tacana have reported single-digit microsecond latencies for two LSTM sizes by focusing latency measurements on the final time step and leveraging precomputations outside critical sections.
Achieving such low latency on GPUs requires a custom-tailored solution, pushing the boundaries of GPU kernel launch latency.
The NVIDIA implementation consists of two sequential steps. The first step is precomputation, which generates required inputs for the final time step of the sliding window LSTM. For example, if there is the requirement to reset sliding window’s initial hidden/cell inputs to 0, that would be two GEMM operations per layer. This precomputation phase is excluded from timing measurements.
The second step is inference, where the last LSTM time step is computed after the sliding window shifts to the new input. After the inference, the relevant data for the next inference iteration is precomputed in the next preprocess stage.
Low-latency LSTM inference on GPUs
This section describes techniques for implementing low-latency inference of LSTM networks efficiently on NVIDIA hardware, including an open source reference implementation.
NVIDIA open source LSTM CUDA kernels
dl-lowlat-infer is an open source repository that provides examples of CUDA kernels for implementing low-latency time series inference. The techniques used in the kernels presented here were also applied in the STAC-ML benchmarks. While the open source repository includes minimal benchmarking capabilities to enable code execution, it is not intended to be a fully-fledged benchmarking suite like STAC-ML.
The dl-lowlat-infer repository showcases efficient techniques for running deep learning workloads on NVIDIA GPUs and is fully self-contained. It can generate model weights and inputs, randomly sample input data locations, and run inference for single or multiple model instances on the same GPU. Currently, it is restricted to sliding-window use cases for LSTMs.
This work focuses on three LSTM model sizes that are tuned specifically to fit and run efficiently on an NVIDIA RTX PRO 6000 Blackwell Server Edition GPU. The configurations include a small model that fits within the shared memory and registers of a single streaming multiprocessor (SM), a medium model that spans eight SMs within a thread block cluster (TBC), and a large model that utilizes nearly the entire device (184 out of 186 SMs).
| Layers | Time steps | Inputs | Units | Weights | |
| Small | 2 | 64 | 128 | 96 | 160K |
| Medium | 3 | 96 | 192 | 160 | 635K |
| Large | 4 | 128 | 512 | 736 | 16.7M |
While the record-breaking STAC-ML Tacana results were achieved on the NVIDIA GH200 Grace Hopper Superchip, the following tutorial uses the NVIDIA RTX PRO 6000 Blackwell Server Edition. This transition is motivated by the target deployment environment for many financial services firms. Low-latency trading desks often operate in power-constrained co-location environments where the thermal and power envelopes of traditional data center-class GPUs, such as the GH200, may not be a viable option.
The NVIDIA RTX PRO 6000 Blackwell Server Edition GPU provides a powerful and efficient alternative, suitable for deployment in these restricted environments. Crucially, the low-latency inference techniques and the open source code presented in the following tutorial are fully compatible with both architectures. This ensures that the same optimized kernels that deliver high performance on the RTX PRO 6000 Blackwell Server Edition GPU will also run efficiently on the GH200. This enables users to easily benchmark on data center platforms.
How to build and run the low-latency LSTM inference reference implementation
To build and run the benchmark, you need CUDA 13.0 or newer and a C++20-capable compiler. The following instructions are tailored to the latest NVIDIA Blackwell architecture, but you can also run the code on NVIDIA Hopper GPUs by compiling for SM90. Only the small network is supported on older GPU architectures; the two larger networks cannot run there due to technical limitations.
Building inside Docker
The benchmark is designed to run inside a Docker container. From within the top-level directory of the code, you can build the container and the benchmark, and prepare the models’ weights and inputs:
make -C docker CUDA_ARCHS=120-real LOCAL_USER=1 release_run
CUDA_ARCHS
sets the target GPU architecture in cmake. For example, 100
could be used for both NVIDIA Blackwell and NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs.
Running a model
After the image is built and the container is started, you can go to the app directory, /app/dl-lowlat-infer
, and run, for example, 10-second executions of a single instance of the small model using the persistent algorithm:
./nvLstmInf lstm_s data/lstm_s data/lstm_s.npy 10
Run four instances of the medium model using the persistent algorithm using six CPU threads (one thread per model instance plus main thread plus timing thread):
./nvLstmInf --cpuset=0,1,2,3,4,5 --num-instances=4 lstm_m data/lstm_m data/lstm_m.npy 10
For more details on running and developing inside the container, refer to the benchmark documentation.
Results
Table 2 shows the results produced from launching the code on a system with an AMD EPYC 9124 16-Core processor and an NVIDIA RTX PRO 6000 Blackwell Server Edition GPU.
| Ping Pong | Small | Medium | Large | |
| Average, µs | 2.4 | 3.5 | 4.7 | 13.2 |
| P99, µs | 2.5 | 4.3 | 5.4 | 14.2 |
The Ping Pong test measures the overhead of CPU-GPU synchronization and reading the input vector from host memory, which is the dominant contributor to latency for the small model. These measurements follow the similar approach as the MVAPICH latency microbenchmarks from Ohio State University. This overhead varies across systems and depends on multiple factors in the hardware and software stack. For larger models with more layers, additional latency arises from the use of cluster- and grid-level synchronization primitives.
Implementation details
Details about implementation are presented in this section.
Persistent kernels for inference
The inference stage with a batch size of one performs matrix vector multiplication, followed by the elementwise operation at each layer. After the final layer, the resulting hidden state is reduced into a single value, which is reported by the inference to the benchmarking process.
Inference was implemented using a persistent kernel approach, meaning the kernel remains active throughout the application’s lifetime. This persistence improves performance by loading weights into shared memory and registers only once during kernel initialization.
Depending on the problem size and to ensure weights fit within the available SMs, use a single CUDA block, a TBC, or allocate the entire device. As a result, three distinct kernels are implemented, all sharing the same memory layout for weights and all following similar structural and timing conventions.
The TBC can span up to eight SMs on RTX PRO 6000 Blackwell Server Edition GPUs, which is sufficient to accommodate weights for the medium model. The distributed shared memory API for TBCs allows more efficient data exchange and synchronization between SMs when gathering pieces of computed hidden state from the other CUDA blocks.
Timing
Timing is managed by a CPU thread, requiring implementing the signaling between host and device using CPU and GPU atomic synchronization primitives.
- The host signals the device when new input arrives in host memory and simultaneously starts the timer.
- The kernel polls for this signal, then reads the input and initiates computation.
- The computed floating-point output also acts as the host’s signal to stop the timer.
There is additional signaling to abort the kernel execution or reset the double buffer ID. Those buffers contain the data coming from the precomputation.
Serving multiple model instances
It is not energy- or cost-efficient to run, for example, a single CUDA block inference on an RTX PRO 6000 Blackwell Server Edition GPU. Use the CUDA green context (GC) feature to serve multiple inference instances on the same GPU. Note that there are alternative ways to serve multiple instances independently. For example, use NVIDIA Multi-Instance GPU (MIG) feature or add another layer of complexity of signalling to the persistent CUDA kernel itself.
The GC feature enables partitioning the GPU into GCs inside of the application without complicating the kernel. Each GC binds to a specific number of SMs. Any CUDA work submitted to a CUDA stream created in such a context will be executed on the corresponding set of SMs.
GCs are more lightweight and transparent to the programmer than traditional ones. The GPU is split into partitions of equal size to serve multiple persistent kernels. The remaining SMs are used for the precomputation phase. Since the precomputation is not latency critical, precomputations from different model instances are submitted to the same partition with remaining SMs but in different CUDA streams.
Coordinating with a persistent kernel instance from the host involves multiple spin loops. Thus, serving multiple model instances requires spawning one additional CPU thread per GC.
The minimal GC size is two SMs. So, small and medium models allocate two and eight SMs per GC, respectively. The large model needs almost the whole device to hold the weights in shared memory and registers, and it’s not possible to serve more than one model at once on a single RTX PRO 6000 Blackwell Server Edition GPU.
GDRCopy
Polling a device on a flag located in a pinned host buffer can be quite expensive. GDRCopy provides a low-latency alternative by creating a CPU mapping of GPU memory using GPUDirect RDMA. This allows CPU-driven memory copies with minimal overhead — particularly beneficial in low-latency scenarios where small data transfers are small and frequent. In our experiments, using GDRCopy has yielded speedups of up to 0.5 µs on PCIe-based systems.
Ping Pong benchmark
To obtain a Ping Pong model, start from the smallest model implementation and remove all LSTM-related computations. This setup measures only the overhead from CPU signaling and input reading of a single time step. Because it involves no weights, implement it using a single CUDA block, just like in the smallest model. This enables estimating the minimal latency achievable on a given system with our implementation.
Get started with low-latency inference
Building on the previous work reported in Benchmarking Deep Neural Networks for Low-Latency Trading and Rapid Backtesting on NVIDIA GPUs, we have now integrated custom CUDA kernels specifically optimized for latency‑critical paths. These enhancements achieved record‑breaking latency across two LSTM model sizes while preserving a flexible developer experience. The NVIDIA platform continues to provide a consistent, productivity‑oriented environment for research, optimization, and deployment.
These capabilities are accessible through an open source time series modeling pipeline that showcases how to use NVIDIA technology efficiently for low‑latency inference and backtesting. You can also view the GTC 2026 session Build High-Performance Financial AI: Achieve Microsecond Latency and Scalable LLM Inference on demand.
STAC and all STAC names are trademarks or registered trademarks of the Strategic Technology Analysis Center, LLC.
