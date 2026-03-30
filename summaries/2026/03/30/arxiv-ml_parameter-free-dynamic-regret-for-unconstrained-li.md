---
title: "Parameter-Free Dynamic Regret for Unconstrained Linear Bandits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25916"
published: "2026-03-30"
summarized: "2026-03-31T07:19:41.275201"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了无约束对抗性线性赌博机中的动态遗憾最小化问题。作者提出了一种简单的方法，能够组合多个赌博机算法的保证，从而最优地适应任意比较器序列的切换次数 $S_T$。该研究首次实现了无需预先知道 $S_T$ 的情况下，达到 $\mathcal{O}\big(\sqrt{d(1+S_T) T}\big)$ 量级的最优遗憾保证（至多相差多对数因子），解决了一个长期存在的开放性问题。

【方法概述 / Method】

作者提出了一种算法组合框架，通过巧妙地整合多个具有不同参数设置的赌博机算法，实现对未知切换次数 $S_T$ 的自适应。该方法采用"专家聚合"（experts aggregation）或类似的多臂赌博机技术，动态地选择或加权不同算法，从而在不依赖 $S_T$ 先验知识的情况下获得最优保证。

【实验结果 / Results】

论文的主要理论结果是证明了所提算法达到了 $\tilde{\mathcal{O}}\big(\sqrt{d(1+S_T) T}\big)$ 的动态遗憾界，这与已知下界匹配，是最优的。该结果适用于任意比较器序列 $\boldsymbol{u}_1,\ldots,\boldsymbol{u}_T \in \mathbb{R}^d$，且仅需每轮的点评估反馈，无需对比较器序列的范数或变化进行任何先验假设。

【应用价值 / Applications】

该研究适用于需要在线决策且环境可能非平稳的场景，如在线广告竞价、推荐系统动态优化、网络路由和资源分配等。算法无需手动调参即可适应环境变化程度，大大降低了实际部署难度，为对抗性和非平稳环境下的自适应学习提供了理论基础。
