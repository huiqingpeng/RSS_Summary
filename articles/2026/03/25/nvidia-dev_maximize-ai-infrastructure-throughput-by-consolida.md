---
title: "Maximize AI Infrastructure Throughput by Consolidating Underutilized GPU Workloads"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/maximize-ai-infrastructure-throughput-by-consolidating-underutilized-gpu-workloads/"
published: "2026-03-25"
fetched: "2026-03-26T07:03:52.543013"
---

In production Kubernetes environments, the difference between model requirements and GPU size creates inefficiencies. Lightweight automatic speech recognition (ASR) or text-to-speech (TTS) models may require only 10 GB of VRAM, yet occupy an entire GPU in standard Kubernetes deployments. Because the scheduler maps a model to one or more GPUs and can’t easily share across GPUs across models, expensive compute resources often remain underutilized.
Solving this isn’t just about cost reduction—it’s about optimizing cluster density to serve more concurrent users on the same world-class hardware. This guide details how to implement and benchmark GPU partitioning strategies, specifically NVIDIA Multi-Instance GPU (MIG) and time-slicing to fully use compute resources.
Using a production-grade voice AI pipeline as our testbed, we show how to combine models to maximize infrastructure ROI while maintaining >99% reliability and strict latency guarantees.
Addressing GPU resource fragmentation
By default, the NVIDIA Device Plugin for Kubernetes shows GPUs as integer resources. A pod requests nvidia.com/gpu: 1
, and the scheduler binds it to a physical device.
Large language models (LLMs) like NVIDIA Nemotron, Llama 3, or Qwen 7B/8B require dedicated compute to maintain low time to first token (TTFT) and high batch throughput. However, support models in a generative AI pipeline—embedding models, ASR, TTS, or guardrails—often use only a fraction of a card. Running these lightweight models on dedicated GPUs results in:
- Low utilization: GPU compute utilization often hovers near 0-10%.
- Cluster bloat: More nodes need provisioning to run the same number of pods.
- Scaling friction: Adding a new capability requires a new physical GPU.
To solve this, we must break the 1:1 relationship between pods and GPUs.
Architecture: Partitioning strategies
We evaluated two primary strategies for GPU partitioning supported by the NVIDIA GPU Operator.
Software-based partitioning: Time-slicing and MPS
Time-slicing enables multiple NVIDIA CUDA processes to share a GPU by interleaving execution. It functions similarly to a CPU scheduler: context A runs, pauses, and context B runs.
- Mechanism: Software-level scheduling through the CUDA driver.
- Pros: Maximizes utilization. Enables “bursting”—if Pod A is idle, Pod B can use 100% of the GPU’s compute cores.
- Cons: No hardware isolation. A memory overflow (OOM) in one pod may impact the shared execution context, and heavy compute in one pod can throttle neighbors (the “noisy neighbor” effect).
In addition to time-slicing, NVIDIA Multi-Process Service (MPS) offers an alternative software-based approach. MPS enables multiple processes to share GPU resources concurrently by using a server-client architecture. This provides more flexibility than MIG and is more resilient to certain issues like memory leaks compared to standard time-slicing.
However, in production, both methods share a single execution context, limiting isolation. While modern MPS provides isolated virtual address spaces, it lacks hardware-level fault isolation. This means a fatal execution error or illegal memory access in one process will propagate across the shared context, potentially leading to a GPU reset that affects other processes sharing the card.
MIG: The hardware approach to partitioning
MIG physically partitions the GPU into separate instances, each with its own dedicated memory, cache, and streaming multiprocessors (SMs). To the OS and Kubernetes, these look like separate PCI devices.
- Mechanism: Hardware-level isolation.
- Pros: Strict quality of service (QoS). One workload can’t impact the performance or memory stability of another.
- Cons: Rigid sizing. If a partition is idle, its compute resources can’t be “borrowed” by a neighbor.
While time-slicing offers flexibility, MIG is preferred for production environments where strict hardware-level fault isolation is required to meet enterprise SLAs. Hardware partitioning ensures that a memory error in one model cannot cause a cascading failure across the shared GPU—a critical requirement for mission-critical Voice AI.
Experimental setup: The voice AI pipeline
To validate these strategies in a production-realistic scenario, we used a multimodal voice-to-voice AI pipeline. This workload is ideal for benchmarking because it mixes three distinct traffic patterns:
- ASR (streaming): Constant, low-compute stream processing with NVIDIA Parakeet 1.1B
- TTS (bursty): Idle for seconds, then spikes to 100% usage to generate audio in milliseconds with NVIDIA Magpie Multilingual
- LLM (heavy): High-compute, high memory usage, Llama-3.1-Nemotron-Nano-VL-8B-V1.
Before optimizing, it’s critical to understand our latency profile. In our voice-to-voice pipeline, the LLM is the dominant bottleneck. Under heavy loads, the LLM accounts for ~9 seconds of the total processing time. This delay can fluctuate significantly based on context length; for instance, high-input scenarios (like training users) or growing conversation histories increase processing overhead compared to short prompts. As history accumulates, the LLM must process more tokens before generating a response, extending the bottleneck that support models must be masked behind.
Consolidating support models like ASR and TTS provides a strategic path to maximize hardware utilization while maintaining end-to-end responsiveness. While consolidation may introduce a slight latency adjustment of 100-200 ms, the gains in infrastructure throughput and ROI are significant.
Our hypothesis
Consolidating ASR and TTS workloads on a single GPU preserves latency and jitter while freeing compute for additional LLM instances.
Experiment
We designed three distinct configurations for testing. In each round, we used three voice samples, waiting for the first response from LLM+TTS to complete. The setup used a Kubernetes cluster, models deployed using NVIDIA NIM, and managed by the NVIDIA NIM Operator. The worker node had access to three NVIDIA A100 Tensor Core GPUs.
- Experiment 1: Baseline with three GPUs
- Setup: One dedicated GPU for each model (LLM, ASR, TTS).
- Goal: Establish the “gold standard” for latency and throughput against which to measure optimization.
- Resource:
nvidia.com/gpu: 1
per pod.
- Experiment 2: Time-slicing with two GPUs
- Setup: LLM retains a dedicated GPU. ASR and TTS share GPU 0 using software-level time-slicing.
- Goal: Test if dynamic scheduling can handle the “noisy neighbor” contention between streaming ASR and bursty TTS.
- Resource:
nvidia.com/gpu: 1
(Shared viareplicas: 2
).
- Experiment 3: MIG Partitioning with two GPUs
- Setup: LLM retains a dedicated GPU. GPU 0 is physically partitioned into two isolated instances.
- Goal: Test if hardware isolation provides better stability than software scheduling.
- Resource:
nvidia.com/mig-3g.40gb: 1
per pod.
Configuration Note: To achieve these topologies, we used specific configurations within the NVIDIA GPU Operator.
- For Experiment 2, we used the
timeSlicing
configuration to advertise multiple replicas per physical GPU. - For Experiment 3, we applied a custom
mig-configs
ConfigMap to partition the GPU into two3g.40gb
instances.
(For the exact kubectl
commands and YAML manifests used to reproduce this setup, please see the Implementation Appendix at the end of this post.)
Results
To evaluate resource fragmentation, we tested the system with two distinct traffic patterns:
- Light load: 5 concurrent users simulating ~135 seconds of sustained interaction.
- Heavy load: 50 concurrent users simulating ~375 seconds of sustained interaction.
Figure 5 compares generative AI inference throughput across traffic patterns. The data shows how partitioning affects process requests as concurrency increases, across baseline (dedicated GPUs), time-slicing (software sharing), and MIG (hardware partitioning) under light and heavy loads. All experiments have a 100% success rate, no failures. The current req/s is the reason for the LLM bottleneck in the pipeline.
Mean latency metrics
The following analysis evaluates how different GPU partitioning strategies impact overall system efficiency and responsiveness.
Throughput compared to latency
Consolidating ASR and TTS workloads onto a single GPU results in an optimized pipeline, enabling the cluster to support more simultaneous AI streams. However, our benchmarks reveal a critical performance divergence between the two partitioning strategies:
- MIG (hardware): Highest efficiency
Experiment 3 achieved the highest per-unit productivity, reaching ~1.00 req/s per GPU. By providing dedicated hardware paths for each instance, MIG eliminates resource contention. Organizations can achieve near-full system capacity while effectively freeing up an entire GPU for other heavy LLM workloads.
- Time-slicing (software): Higher density with overhead
Experiment 2 showed that software-level sharing can also improve per-GPU density compared to the baseline, achieving ~0.76 req/s per GPU. However, the CUDA driver’s management of rapid context switches between streaming and bursty models introduces scheduling overhead. While functional, this software-based approach doesn’t reach the aggregate throughput efficiency provided by hardware partitioning.
Latency and the bursty factor
Time-slicing handles individual bursty tasks slightly faster, with a mean TTS latency of 144.7 ms compared to MIG’s 168.2ms. However, this 23.5 ms difference represents a small fraction of the total end-to-end pipeline response time at the present scale. Under heavy load, the LLM accounts for the vast majority of the total interaction time. Because the end-user cannot perceive a 20ms delta within a multi-second response, the throughput stability of MIG is a more valuable production metric.
Recommendations for partitioning
Based on the benchmark data, we recommend the following decision matrix:
- Default to MIG for production scale and stability
- Experiment 3 showed that MIG handles higher request volumes (2 req/s) with only a minor latency trade-off.
- Strict hardware-level fault isolation prevents a memory overflow in one process from crashing the other.
- Best for production environments where throughput and 100% reliability are the priorities.
- Use time-slicing for development or low-concurrency apps
- This involves a 32% reduction in total throughput and shared-resource dependencies.
- Best for development, CI/CD, and PoCs to run a full pipeline on a minimal hardware footprint.
Get started
- Experiment further: Try the repository.
- Implement partitioning: Follow our Implementation Guide to configure MIG profiles and use the provided YAML manifests to eliminate resource fragmentation in your cluster.
- Scale with NIM: Deploy NVIDIA NIM pipelines to fully utilize your ASR, TTS, and LLM workloads for maximum ROI.
