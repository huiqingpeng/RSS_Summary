---
title: "NVIDIA Vera CPU Delivers High Performance, Bandwidth, and Efficiency for AI Factories"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/nvidia-vera-cpu-delivers-high-performance-bandwidth-and-efficiency-for-ai-factories/"
published: "2026-03-16"
summarized: "2026-03-17T07:09:07.186479"
ai_provider: "openai"
---

【是什么 / What it is】

NVIDIA Vera CPU 是 NVIDIA 首款全定制数据中心 CPU，专为现代 AI 工作负载设计，特别是强化学习（RL）后训练和智能体（agentic）推理场景。它采用 88 个自研 Olympus 核心，配备第二代可扩展一致性互连（SCF）和 1.2 TB/s 的 LPDDR5X 内存带宽，旨在解决 AI 工厂中 CPU 成为性能瓶颈的"Amdahl 定律"问题。

The NVIDIA Vera CPU is NVIDIA's first fully custom data center CPU, designed specifically for modern AI workloads, particularly reinforcement learning (RL) post-training and agentic inference scenarios. It features 88 self-developed Olympus cores, second-generation Scalable Coherency Fabric (SCF), and 1.2 TB/s LPDDR5X memory bandwidth, aiming to address the "Amdahl's law" problem where CPUs become performance bottlenecks in AI factories.

【为什么重要 / Why it matters】

随着推理模型和智能体 AI 的兴起，token 需求激增，传统 CPU 在串行任务、单线程性能和内存带宽方面的不足严重制约 GPU 利用率。Vera CPU 通过 50% 更快的沙箱性能、3 倍于传统 CPU 的每核内存带宽，以及确定性低延迟执行，确保 AI 工厂能高效扩展，避免训练周期中的 token 浪费，加速模型迭代。

As reasoning models and agentic AI surge, token demand explodes, and traditional CPUs' limitations in serial tasks, single-threaded performance, and memory bandwidth severely constrain GPU utilization. The Vera CPU delivers 50% faster sandbox performance, 3x per-core memory bandwidth versus traditional CPUs, and deterministic low-latency execution—ensuring AI factories scale efficiently, avoiding token waste in training cycles and accelerating model iteration.

【我能用什么 / How I can use it】

若从事 AI 基础设施规划，可评估 Vera CPU 用于 RL 后训练集群和智能体服务部署，利用其 SMT 特性在性能与线程数间动态调优；若开发 AI 应用，可设计更复杂的工具调用链和代码生成-验证-执行闭环，依托 Vera 的高单核性能和低尾延迟特性；若关注能效，可参考其 LPDDR5X + SOCAMM 设计思路，在低功耗内存与可维护性间取得平衡。

For AI infrastructure planning, evaluate Vera CPUs for RL post-training clusters and agentic service deployment, leveraging SMT to dynamically tune between performance and thread count; for AI application development, design more complex tool-calling chains and code generation-validation-execution loops, capitalizing on Vera's high single-core performance and low tail latency; for energy efficiency focus, reference its LPDDR5X + SOCAMM design approach to balance low-power memory with serviceability.
