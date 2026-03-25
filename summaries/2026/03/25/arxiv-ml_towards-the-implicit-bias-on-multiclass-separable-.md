---
title: "Towards The Implicit Bias on Multiclass Separable Data Under Norm Constraints"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22824"
published: "2026-03-25"
summarized: "2026-03-26T07:17:33.609579"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了基于梯度算法在多分类可分数据上的隐式偏差机制，提出了一种名为NucGD的几何感知优化器，通过核范数约束强制低秩结构。作者将NucGD与新兴的低秩投影方法建立联系，提供了统一视角，并推导出无需SVD的高效异步幂迭代更新规则。此外，论文还实证分析了随机优化动态（包括小批量采样和动量引入的梯度噪声）如何调节向期望最大间隔收敛的过程。

【方法概述 / Method】
论文基于归化最速下降（Normalized Steepest Descent, NSD）框架，设计了NucGD优化器，利用核范数几何特性诱导低秩解。为实现可扩展训练，作者通过异步幂迭代开发了免SVD的近似更新规则，避免了大矩阵分解的计算开销。

【实验结果 / Results】
论文实证研究了随机优化动态对隐式偏差的影响，揭示了小批量采样和动量所引入的梯度噪声水平如何调制收敛行为。实验表明，这些随机因素会影响优化轨迹向期望最大间隔解的收敛特性，为理解深度学习中的隐式正则化提供了新见解。

【应用价值 / Applications】
该研究为设计具有可控隐式偏差的优化算法提供了理论基础，特别适用于需要低秩解的过参数化模型训练场景，如神经网络压缩和高效表示学习。NucGD的免SVD特性使其能够扩展到大规模问题，对实际深度学习系统的优化器设计具有指导意义。
