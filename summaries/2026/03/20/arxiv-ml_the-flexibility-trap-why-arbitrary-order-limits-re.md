---
title: "The Flexibility Trap: Why Arbitrary Order Limits Reasoning Potential in Diffusion Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.15165"
published: "2026-03-20"
summarized: "2026-03-20T15:03:27.777187"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文揭示了扩散大语言模型（dLLMs）中一个反直觉的现象：虽然任意顺序生成理论上扩展了解决空间，但实际上却限制了模型的推理能力。研究发现dLLMs会利用顺序灵活性绕过关键的高不确定性token，导致解空间过早坍塌。为此，作者提出JustGRPO方法，通过放弃任意顺序生成、采用标准GRPO训练，在保留并行解码能力的同时显著提升了推理性能。

【方法概述 / Method】

作者提出JustGRPO方法，核心思想是故意放弃dLLMs的任意顺序生成灵活性，转而采用标准的自左向右生成顺序。该方法直接使用Group Relative Policy Optimization（GRPO）进行强化学习训练，无需处理组合轨迹和难解似然等复杂问题，同时通过特殊的掩码策略保留dLLMs的并行解码能力。

【实验结果 / Results】

JustGRPO在多个推理基准上取得显著效果：GSM8K数学推理准确率达89.1%，大幅超越现有dLLM推理方法。实验表明，固定顺序生成配合标准GRPO不仅简化了训练流程，还有效避免了模型利用灵活性绕过关键推理步骤的问题，充分释放了dLLMs的推理潜力。

【应用价值 / Applications】

该研究为扩散语言模型的训练范式提供了重要启示，表明"灵活性陷阱"可能存在于其他生成模型中。JustGRPO方法可直接应用于需要高效推理的场景（如数学求解、代码生成），在保持dLLMs并行生成速度优势的同时获得接近自回归模型的推理质量，为工业级部署提供了更简洁有效的解决方案。
