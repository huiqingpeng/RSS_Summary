---
title: "NVIDIA Extreme Co-Design Delivers New MLPerf Inference Records"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/nvidia-extreme-co-design-delivers-new-mlperf-inference-records/"
published: "2026-04-01"
summarized: "2026-04-02T07:09:06.444381"
ai_provider: "openai"
---

【是什么 / What it is】

本文介绍了NVIDIA在MLPerf Inference v6.0基准测试中创下的新纪录，展示了Blackwell Ultra GPU平台通过硬件、软件与模型的协同设计（Extreme Co-Design）实现的领先AI推理性能。文章详细说明了新增的五个基准测试场景（包括DeepSeek-R1 Interactive、Qwen3-VL-235B-A22B等），以及TensorRT-LLM和Dynamo软件优化带来的显著性能提升。

This article introduces NVIDIA's new records in the MLPerf Inference v6.0 benchmark, demonstrating the leading AI inference performance achieved by the Blackwell Ultra GPU platform through Extreme Co-Design of hardware, software, and models. It details five newly added benchmark scenarios (including DeepSeek-R1 Interactive, Qwen3-VL-235B-A22B, etc.) and significant performance gains from TensorRT-LLM and Dynamo software optimizations.

---

【为什么重要 / Why it matters】

这代表了AI工厂（AI Factory）效率的新标杆——通过软件优化在相同硬件上实现2.7倍吞吐量提升，将单token成本降低60%以上，直接影响AI服务提供商的盈利能力和规模扩展能力。NVIDIA累计291次MLPerf胜绩（是其他所有提交者总和的9倍）及其14家合作伙伴的广泛参与，进一步巩固了其作为AI基础设施事实标准的地位。

This represents a new benchmark for AI Factory efficiency—achieving 2.7x throughput improvement on identical hardware through software optimization, reducing per-token cost by over 60%, directly impacting AI service providers' profitability and scaling capabilities. NVIDIA's cumulative 291 MLPerf wins (9x all other submitters combined) and broad participation from 14 partners further solidify its position as the de facto standard for AI infrastructure.

---

【我能用什么 / How I can use it】

对于AI基础设施决策者，应优先考虑支持持续软件优化的全栈平台（而非仅关注峰值算力），并评估Disaggregated Serving、Wide Expert Parallel等新技术在MoE模型推理中的部署潜力。开发者可关注NVIDIA Dynamo开源框架的KV-aware routing和Multi-Token Prediction特性，以优化高交互场景下的推理效率；同时参考MLPerf新增的多模态和视频生成基准，规划面向下一代AI应用的架构设计。

For AI infrastructure decision-makers, prioritize full-stack platforms supporting continuous software optimization (rather than peak compute specs alone), and evaluate emerging technologies like Disaggregated Serving and Wide Expert Parallel for MoE model inference deployment. Developers should explore NVIDIA Dynamo open-source framework's KV-aware routing and Multi-Token Prediction features to optimize inference efficiency in high-interactivity scenarios; meanwhile, reference MLPerf's new multi-modal and video generation benchmarks to architect for next-generation AI applications.
