---
title: "Removing the Guesswork from Disaggregated Serving"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/removing-the-guesswork-from-disaggregated-serving/"
published: "2026-03-09"
fetched: "2026-03-10T12:44:06.892585"
---

Deploying and optimizing large language models (LLMs) for high-performance, cost-effective serving can be an overwhelming engineering problem. The ideal configuration for any given workload (such as hardware, parallelism, and prefill/decode split) resides in a massive, multi-dimensional search space that is impossible to explore manually or through exhaustive testing. AIConfigurator, an open source tool that simplifies the NVIDIA Dynamo AI serving stack, is intended to cut through this complexity and get you to an optimal deployment in minutes.
The core benefit of AIConfigurator is that you don’t need to run every possible configuration on real hardware to predict which one will perform best. Instead, it decomposes LLM inference into its constituent operations and measures each one in isolation on the target GPU. AIConfigurator can then reassemble those measurements to estimate the end-to-end performance of any configuration, all without occupying a single GPU-hour at search time.
This blog will provide a quick overview of how AIConfigurator works; how to use it with Dynamo; and how ecosystem contributors such as Alibaba and Mooncake are helping extend the features of this open source project to all frameworks.
Using AIConfigurator to configure disaggregated serving
With AIConfigurator, the latency estimate for each operation—including General Matrix Multiplications (GEMM), attention, communication, and mixture-of-experts (MoE) dispatch—is backed by real kernel measurements collected on the target hardware. The collector toolchain benchmarks every primitive across supported quantization modes, batch sizes, sequence lengths, and GPU counts, and logs results to a silicon-calibrated performance database. When collected data isn’t available for a new model or GPU, AIConfigurator falls back to speed-of-light roofline estimates with empirical correction factors, giving usable recommendations even before the model has been empirically profiled.
On top of this estimation layer, AIConfigurator models continuous batching for aggregated serving, rate-matches prefill and decode worker pools for disaggregated serving, and handles MoE-specific concerns like expert parallelism and token routing skew. Rather than returning a single answer, it computes the Pareto frontier across all evaluated configurations, showing the throughput-vs-latency tradeoff for both aggregated and disaggregated modes side-by-side. The full search, often spanning tens of thousands of candidate configurations, completes in seconds, instead of spending days searching on GPUs.
To see how this tool can help you as a developer, consider a concrete example: deploying Qwen3-32B with NVFP4 quantization across 64 NVIDIA B200 GPUs, with target SLAs of 1000ms time-to-first-token (TTFT) and 15ms time-per-output-token (TPOT). Using a single command, you can search through thousands of candidate configurations:
pip install aiconfigurator # or install from source for latest
aiconfigurator cli default \
--model-path nvidia/Qwen3-32B-NVFP4 \
--total-gpus 64 \
--system b200_sxm \
--isl 15000 --osl 500 \
--ttft 1000 --tpot 15 \
--save-dir ./results
Within seconds, AIConfigurator returns a recommendation. In this example, disaggregated serving achieves 550 tokens/s/GPU, a 38% improvement over the best aggregated configuration. The output includes a Pareto frontier visualizing the full tradeoff space, ranked configurations (best_config_topn.csv
), engine configurations for each worker type, and ready-to-use deployment artifacts for both serving modes.
For disaggregated serving in Dynamo, deploying the recommended configuration requires a single command:
kubectl apply -f results/disagg/top1/k8s_deploy.yaml
This workflow generalizes across models and hardware. The same interface applies whether deploying Qwen3-32B on eight NVIDIA H200 GPUs or DeepSeek-V3 across a multi-node B200 cluster; AIConfigurator adapts its search space and recommendations to the specified model, hardware, and SLA constraints.
Extending support to multiple frameworks
AIConfigurator originally supported only NVIDIA TensorRT LLM, but as frameworks like SGLang gained traction—particularly for MoE models like DeepSeek—single-backend support was no longer sufficient. We designed a framework-agnostic abstraction layer with a unified parameter mapping that normalizes each backend’s config schemas and terminology behind a single interface. That investment paid off when community partners such as Mooncake and Alibaba brought SGLang support to life, contributing collectors, validation, and integration work covered in the following sections.
From a user’s perspective, comparing backends is a one-flag change:
# TensorRT LLM
aiconfigurator cli default \
--model-path nvidia/Qwen3-32B-NVFP4 \
--total-gpus 64 --system b200_sxm \
--backend trtllm
# SGLang
aiconfigurator cli default \
--model-path nvidia/Qwen3-32B-NVFP4 \
--total-gpus 64 --system b200_sxm \
--backend sglang
# vLLM
aiconfigurator cli default \
--model-path nvidia/Qwen3-32B-NVFP4 \
--total-gpus 64 --system b200_sxm \
--backend vllm
To make it even simpler, --backend auto
compares three frameworks in one command:
aiconfigurator cli default \
--model-path nvidia/Qwen3-32B-NVFP4 \
--total-gpus 64 --system b200_sxm \
--backend auto
The search process is identical across backends; only the generated deployment artifacts differ, with each backend receiving native config files, CLI arguments, and K8s manifests in its expected format. AIConfigurator currently ships with silicon-validated performance data for TensorRT LLM and SGLang across NVIDIA H100, H200, and B200 systems, with vLLM support on select platforms as well.
WideEP inference for SGLang
SGLang is especially popular for running “Wide Expert Parallelism” (WideEP), which dramatically increases decode throughput for MoE models like DeepSeek V3/R1 by distributing experts across a large number of GPUs. To accurately model SGLang’s WideEP pathway, AIConfigurator simulates key elements like DeepEP all-to-all communication, MTP, MLA attention, Attention DP, workload-aware MoE, and expert parallel load balancing (EPLB). Modeling MoE and EPLB poses the greatest challenge.
WideEP’s MoE routing inherently suffers from load imbalance, with some experts receiving more tokens than others. AIConfigurator models this power-law workload distribution using an alpha parameter. This alpha acts as a lookup key in the performance database, linking distribution patterns to collected latency profiles, similar to the standard MoE path. An alpha of 1.01 empirically fits DeepSeek V3.1 well for both prefill and decode across datasets.
In WideEP deployments, AIConfigurator models EPLB by adjusting two factors instead of directly simulating the algorithm. First, the workload distribution alpha is lowered from 1.01 to 0.6 to reflect the load smoothing from expert replication. Second, the effective token count is multiplied by 0.8, modeling the empirical reduction in maximum per-GPU token load. These changes select the correct latency curve and adjust the operating point accordingly.
Preliminary results are promising: The best configuration identified by AIConfigurator aligns with the manually tuned production configuration. Further collaboration is planned to bring this to production readiness.
How the SGLang community is contributing
Mooncake: Initial SGLang support in AIConfigurator
AIConfigurator initially supported only TensorRT LLM, reserving interfaces for SGLang and vLLM without full implementation. Contributors from Mooncake (an open source collaboration between Moonshot AI, Tsinghua University, and others) then developed the first version of the SGLang backend.
They first completed the collector layer, modeling and encapsulating core operations (GEMM, attention, batch-GEMM). This allowed quick support for models like Llama, Qwen, and DeepSeek. This work, combined with the subsequent SGLang WideEP effort, formed the first SGLang backend for AIConfigurator.
Alibaba: Integrating AIConfigurator in the AI Serving Stack for automated deployments
The AI Serving Stack, built on the Alibaba Container Service for Kubernetes (ACK), is an end-to-end solution for efficient and scalable cloud-native LLM inference. It manages the entire lifecycle, offering deployment, smart routing, auto-scaling, and deep observability.
Within this stack, the RoleBasedGroup (RBG), an SGLang community-incubated AI orchestration engine to which Alibaba Cloud heavily contributes, simplifies LLM inference service deployment on Kubernetes. RBG uses “Role” as its core orchestration unit, dividing prefill-decode-disaggregation based services into router, prefill, and decode roles to coordinate their placement, scaling, and updates. That ensures a balance of performance and stability with role-based extensibility.
The full Dynamo service stack can be deployed with the AI Serving Stack on ACK, leveraging the AIConfigurator prediction results as input and AIConfigurator’s generator module. The ACK team can generate the deployable configuration for RBG, reference here. By integrating this process, Alibaba achieved 1.86x the throughput on the Qwen3-235B-FP8 model compared to the baseline, while maintaining TTFT <5000ms and ITL<40ms.
RBG will continue to track AIConfigurator’s progress and provide Day 0 support for rapid deployment of new models in ACK.
Alibaba: Building HiSim based on AIConfigurator
AIConfigurator optimizes static workloads, but it cannot easily model dynamic, bursty production traffic, complex scheduling, and KV cache dynamics. To overcome this, the Alibaba TAIR KV Cache Team created Tair-KVCache-HiSim, a lightweight, high-fidelity, and event-driven system simulator.
HiSim tackles dynamic traffic and queuing (predicting TTFT, TPOT, and throughput under variable rates and complex scheduling like SGLang) and advanced KV cache optimization (quantifying tradeoffs for multi-level storage and various eviction/prefetch policies) via system-level simulation.
HiSim comprises a workload generator, global router simulator, and the inference engine simulator (IES). The IES uses a unified global clock to coordinate the scheduler simulator (managing LLM requests: preemption, batching), the KVCache Manager Simulator (HiCacheController, modeling the three-level KV cache and eviction), and the BatchRunnerEstimator (AIConfiguratorTimePredictor, calculating batch latency based on AIConfigurator).
This structure adapts rapidly to diverse inference engines (vLLM, SGLang, TensorRT LLM), accurately mimicking real-world configurations, runtime parameters, and execution semantics (parallelism, batching, device optimizations) without engine modification, ensuring high fidelity.
HiSim guides SGLang R&D by allowing configuration tuning to quantify scheduling tradeoffs (TTFT/throughput, queueing/memory, cache hit/TTFT, overlap efficiency) without code changes. It provides “oracle” evaluation for new hardware by estimating performance ceilings and identifying bottlenecks using theoretical specs. HiSim also aids HiCache architecture exploration and cost/performance optimization through three-level KV cache design (e.g., L2 size, prefetch/eviction policy, L3 bandwidth needs, write-through vs write-back) to find the best cost–performance point.
Leveraging AIConfigurator, HiSim extends static analysis to active, cost-aware deployment recommendations for dynamic traffic. The end-to-end simulation is within 5% error of real-world performance. Future work will enhance this collaboration to build a high-fidelity, production-ready system simulator.
What’s next for AIConfigurator
The roadmap ahead extends AIConfigurator from a standalone command line tool into a core component of the Dynamo platform:
- Faster model support. “Hybrid” mode already provides Day 1 recommendations via speed-of-light estimates; we are also automating the silicon data-collection pipeline to accelerate fully validated support.
- Powering Dynamo deployments. AIConfigurator is becoming the configuration engine behind Dynamo’s Kubernetes flow via the DynamoGraphDeploymentRequest (DGDR) CRD, producing optimized deployments from a single YAML file.
- Dynamic workload modeling. Moving beyond static input sequence length/output sequence length/concurrency targets toward models that capture production workload distributions directly.
NVIDIA plans to keep working with third parties on bringing AIConfigurator to more systems and tools. AIConfigurator is actively welcoming contributions, including performance data for new hardware, additional backend support, new features, and extensions like HiSim.
See the AIConfigurator repository to get started, and check out the Dynamo project for the fastest way to set up disaggregated serving.
For a full technical treatment, including formal definitions and validation results, read our paper: AIConfigurator: Lightning-Fast Configuration Optimization for Multi-Framework LLM Serving.
