---
title: "Best-of-Both-Worlds Multi-Dueling Bandits: Unified Algorithms for Stochastic and Adversarial Preferences under Condorcet and Borda Objectives"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18972"
published: "2026-03-20"
summarized: "2026-03-20T12:17:50.762900"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文首次为多臂决斗赌博机（multi-dueling bandits）问题提出了"两全其美"（best-of-both-worlds）算法，能够在随机和对抗性偏好环境下同时达到最优性能，且无需预先知道环境类型。针对Condorcet目标，作者提出的MetaDueling算法通过黑盒归约将多路比较反馈转化为无偏成对信号，结合Versatile-DB实现了$O(\sqrt{KT})$的对抗遗憾界和实例最优的$O(\sum_{i \neq a^\star} \frac{\log T}{\Delta_i})$随机遗憾界。针对Borda目标，提出的算法在随机环境下达到$O(\sum_{i: \Delta_i^{\mathrm{B}} > 0} \frac{K\log KT}{(\Delta_i^{\mathrm{B}})^2})$遗憾，在对抗环境下达到$O(K\sqrt{T\log KT})$遗憾。

【方法概述 / Method】

核心方法是**MetaDueling黑盒归约框架**：通过随机采样将每轮$m \geq 2$个臂的多路胜者反馈转化为成对比较的无偏估计，从而将任意决斗赌博机算法扩展为多决斗设置。对于Condorcet目标，该归约与Versatile-DB结合，利用其自调整学习率机制同时适应两种环境；对于Borda目标，设计了专门的探索-利用平衡策略，通过维护Borda分数的置信区间来同时处理随机和对抗性偏好。

【实验结果 / Results】

理论分析证明了所提算法的紧确性：Condorcet设置下，上界与匹配的下界一致，证实了实例最优性；Borda设置下，上界与已知下界相差至多$K$倍，达到了文献中最优结果。具体而言，MetaDueling在随机环境下消除了对问题相关常数的依赖，在对抗环境下达到了极小极大最优的$\sqrt{T}$速率；Borda算法在两种环境下均实现了次线性遗憾，且无需环境类型作为先验知识。

【应用价值 / Applications】

该研究直接适用于**在线排序和推荐系统**，如搜索引擎结果优化、产品推荐、众包标注等场景，其中系统需要同时从多个选项中识别最优项且仅能获得相对偏好反馈。算法的环境自适应特性使其在实际部署中更具鲁棒性——无需人工判断用户偏好是稳定随机还是可能突变的对抗性，即可保证理论最优性能，降低了系统调参成本并提升了可靠性。
