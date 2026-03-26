---
title: "Linear-Nonlinear Fusion Neural Operator for Partial Differential Equations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24143"
published: "2026-03-26"
summarized: "2026-03-27T07:21:32.358643"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种新颖的神经网络算子架构——线性-非线性融合神经算子（LNF-NO），通过显式解耦算子映射中的线性与非线性效应，实现了轻量化和可解释的表示。该架构采用线性与非线性组件的乘积融合方式，能够在算子层面高效捕捉复杂解特征，同时保持稳定性和泛化能力。在多个偏微分方程算子学习基准测试中，LNF-NO 的训练速度显著快于 DeepONet 和 FNO，且在大多数情况下达到相当或更优的精度，在三维 Poisson-Boltzmann 案例中训练速度提升约 2.7 倍并获得最佳精度。

【方法概述 / Method】

LNF-NO 的核心创新在于将神经算子分解为线性组件和非线性组件的乘积融合形式，其中线性组件负责捕捉解的全局趋势和光滑结构，非线性组件则建模局部复杂特征和高频变化。该架构天然支持多函数输入，并适用于规则网格和不规则几何，通过显式解耦降低了模型学习难度，提升了参数效率。

【实验结果 / Results】

实验涵盖了非线性 Poisson-Boltzmann 方程和多物理耦合系统等多样化 PDE 基准测试，结果表明 LNF-NO 在训练效率上显著优于 DeepONet 和 FNO。在三维 Poisson-Boltzmann 案例中，LNF-NO 不仅取得了对比模型中的最高精度，训练速度相比三维 FNO 基线提升了约 2.7 倍，展现出优异的计算效率与精度权衡。

【应用价值 / Applications】

LNF-NO 可广泛应用于需要快速推理的科学与工程场景，如分子生物物理学中的静电势计算、多物理场耦合仿真以及实时预测需求高的数字孪生系统。其轻量化特性和对不规则几何的兼容性使其特别适合嵌入资源受限的下游应用，为替代传统数值求解器提供了高效可行的机器学习方案。
