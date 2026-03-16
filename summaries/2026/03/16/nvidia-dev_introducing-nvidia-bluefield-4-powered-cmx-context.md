---
title: "Introducing NVIDIA BlueField-4-Powered CMX Context Memory Storage Platform for the Next Frontier of AI"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/introducing-nvidia-bluefield-4-powered-inference-context-memory-storage-platform-for-the-next-frontier-of-ai/"
published: "2026-03-16"
summarized: "2026-03-17T07:07:38.371481"
ai_provider: "openai"
---

【是什么 / What it is】

本文介绍 NVIDIA 推出的 CMX（Context Memory Storage Platform）上下文内存存储平台，这是基于 BlueField-4 处理器和 STX 参考架构的新型存储层级，专门用于解决 AI 推理中 KV 缓存（Key-Value cache）的扩展难题。随着 Agentic AI 工作负载的兴起，模型上下文窗口扩展至数百万 token，传统存储层级（G1-G4）在性能、成本和能效之间难以平衡，CMX 通过在 POD 级别创建专门的 G3.5 层级来填补这一空白。

This article introduces NVIDIA's CMX (Context Memory Storage Platform), a new storage tier built on the BlueField-4 processor and STX reference architecture, designed to address the scaling challenges of KV cache (Key-Value cache) in AI inference. As agentic AI workloads emerge with context windows expanding to millions of tokens, traditional storage tiers (G1-G4) struggle to balance performance, cost, and energy efficiency; CMX fills this gap by creating a dedicated G3.5 tier at the POD level.

---

【为什么重要 / Why it matters】

Agentic AI 的爆发使得 KV 缓存从临时数据转变为模型的"长期记忆"，需要在多轮对话、工具和会话间持久化共享，但现有存储层级迫使企业在稀缺的 GPU HBM 与通用企业存储之间二选一，导致 GPU 利用率低下、每 token 成本飙升、功耗激增。CMX 通过 5 倍提升 token 吞吐量和 5 倍降低功耗，为 AI 工厂提供了可扩展、高能效的上下文存储基础设施，是支撑万亿参数模型和实时推理的关键技术突破。

The explosion of agentic AI transforms KV cache from temporary data into the model's "long-term memory," requiring persistence and sharing across turns, tools, and sessions. Yet existing storage tiers force a binary choice between scarce GPU HBM and general-purpose enterprise storage, leading to underutilized GPUs, soaring per-token costs, and power consumption spikes. By delivering 5× higher token throughput and 5× better power efficiency, CMX provides scalable, energy-efficient context storage infrastructure for AI factories—a critical technical breakthrough supporting trillion-parameter models and real-time inference.

---

【我能用什么 / How I can use it】

若您正在构建或运营大规模 AI 推理基础设施，可评估将 CMX 作为 G3.5 层级整合到现有存储架构中，利用 NVIDIA Dynamo 等编排框架管理跨层级的 KV 缓存流动；对于 AI 应用开发者，应设计支持长上下文窗口和跨会话记忆保留的 Agentic 工作流，以充分利用 CMX 的预加载能力；同时关注 Vera Rubin 平台的整体架构演进，将计算、网络和存储机架作为可配置的 AI 工厂构建模块进行规划。

If you're building or operating large-scale AI inference infrastructure, evaluate integrating CMX as a G3.5 tier into your existing storage architecture, using orchestration frameworks like NVIDIA Dynamo to manage KV cache movement across tiers; for AI application developers, design agentic workflows that support long context windows and cross-session memory retention to leverage CMX's pre-staging capabilities; also monitor the Vera Rubin platform's evolution, planning compute, networking, and storage racks as configurable building blocks for AI factories.
