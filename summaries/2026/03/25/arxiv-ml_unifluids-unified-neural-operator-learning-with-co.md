---
title: "UniFluids: Unified Neural Operator Learning with Conditional Flow-matching"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22309"
published: "2026-03-25"
summarized: "2026-03-26T07:09:45.703197"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了UniFluids，一种基于条件流匹配的神经算子学习框架，首次利用扩散Transformer的可扩展性实现跨不同维度和物理变量的PDE解算子的统一学习。与自回归PDE基础模型不同，UniFluids采用流匹配实现并行序列生成。通过引入统一四维时空表示和x-预测策略，该方法在多个1D/2D/3D PDE数据集上展现出强预测精度、良好可扩展性和跨场景泛化能力。

【方法概述 / Method】
UniFluids核心采用条件流匹配（conditional flow-matching）结合扩散Transformer架构，替代传统的自回归生成方式以实现并行化序列生成。方法关键设计包括：统一的四维时空表示用于异构PDE数据集的联合训练与条件编码，以及基于数据集有效维度远低于patch维度的发现而采用的x-预测（而非噪声预测）策略。

【实验结果 / Results】
论文在涵盖1D、2D和3D空间维度的多个PDE数据集上进行了大规模评估，实验表明UniFluids具有强大的预测准确性。该方法展现出良好的可扩展性（scalability）和跨场景泛化能力（cross-scenario generalization），验证了统一神经算子学习框架在实际PDE求解中的有效性。

【应用价值 / Applications】
UniFluids可广泛应用于科学研究和工程领域的PDE数值模拟，如流体力学、气象预测、材料科学等需要求解多变维度物理方程的场景。其统一框架能够减少为不同PDE单独训练模型的成本，并行生成特性也提升了推理效率，为构建通用PDE基础模型提供了新路径。
