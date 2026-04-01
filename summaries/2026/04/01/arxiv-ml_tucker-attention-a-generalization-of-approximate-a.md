---
title: "Tucker Attention: A generalization of approximate attention mechanisms"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.30033"
published: "2026-04-01"
summarized: "2026-04-02T07:22:10.911955"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Tucker Attention，一种对近似注意力机制的泛化框架，旨在降低多头自注意力（MHA）的内存占用。该框架通过统一的低秩分解视角，将GQA、MLA和MHA统一为特例，并实现了比现有方法（GQA和MLA）少一个数量级参数的同时保持可比的验证指标。此外，Tucker Attention完全兼容Flash Attention和旋转位置编码（RoPE），并为理解这些注意力变体的实际秩行为提供了理论洞察。

【方法概述 / Method】
Tucker Attention基于Tucker分解（一种高阶张量分解方法），对自注意力层中的权重对象进行广义低秩分解，而非局限于嵌入维度或注意力头的特定分解方式。该方法通过在不同模式（modes）上施加低秩约束，构建了一个参数高效的参数化方案，能够灵活地恢复现有注意力变体作为其特例。

【实验结果 / Results】
在大型语言模型（LLM）和视觉Transformer（ViT）的测试案例中，Tucker Attention相比GQA和MLA实现了约10倍的参数减少，同时保持相当的验证集性能指标。该框架还揭示了MHA、GQA和MLA在实际训练中达到的真实秩，并据此提出了MLA的简化方案。

【应用价值 / Applications】
Tucker Attention可直接应用于需要高效部署Transformer模型的场景，如边缘设备上的大语言模型推理和资源受限环境下的视觉任务处理。其理论框架为理解和设计新的注意力机制提供了系统化的工具，有助于推动更高效、可解释的模型架构发展。
