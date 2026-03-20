---
title: "A Theoretical Comparison of No-U-Turn Sampler Variants: Necessary and Su?cient Convergence Conditions and Mixing Time Analysis under Gaussian Targets"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18640"
published: "2026-03-20"
summarized: "2026-03-20T13:15:38.981564"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文首次对No-U-Turn Sampler（NUTS）的两种主要变体——NUTS-mul（多项式采样）和NUTS-BPS（有偏渐进采样）进行了系统的理论比较研究。作者推导出了两种变体几何遍历性的首个必要条件，并建立了NUTS-mul几何遍历性和遍历性的首个充分条件，同时获得了NUTS-BPS在标准高斯分布上的首个混合时间结果。研究发现两种变体在定性行为上几乎相同（几何遍历性均依赖于目标分布的尾部性质），但在定量收敛速率上存在差异：两者混合时间均按$O(d^{1/4})$缩放，但NUTS-BPS的常数因子严格更小。

【方法概述 / Method】

本文采用严格的概率论和马尔可夫链理论分析方法，通过建立漂移条件和矩条件来研究NUTS变体的收敛性质。针对高斯目标分布，作者利用哈密顿动力学和泊松核的显式表达式，对两种采样策略的转移核进行精细分析，从而推导混合时间的显式上界。

【实验结果 / Results】

理论分析表明，在典型集初始化条件下，NUTS-mul和NUTS-BPS的混合时间均随维度$d$按$O(d^{1/4})$缩放（至多相差对数因子）。关键差异在于：NUTS-BPS的混合时间常数严格小于NUTS-mul，表明其在高维情况下具有更快的实际收敛速度。此外，几何遍历性的必要和充分条件揭示了目标分布尾部衰减速度对算法收敛的决定性作用。

【应用价值 / Applications】

该研究为贝叶斯计算软件库（如Stan、PyMC）中默认采样器的选择提供了重要理论指导，帮助实践者在NUTS-mul和NUTS-BPS之间做出基于收敛速度考量的明智决策。对于高维贝叶斯推断问题（如复杂分层模型、神经网络的贝叶斯训练），这些理论结果为算法调优和计算资源预估提供了可量化的理论依据。
