---
title: "Total Variation Guarantees for Sampling with Stochastic Localization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29555"
published: "2026-04-01"
summarized: "2026-04-02T07:19:11.242791"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对基于随机局部化（Stochastic Localization）的采样算法SLIPS，首次建立了全变差（Total Variation）距离下的严格收敛保证。在目标分布的最小假设条件下，作者证明达到ε-精度所需的迭代步数随维度线性增长（至多对数因子）。该分析借鉴了分数生成模型的理论技术，并为SLIPS中离散化点的经验最优选择提供了理论解释。

【方法概述 / Method】

论文采用随机局部化框架，通过逐步揭示目标分布的信息来构建采样过程；核心分析技术移植自分数生成模型的理论工具，包括得分估计误差控制和离散化误差分析。作者通过精心设计的时间离散化方案，将连续时间随机局部化过程转化为可实现的算法，并建立其与目标分布的全变差距离上界。

【实验结果 / Results】

理论结果表明，SLIPS算法的计算复杂度为O(d · polylog(d/ε))，其中d为维度，ε为目标精度；该线性维度依赖优于许多传统MCMC方法在恶劣条件下的指数依赖。分析同时揭示了离散化点数量与分布特性（如对数Sobolev常数）的定量关系，为实际调参提供了指导。

【应用价值 / Applications】

该研究为SLIPS算法在贝叶斯推断、统计物理模拟和生成建模等领域的可靠应用奠定了理论基础；全变差保证相比Wasserstein距离更适合概率质量分布的精确匹配任务。理论洞察可帮助实践者优化离散化方案，在高维复杂分布采样问题中提升计算效率。
