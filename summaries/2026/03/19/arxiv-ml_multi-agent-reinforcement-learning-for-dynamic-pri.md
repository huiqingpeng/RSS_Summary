---
title: "Multi-Agent Reinforcement Learning for Dynamic Pricing: Balancing Profitability,Stability and Fairness"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16888"
published: "2026-03-19"
summarized: "2026-03-19T12:05:11.156240"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本论文系统性地评估了多智能体强化学习（MARL）方法在竞争性零售市场动态定价中的应用，重点比较了MAPPO和MADDPG两种算法与独立DDPG（IDDPG）基线。研究发现MAPPO在平均收益和稳定性方面表现最优，而MADDPG虽利润略低但实现了最公平的利润分配。该研究表明MARL方法（特别是MAPPO）为动态零售定价提供了可扩展且稳定的替代方案。

【方法概述 / Method】

研究采用基于真实零售数据构建的模拟市场环境，对MAPPO（多智能体近端策略优化）、MADDPG（多智能体深度确定性策略梯度）和IDDPG三种算法进行基准测试。实验从收益表现、随机种子稳定性、公平性和训练效率四个维度进行综合评估。

【实验结果 / Results】

MAPPO在所有算法中 consistently 获得最高平均收益且方差最低，展现出优秀的稳定性和可复现性；MADDPG在利润指标上略逊一筹，但实现了智能体间最公平的利润分配；IDDPG作为独立学习基线表现不及两种中心化训练的多智能体方法。

【应用价值 / Applications】

该研究为零售商在竞争激烈的市场环境中制定动态定价策略提供了实用的算法选择依据，MAPPO的高稳定性和可扩展性使其特别适合大规模部署，而MADDPG的公平性优势则适用于注重合作生态健康的平台场景。研究成果有助于平衡企业盈利目标与市场稳定性、公平性之间的多目标优化。
