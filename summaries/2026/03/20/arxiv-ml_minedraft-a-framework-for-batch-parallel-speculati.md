---
title: "MineDraft: A Framework for Batch Parallel Speculative Decoding"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18016"
published: "2026-03-20"
summarized: "2026-03-20T13:07:21.578561"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了MineDraft，一种批并行推测解码（PSD）框架，通过将起草（drafting）与验证（verification）阶段重叠执行来隐藏起草延迟，从而克服标准推测解码（SD）中严格串行执行的性能瓶颈。理论分析表明PSD比标准SD具有显著更高的效率。实验结果显示，MineDraft在吞吐量上最高提升75%，端到端延迟最高降低39%，并已成功实现为vLLM插件以验证其生产实用性。

【方法概述 / Method】

MineDraft采用双批次请求管理机制，维护两个独立的请求批次，使一个批次的起草过程与另一个批次的验证过程并行执行，实现真正的批并行推测解码。该设计通过时间重叠有效隐藏了小模型起草的计算延迟，同时保持了大模型验证的准确性保证。

【实验结果 / Results】

与标准推测解码相比，MineDraft在多个评估维度上取得显著性能提升：吞吐量提高最高达75%，端到端延迟降低最高达39%。此外，该框架已作为插件集成到广泛使用的vLLM推理系统中，证明了其在实际生产环境中的可行性和易部署性。

【应用价值 / Applications】

MineDraft可直接应用于大规模语言模型在线推理服务，如聊天机器人、代码生成助手等需要低延迟高吞吐的场景。作为vLLM插件的实现方式使其能够快速部署到现有生产环境，为云服务提供商和AI应用开发者提供即插即用的推理加速解决方案，降低部署成本的同时提升用户体验。
