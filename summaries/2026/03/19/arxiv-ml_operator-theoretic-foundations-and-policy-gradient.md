---
title: "Operator-Theoretic Foundations and Policy Gradient Methods for General MDPs with Unbounded Costs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17875"
published: "2026-03-19"
summarized: "2026-03-19T12:17:50.364557"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文将马尔可夫决策过程（MDP）重新诠释为在一般函数空间上线性算子的目标函数优化问题。利用成熟的线性算子摄动理论，该视角能够识别目标函数关于线性算子的导数，从而将强化学习中的许多经典结果推广到一般状态和动作空间的情形。此前此类结果仅限于有限状态-有限动作MDP或特定线性函数逼近设置。该框架还导出了适用于一般状态动作空间MDP的新型低复杂度PPO类强化学习算法。

【方法概述 / Method】
论文采用算子理论视角，将MDP建模为线性算子空间上的优化问题，并运用线性算子的摄动理论来推导目标函数的导数。这种方法避免了传统有限维假设的局限，适用于更一般的函数空间设置。

【实验结果 / Results】
（注：提供的摘要未包含具体实验结果，仅提及理论框架导出新型PPO类算法。）

【应用价值 / Applications】
该研究扩展了策略梯度方法的适用范围，使其能够处理具有无界代价的一般连续状态动作空间MDP，为复杂强化学习问题（如机器人控制、连续决策任务）提供了更坚实的理论基础和实用算法工具。
