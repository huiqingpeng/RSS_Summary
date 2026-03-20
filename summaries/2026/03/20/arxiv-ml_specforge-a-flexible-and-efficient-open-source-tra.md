---
title: "SpecForge: A Flexible and Efficient Open-Source Training Framework for Speculative Decoding"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18567"
published: "2026-03-20"
summarized: "2026-03-20T12:13:41.366946"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SpecForge，一个面向生产的开源框架，用于训练投机解码（speculative decoding）模型，并完整支持EAGLE-3架构。该框架通过目标-草稿解耦、混合并行策略和优化训练内核等技术，将Qwen3-235B-A22B的EAGLE-3训练速度提升达9.9倍。研究团队还发布了SpecBundle——一套面向主流开源LLM的生产级EAGLE-3草稿模型，在SGLang上实现了最高4.48倍的端到端推理加速，有效解决了社区中高质量草稿模型稀缺的问题。

【方法概述 / Method】
SpecForge采用目标-草稿解耦（target-draft decoupling）架构，将目标模型与草稿模型的训练分离，结合混合并行策略（hybrid parallelism）和优化的训练内核来提升效率。该框架还与生产级推理引擎（如SGLang）深度集成，支持从训练到部署的全流程。

【实验结果 / Results】
在Qwen3-235B-A22B上的实验表明，SpecForge可实现最高9.9倍的EAGLE-3训练加速。发布的SpecBundle草稿模型在SGLang推理引擎上达到了最高4.48倍的端到端推理速度提升，显著降低了大语言模型的推理延迟。

【应用价值 / Applications】
SpecForge为大规模语言模型的低延迟推理部署提供了实用基础，特别适用于需要实时响应的在线服务场景，如对话系统、代码补全和交互式AI应用。其开源特性和生产级集成能力使研究者和工程师能够快速构建和部署高效的投机解码系统。
