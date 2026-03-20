---
title: "Hardness of High-Dimensional Linear Classification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19061"
published: "2026-03-20"
summarized: "2026-03-20T13:19:52.656230"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文建立了最大半空间差异（Maximum Halfspace Discrepancy）问题的新指数级下界，该问题是线性分类的核心理论模型。此前该问题仅已知多项式下界，与已知的 $O(n^d)$ 和 $\tilde O(1/\varepsilon^d)$ 上界存在显著差距。作者通过从仿射退化检测（Affine Degeneracy testing）和 $k$-Sum 问题的归约，首次在多项式对数因子范围内闭合了这一差距，证明了近乎匹配的指数级下界。

【方法概述 / Method】

本文采用计算复杂性理论中的归约技术，将广泛相信的困难问题（仿射退化检测和 $k$-Sum）归约到最大半空间差异问题。针对精确版本和近似版本分别构造归约，并特别考虑了仅允许侧面查询（sidedness queries）的计算模型，该模型对应于许多现代算法和计算范式中实际实现的设置。

【实验结果 / Results】

基于仿射退化检测的假设，证明了最大半空间差异问题的下界为 $\tilde\Omega(n^d)$（精确版本）和 $\tilde\Omega(1/\varepsilon^d)$（近似版本）；基于 $k$-Sum 假设，分别得到 $\tilde\Omega(n^{d/2})$ 和 $\tilde\Omega(1/\varepsilon^{d/2})$ 的下界。在侧面查询限制模型下，第一个下界无条件成立。

【应用价值 / Applications】

该研究为高维线性分类问题提供了严格的计算复杂性理论边界，对机器学习算法设计具有重要指导意义。结果暗示在高维空间中精确或高精度近似求解线性分类问题本质困难，为算法优化策略（如降维、随机化近似）的选择提供了理论依据，同时也验证了现有基于侧面查询的几何算法框架的局限性。
