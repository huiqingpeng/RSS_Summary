---
title: "Natural Gradient Descent for Online Continual Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20898"
published: "2026-03-24"
summarized: "2026-03-25T07:15:37.830683"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对在线持续学习（Online Continual Learning, OCL）中快速收敛与灾难性遗忘的挑战，提出了一种基于自然梯度下降（Natural Gradient Descent）的新型训练方法。该方法通过Kronecker分解近似曲率（KFAC）对Fisher信息矩阵进行近似，显著提升了OCL模型的性能。实验表明，该方法在Split CIFAR-100、CORE50和Split miniImageNet等数据集上均取得显著改进，且能与现有OCL技巧有效结合。

【方法概述 / Method】
论文采用自然梯度下降优化器替代传统的随机梯度下降，利用KFAC（Kronecker Factored Approximate Curvature）技术对Fisher信息矩阵进行高效近似，从而在参数空间中沿着最速下降方向更新模型。这一方法能够在在线非独立同分布（non-i.i.d.）数据流场景下，更有效地平衡新任务学习与旧知识保持。

【实验结果 / Results】
实验在Split CIFAR-100、CORE50和Split miniImageNet三个标准OCL基准数据集上进行，结果表明所提出的自然梯度下降方法在所有OCL基线方法上均带来显著性能提升。特别地，当与现有的OCL技巧（如经验回放、正则化等）结合时，性能改善尤为明显，同时实现了更快的收敛速度。

【应用价值 / Applications】
该研究适用于需要模型持续学习新类别、同时保持旧知识的实际场景，如自动驾驶中的实时物体识别、工业质检中的缺陷分类系统，以及个性化推荐系统等。方法通过提升在线学习效率，降低了计算资源消耗，使持续学习模型更适合部署在资源受限的边缘设备上。
