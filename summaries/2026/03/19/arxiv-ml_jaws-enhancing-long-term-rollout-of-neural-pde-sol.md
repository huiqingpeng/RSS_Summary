---
title: "JAWS: Enhancing Long-term Rollout of Neural PDE Solvers via Spatially-Adaptive Jacobian Regularization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.05538"
published: "2026-03-19"
summarized: "2026-03-19T14:13:17.473642"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种名为JAWS（Jacobian-Adaptive Weighting for Stability）的新方法，用于提升神经偏微分方程（PDE）求解器在长期 rollout 中的稳定性。该方法将算子学习重新表述为带有空间异方差不确定性的最大后验估计问题，使正则化强度能够根据局部物理复杂度自适应调整。实验表明，JAWS 可作为轨迹优化的有效谱预处理器，使短视界、内存高效的训练达到与长视界基线相当的精度，并在1D粘性Burgers方程和2D圆柱绕流（Re=400分布外泛化）验证中展现出长期稳定性、物理守恒性和计算效率的优势。

【方法概述 / Method】

JAWS 通过空间自适应雅可比正则化来实现动态稳定性控制：在平滑区域强制执行收缩动力学以抑制噪声，同时在激波等奇异特征附近放松约束以保留梯度信息。该方法将神经算子训练视为MAP估计问题，引入空间变化的方差参数来建模局部不确定性，从而避免全局正则化导致的过度平滑问题。

【实验结果 / Results】

在1D粘性Burgers方程和2D圆柱绕流（Re=400，分布外泛化）上的验证表明，JAWS显著提升了长期稳定性并保持了物理守恒特性。该方法使短视界训练能够达到与长视界基线相当的精度，同时大幅降低内存消耗，实现了计算效率与精度的有效平衡。

【应用价值 / Applications】

JAWS 特别适用于实际工程应用中的大规模流场长期稳定高效模拟，如计算流体力学中的湍流模拟和多尺度物理问题。其显著的内存使用 reduction 使得在资源受限环境下进行高精度、长时程的神经网络代理模型训练成为可能，为工业级数字孪生和实时仿真系统提供了可行技术路径。
