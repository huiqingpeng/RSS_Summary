---
title: "Self Paced Gaussian Contextual Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23755"
published: "2026-03-26"
summarized: "2026-03-27T07:16:50.359532"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了自步高斯课程学习（SPGL），一种用于上下文强化学习的新方法。该方法通过利用高斯上下文分布的闭式更新规则，避免了传统自步课程方法中计算昂贵的内循环优化问题。理论分析保证了算法的收敛性，实验表明SPGL在多个基准任务上匹配或超越了现有课程学习方法，尤其在隐藏上下文场景中表现更优，同时实现了更稳定的上下文分布收敛。

【方法概述 / Method】
SPGL将上下文分布约束为高斯分布，从而推导出上下文分布参数的闭式更新规则，无需迭代优化。该方法通过自步学习机制自适应地调整任务难度序列，在保持样本效率和适应性的同时显著降低计算开销。

【实验结果 / Results】
实验在Point Mass、Lunar Lander和Ball Catching等多个上下文RL基准环境上进行。结果表明SPGL在隐藏上下文场景中尤其优于现有方法，且上下文分布收敛更加稳定，计算效率大幅提升。

【应用价值 / Applications】
SPGL为高维和连续上下文空间中的课程生成提供了可扩展的解决方案，适用于机器人控制、自主导航等需要处理部分可观测性和复杂动态环境的实际任务，为大规模强化学习系统的训练效率提升提供了新途径。
