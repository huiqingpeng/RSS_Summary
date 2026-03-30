---
title: "A Lyapunov Analysis of Softmax Policy Gradient for Stochastic Bandits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26547"
published: "2026-03-30"
summarized: "2026-03-31T07:25:09.464694"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文将Lattimore (2026)关于连续时间k臂随机老虎机策略梯度分析的方法，成功推广到标准离散时间设定。研究证明了当学习率η = O(Δ²_min/(Δ_max log(n)))时，遗憾界(regret)为O(k log(k) log(n)/η)，其中n为时间范围，Δ_min和Δ_max分别表示最小和最大奖励间隙。该结果为离散时间softmax策略梯度算法提供了严格的理论保证。

【方法概述 / Method】
本研究采用Lyapunov函数分析方法，借鉴连续时间随机微分方程的稳定性理论，将其适配到离散时间随机优化框架。通过构造合适的能量函数，分析softmax参数化策略在离散时间更新下的收敛动态。

【实验结果 / Results】
论文建立了明确的遗憾上界：在适当选择学习率η的条件下，累积遗憾随时间范围n呈对数增长O(log(n))，且与臂数k的关系为O(k log(k))。学习率的选择依赖于问题相关的间隙参数Δ_min和Δ_max，实现了问题依赖的(instance-dependent)最优速率。

【应用价值 / Applications】
该理论结果为强化学习中的策略梯度方法在离散时间随机决策问题中的应用提供了严格基础，可指导在线推荐系统、临床试验设计、自适应路由等场景中的探索-利用权衡策略设计，并为学习率调参提供理论依据。
