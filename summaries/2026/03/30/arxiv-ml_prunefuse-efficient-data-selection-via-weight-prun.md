---
title: "PruneFuse: Efficient Data Selection via Weight Pruning and Network Fusion"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26138"
published: "2026-03-30"
summarized: "2026-03-31T07:22:15.480134"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了PruneFuse，一种通过权重剪枝和网络融合实现高效数据选择的新策略。该方法首先利用结构化剪枝构建与原始网络结构一致的小型剪枝网络进行数据选择，随后将训练好的剪枝网络与原始网络融合以优化训练过程。实验表明，PruneFuse显著降低了数据选择的计算成本，在多个数据集上优于基线方法，并加速了整体训练过程。

【方法概述 / Method】
PruneFuse采用两阶段策略：第一阶段应用结构化剪枝创建小型剪枝网络，利用其与原始网络的结构一致性进行高效数据选择；第二阶段将训练后的剪枝网络与原始网络无缝融合，借助剪枝网络的学习 insights 促进融合网络的训练，同时保留发现更鲁棒解的空间。

【实验结果 / Results】
在多个数据集上的广泛实验表明，PruneFuse相比传统方法显著降低了数据选择的计算开销，同时取得了优于基线方法的性能表现，并实现了整体训练过程的加速。

【应用价值 / Applications】
PruneFuse可应用于深度学习模型训练中的高效数据选择场景，特别适用于大规模数据集和计算资源受限的环境，能够有效减少数据标注需求和训练成本，对提升深度学习训练效率和降低实际部署成本具有重要价值。
