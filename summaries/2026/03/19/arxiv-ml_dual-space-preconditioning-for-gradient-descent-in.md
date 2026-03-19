---
title: "Dual Space Preconditioning for Gradient Descent in the Overparameterized Regime"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.10485"
published: "2026-03-19"
summarized: "2026-03-19T14:19:16.496959"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了双空间预条件梯度下降（Dual Space Preconditioned Gradient Descent）的收敛性质，该框架涵盖归一化梯度下降、梯度裁剪和Adam等优化器。作者证明了在过参数化线性模型设定下，预条件梯度下降的迭代总能收敛到满足插值条件XW∞=Y的点。此外，论文分析了该方法的隐式偏差：对于各向同性预条件器，收敛点与标准梯度下降的收敛点相同；对于一般预条件器，两者距离仅相差一个常数因子。

【方法概述 / Method】

论文采用基于Bregman散度的分析框架，引入了一种新颖的Bregman散度变体及其恒等式来证明收敛性。研究考虑的预条件器形式为∇K，其中K: ℝᵖ→ℝ是凸函数，具体包括归一化梯度下降、梯度裁剪和Adam等实例。分析设定为过参数化线性模型，损失函数为ℓ(XW−Y)的形式。

【实验结果 / Results】

理论结果表明：预条件梯度下降总能收敛到满足XW∞=Y的插值解；对于各向同性预条件器K(G)=h(‖G‖_F)，收敛点W∞在满足约束XW∞=Y的条件下最小化‖W∞−W0‖_F²，即与标准梯度下降收敛到同一点；对于一般预条件器，有‖W0−W∞‖_F ≤ c‖W0−W_GD,∞‖_F。实证研究发现，对于一般K(·)，W∞依赖于学习率选择，难以精确刻画隐式偏差。

【应用价值 / Applications】

该研究为理解现代深度学习优化器（如Adam、梯度裁剪）在过参数化场景下的行为提供了理论保证，有助于指导优化器的选择和超参数调优。结果说明各向同性预条件器不会改变梯度下降的隐式偏差特性，为设计具有特定泛化性质的优化算法提供了理论基础，对神经网络训练的理论理解和实践应用均有重要意义。
