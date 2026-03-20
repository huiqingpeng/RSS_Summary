---
title: "A Simple Efficiency Incremental Learning Framework via Vision-Language Model with Nonlinear Multi-Adapters"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.11211"
published: "2026-03-20"
summarized: "2026-03-20T16:18:37.354747"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SimE，一种简单高效的增量学习框架，通过视觉-语言模型配合专门设计的适配器来解决增量学习中的三大挑战：训练效率、对记忆库的依赖以及对强骨干网络的需求。研究发现适配器连接数量与模型增量学习能力之间存在非线性关联——增加Transformer块间的适配器连接能提升性能，但在较小增量步骤中增加块内的自适应连接反而可能降低学习效果。SimE在TinyImageNet上超越传统方法9.6%，在CIFAR-100上优于其他CLIP基线方法5.3%。

【方法概述 / Method】
SimE采用预训练视觉-语言模型（如CLIP）作为骨干，并引入专为增量学习任务设计的非线性多适配器结构。该方法通过精心设计的适配器连接策略，在Transformer块间和块内建立自适应连接，同时避免存储历史数据的记忆库，实现高效的参数更新和知识保留。

【实验结果 / Results】
实验表明SimE在多个基准数据集上取得显著性能提升：相比传统增量学习方法在TinyImageNet上提升9.6%，相比其他基于CLIP的方法在CIFAR-100上提升5.3%。系统研究还发现，使用在更大规模数据集（如LAION2B）上训练、更强架构（如ViT-L/14）的CLIP模型可进一步增强SimE的零样本能力。

【应用价值 / Applications】
该研究适用于需要持续学习新任务且无法存储大量历史数据的实际场景，如边缘设备上的连续视觉识别、个性化推荐系统的动态更新、以及资源受限环境下的模型部署。SimE的高效性和无需记忆库的特性使其特别适合计算资源有限但需要持续适应新任务的应用。
