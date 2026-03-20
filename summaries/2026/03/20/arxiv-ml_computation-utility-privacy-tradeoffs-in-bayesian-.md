---
title: "Computation-Utility-Privacy Tradeoffs in Bayesian Estimation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18254"
published: "2026-03-20"
summarized: "2026-03-20T13:11:04.397192"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了差分隐私贝叶斯估计中的计算-效用-隐私权衡问题。针对高斯均值估计和线性回归这两个典型任务，作者首次提出了高效的算法，使其均方误差达到$(1+o(1))\mathrm{OPT}$的贝叶斯最优水平。研究还发现了有趣的计算-统计间隙：在低阶框架下，所提方法的超额风险在所有高效算法中是最优的，但仍劣于指数时间算法所能达到的性能。

【方法概述 / Method】
论文采用隐私到鲁棒性的框架（privacy-to-robustness framework），但创新性地设计了基于平方和（sum-of-squares）的鲁棒估计器，用于处理本质上非鲁棒的对象（如经验均值和OLS估计器）。作者还引入了一种基于短平分解（short-flat decompositions）的新型约束条件，扩展了平方和工具集。

【实验结果 / Results】
对于贝叶斯均值估计和线性回归任务，所提算法均实现了$(1+o(1))\mathrm{OPT}$的均方误差，接近贝叶斯最优误差。理论分析证明，这些任务存在计算-统计间隙：高效算法无法达到指数时间算法的超额风险下界，且该下界在低阶多项式框架下是紧的。

【应用价值 / Applications】
该研究为数据受限且需要隐私保护的场景（如医疗数据分析、金融建模和社会科学研究）提供了理论基础。所开发的高效隐私保护贝叶斯估计方法，可在保证严格隐私的同时实现接近最优的统计效用，适用于需要不确定性量化的高风险决策应用。
