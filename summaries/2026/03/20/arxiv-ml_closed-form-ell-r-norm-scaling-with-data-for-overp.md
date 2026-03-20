---
title: "Closed-form $\ell_r$ norm scaling with data for overparameterized linear regression and diagonal linear networks under $\ell_p$ bias"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.21181"
published: "2026-03-20"
summarized: "2026-03-20T14:07:41.700710"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对过参数化线性回归中$\ell_p$最小范数插值器（$p\in(1,2]$）的$\ell_r$范数族$\{\|\widehat{w_p}\|_r\}_{r\in[1,p]}$的标度行为，给出了统一的高概率刻画。通过双射线分析，作者发现了一个由信号"尖峰"与$X^\top Y$中零坐标"主体"之间的竞争机制，从而推导出数据依赖的转折点$n_\star$（"肘部"）和普适阈值$r_\star=2(p-1)$的闭式预测，该阈值区分了随样本量$n$增长而饱和或持续增长的范数。研究还将这一理论框架延伸至对角线性网络，建立了显式偏差与隐式偏差之间的预测桥梁。

【方法概述 / Method】

核心方法是"双射线分析"（dual-ray analysis），通过分解$X^\top Y$中的信号分量与零坐标分量来刻画参数范数的渐近行为。对于对角线性网络，作者通过初始化尺度$\alpha$校准到有效$p_{\mathrm{eff}}(\alpha)$，利用DLN的可分离势函数建立与$\ell_p$插值器的对应关系。

【实验结果 / Results】

理论预测得到了高概率保证：当$r < r_\star = 2(p-1)$时，$\|\widehat{w_p}\|_r$随$n$增长而饱和；当$r > r_\star$时，范数以显式指数律持续增长；转折点$n_\star$具有数据依赖性。对角线性网络的实验验证了DLN确实继承相同的肘部/阈值规律，证实了理论框架的预测能力。

【应用价值 / Applications】

该研究为理解过参数化模型的隐式正则化提供了精细的理论工具，特别适用于分析神经网络训练中不同范数作为泛化代理指标（generalization proxies）的可靠性。结果表明，泛化预测能力对所选$\ell_r$范数高度敏感，为算法设计和模型选择提供了重要指导。
