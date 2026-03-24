---
title: "Model Evolution Under Zeroth-Order Optimization: A Neural Tangent Kernel Perspective"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.21169"
published: "2026-03-24"
summarized: "2026-03-25T07:19:35.692472"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文从神经正切核（Neural Tangent Kernel, NTK）理论视角研究零阶优化（Zeroth-Order, ZO）下的模型演化动态。作者提出神经零阶核（Neural Zeroth-order Kernel, NZK）来描述函数空间中ZO更新的模型演化，并证明对于线性模型，期望NZK在训练过程中保持恒定，且显式依赖于随机扰动方向的一阶和二阶矩。该不变性导出了平方损失下模型演化的闭式表达式，为加速ZO收敛提供了新视角。

【方法概述 / Method】

论文核心方法是引入NZK核函数来刻画ZO优化在函数空间中的训练动态，将ZO更新解释为基于NZK的核梯度下降。对于线性模型和线性化神经网络，作者利用随机扰动矩的分析建立理论框架，并通过将ZO更新重新诠释为核梯度下降来理解其收敛行为。

【实验结果 / Results】

实验在合成数据集及MNIST、CIFAR-10、Tiny ImageNet等真实数据集上验证了理论结果的正确性。关键发现表明，使用单一共享随机向量（single shared random vector）能够显著加速ZO优化的收敛速度，为实际应用提供了有效的加速策略。

【应用价值 / Applications】

该研究为内存受限场景下的神经网络训练提供了理论指导，ZO优化因仅需前向传播而无需反向传播，特别适用于边缘设备和大模型微调等内存敏感场景。NZK框架的提出有助于设计更高效的ZO优化算法，而共享随机向量的加速策略可直接提升现有ZO方法的实用性和训练效率。
