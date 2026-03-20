---
title: "Cliqueformer: Model-Based Optimization with Structured Transformers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2410.13106"
published: "2026-03-20"
summarized: "2026-03-20T14:05:03.179549"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Cliqueformer，一种基于结构化Transformer的模型优化（MBO）方法，通过功能图模型（FGM）学习黑箱函数的结构特征，从而在不依赖显式保守策略的情况下解决分布偏移问题。该架构将神经网络强大的预测能力与函数结构建模相结合，在蛋白质工程和材料发现等设计任务中实现了优于现有方法的性能。研究表明，利用目标函数的内在结构可以显著提升离线模型优化效果。

【方法概述 / Method】
Cliqueformer采用Transformer架构，并引入功能图模型（FGM）来显式建模黑箱函数的结构关系，通过结构学习指导优化过程。该方法区别于传统的强化学习和生成建模MBO方法，无需显式的保守性约束即可处理分布外样本，实现了更高效的探索-利用平衡。

【实验结果 / Results】
在化学设计和遗传设计等多个领域的基准测试中，Cliqueformer均优于现有的模型优化方法。实验表明，通过结构化Transformer捕获的函数相关性能够有效指导设计空间中的高质量样本生成，在保持预测准确性的同时提升了优化效率。

【应用价值 / Applications】
Cliqueformer可直接应用于蛋白质工程、材料发现和药物设计等科学发现场景，加速从大规模预测模型到实际优化设计的转化。该方法为需要昂贵实验验证的领域提供了高效的计算筛选工具，有望降低研发成本并缩短设计周期。
