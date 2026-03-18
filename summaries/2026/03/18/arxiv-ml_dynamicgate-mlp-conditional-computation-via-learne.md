---
title: "DynamicGate MLP Conditional Computation via Learned Structural Dropout and Input Dependent Gating for Functional Plasticity"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16367"
published: "2026-03-18"
summarized: "2026-03-18T15:43:09.821634"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DynamicGate-MLP框架，将dropout的正则化视角与条件计算的动态执行视角统一起来。该方法通过学习输入依赖的门控机制替代随机掩码，在推理时生成离散执行掩码来选择执行路径，实现样本自适应的计算分配。训练过程中通过期望门控使用量的惩罚项控制计算预算，并采用Straight-Through Estimator优化离散掩码。实验表明该方法在多个数据集上有效平衡了模型性能与计算效率。

【方法概述 / Method】
DynamicGate-MLP定义连续的门控概率分布，在推理阶段将其转换为离散执行掩码以决定每个单元或模块是否参与计算。训练时引入计算预算约束，通过对期望激活门控比例的惩罚项实现可控的条件计算，并利用STE解决离散采样的不可导问题。

【实验结果 / Results】
该研究在MNIST、CIFAR-10、Tiny-ImageNet、Speech Commands和PBMC3k五个数据集上进行了评估，与多种MLP基线及MoE变体进行了对比。性能评估采用门控激活比例和层加权相对MAC指标来衡量计算效率，而非依赖硬件的后端内核执行时间。

【应用价值 / Applications】
DynamicGate-MLP适用于需要动态计算资源分配的场景，如边缘设备上的实时推理、多任务学习中的自适应计算，以及大规模模型的效率优化。该方法通过输入依赖的门控机制实现"功能可塑性"，使模型能够根据输入复杂度灵活调整计算量，在保持准确性的同时降低平均推理成本。
