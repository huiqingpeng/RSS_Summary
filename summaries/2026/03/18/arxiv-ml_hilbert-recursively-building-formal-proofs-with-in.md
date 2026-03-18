---
title: "Hilbert: Recursively Building Formal Proofs with Informal Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.22819"
published: "2026-03-18"
summarized: "2026-03-18T17:11:52.481394"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 Hilbert，一个智能体框架，旨在弥合大型语言模型（LLM）非形式化数学推理能力与形式化定理证明之间的差距。Hilbert 通过递归分解策略，将复杂问题拆分为子目标，并协同调度非形式化推理 LLM、专用 Lean 4 证明器 LLM、形式化验证器和语义定理检索器四个组件，利用验证器反馈迭代修正错误证明。实验表明，Hilbert 在 miniF2F 基准上达到 99.2% 的准确率，在 PutnamBench 上解决 70.0% 的问题（462/660），显著超越现有公开可用方法及专有系统如 SeedProver。

【方法概述 / Method】

Hilbert 采用智能体架构，核心机制为递归问题分解：当专用证明器 LLM 无法直接求解时，系统将问题拆分为更简单的子目标，由证明器或非形式化推理 LLM 分别处理。系统通过形式化验证器检查证明正确性，并基于错误反馈进行迭代优化，同时利用语义定理检索器增强上下文知识支持。

【实验结果 / Results】

Hilbert 在多个关键基准上取得领先性能：miniF2F 达到 99.2%（较最佳公开方法提升 6.6 个百分点）；PutnamBench 解决 462/660 问题（70.0%），超越 SeedProver（50.4%）等专有方案，较最佳公开基线提升 422%。

【应用价值 / Applications】

Hilbert 为数学证明自动化提供了高可靠性的解决方案，可应用于数学研究辅助、形式化验证的教育工具开发，以及需要严格正确性保证的软硬件系统验证等领域，有效结合非形式化推理的灵活性与形式化验证的严谨性。
