---
title: "Learning to Recall with Transformers Beyond Orthogonal Embeddings"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15923"
published: "2026-03-18"
summarized: "2026-03-18T16:08:40.684040"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了在有限数据和非正交（随机）嵌入条件下，单层Transformer学习存储和检索知识的能力。作者通过分析梯度下降早期阶段的动态，推导出模型存储容量的显式公式，发现样本量N、嵌入维度d和序列长度L之间存在乘法依赖关系。该研究还提供了统计问题的下界，证明这种乘法缩放特性在非正交嵌入条件下是内在的。

【方法概述 / Method】

论文采用理论分析结合数值验证的方法，研究单层Transformer在简单token检索任务上的学习动态。具体而言，模型需要在长度为L的序列中识别信息性token，并学习从token到标签的一对一映射，分析重点追踪梯度下降早期阶段的权重演化过程。

【实验结果 / Results】

理论分析揭示了存储容量与N、d、L的乘法依赖关系，并通过数值实验验证了这些缩放规律。此外，研究还建立了该统计问题的下界，表明所发现的乘法缩放特性是问题固有的，而非算法缺陷。

【应用价值 / Applications】

该研究为理解大语言模型的知识存储机制提供了更贴近现实的理论基础，有助于指导模型设计和训练策略的优化。研究成果可应用于评估和改进Transformer在有限数据条件下的学习效率，对资源受限场景下的模型部署具有实际指导意义。
