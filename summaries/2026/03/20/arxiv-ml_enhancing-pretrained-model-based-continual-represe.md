---
title: "Enhancing Pretrained Model-based Continual Representation Learning via Guided Random Projection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19145"
published: "2026-03-20"
summarized: "2026-03-20T13:05:54.004331"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对基于预训练模型的持续表示学习（Continual Representation Learning）中随机投影层（RPL）在严重领域偏移下表达能力不足的问题，提出了SCL-MGSM方法。该方法通过MemoryGuard监督机制（MGSM）以数据引导的方式逐步选择目标对齐的随机基，构建紧凑而具表达力的投影层，同时改善解析更新的数值稳定性。在多个无示例类增量学习基准上的实验表明，SCL-MGSM显著优于现有最先进方法。

【方法概述 / Method】

SCL-MGSM的核心是MemoryGuard监督机制，该机制通过数据驱动的原则性方法替代随机初始化，逐步筛选与目标域对齐的随机基向量来构建投影层。这种方法在保持RPL紧凑维度的同时增强了对预训练表示的适应能力，并确保特征矩阵的良好条件数以稳定后续的递归解析更新。

【实验结果 / Results】

论文在多个无示例类增量学习（Class Incremental Learning without exemplars）基准上进行了广泛实验，结果表明SCL-MGSM相比现有最先进方法取得了更优的性能。具体而言，该方法在保持较低投影维度的同时，有效解决了大领域偏移下的表示适应问题，并提升了线性分类头解析更新的稳定性。

【应用价值 / Applications】

该研究适用于资源受限场景下的持续学习系统，如边缘设备上的增量视觉识别、流式数据分类等应用，能够在不存储历史样本（exemplar-free）的情况下高效适应新任务。其紧凑的投影层设计降低了计算和存储开销，同时数据引导的基选择机制提升了预训练模型向目标域迁移的可靠性。
