---
title: "Shuffling the Stochastic Mirror Descent via Dual Lipschitz Continuity and Kernel Conditioning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16042"
published: "2026-03-18"
summarized: "2026-03-18T16:09:52.509803"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对非Lipschitz光滑优化问题，提出了一种新的正则性条件——对偶核条件（Dual Kernel Conditioning, DKC），用以刻画核函数的局部相对曲率。结合相对光滑性框架，DKC保证了梯度映射在对偶空间中的Lipschitz连续性，即使其在原始空间中不满足该性质。基于这一工具，作者首次建立了随机重排镜像下降法（random reshuffling mirror descent）在约束非凸相对光滑问题上的复杂度界和迭代收敛性。

【方法概述 / Method】

论文引入对偶核条件（DKC）作为核心分析工具，该条件通过限制Bregman散度下的局部相对曲率，使得梯度映射在由镜像映射诱导的对偶空间中保持Lipschitz连续。作者验证了DKC对常用核函数（如熵核、Fermi-Dirac核等）的普适性，并证明其在仿射复合和锥组合运算下的封闭性，从而将分析框架扩展至更广泛的函数类。

【实验结果 / Results】

理论分析表明，在满足相对光滑性和DKC的条件下，随机重排镜像下降法在约束非凸优化问题中可获得收敛保证。具体而言，论文建立了该算法首次迭代的收敛性结果以及相应的复杂度上界，填补了此前仅适用于标准Lipschitz光滑情形的理论空白。DKC条件被证实与多种实际核函数兼容，包括熵正则化、逻辑损失等机器学习常用设置。

【应用价值 / Applications】

该研究为大规模机器学习优化算法（如动量方法、随机重排和方差缩减技术）在非Lipschitz光滑设置下的理论分析提供了新工具，特别适用于熵正则化优化、矩阵补全、泊松逆问题等领域。DKC框架的灵活性使其可扩展至复合目标函数和分布式优化场景，为设计更高效稳健的镜像下降变体算法奠定了理论基础。
