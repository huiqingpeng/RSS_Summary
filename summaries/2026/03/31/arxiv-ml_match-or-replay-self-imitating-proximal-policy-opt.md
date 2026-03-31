---
title: "Match or Replay: Self Imitating Proximal Policy Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27515"
published: "2026-03-31"
summarized: "2026-04-01T07:25:19.575816"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种自模仿近端策略优化（Self Imitating Proximal Policy Optimization）算法，旨在解决强化学习智能体在稀疏奖励环境中的低效探索问题。该方法通过利用过去高奖励的状态-动作对来指导策略更新，在密集奖励环境中使用最优传输距离匹配最有价值轨迹的状态访问分布，在稀疏奖励环境中则均匀重放成功的自遇轨迹。实验表明，该方法在MuJoCo、Animal-AI Olympics和PointMaze等多种环境中实现了更快的收敛速度和更高的成功率，显著优于现有自模仿强化学习基线方法。

【方法概述 / Method】
本研究提出了一种混合的自模仿策略优化框架，根据奖励密度动态选择两种机制：在密集奖励环境中，采用基于最优传输（Optimal Transport）距离的分布匹配策略，使当前策略的状态访问分布与高奖励轨迹对齐；在稀疏奖励环境中，则采用均匀重放（uniform replay）机制，直接复用智能体自身历史成功轨迹以促进结构化探索。该方法与近端策略优化（PPO）相结合，形成统一的on-policy自模仿学习算法。

【实验结果 / Results】
实验在多样化环境中验证了方法的有效性：在密集奖励的MuJoCo连续控制任务中，基于最优传输的分布匹配显著提升了样本效率；在稀疏奖励的部分可观测3D Animal-AI Olympics和多目标PointMaze任务中，均匀重放机制大幅提高了成功率和收敛速度。结果表明，该混合方法在所有测试环境中均超越了现有的自模仿强化学习基线，展现出更强的探索能力和学习稳定性。

【应用价值 / Applications】
该研究为强化学习在复杂真实场景中的应用提供了更高效的探索策略，特别适用于机器人控制（如MuJoCo模拟的物理交互）、自主导航（如部分可观测3D环境）和多目标决策任务（如迷宫导航）。通过提升稀疏奖励环境下的样本效率，该方法可降低真实世界强化学习的训练成本，为自动驾驶、机器人操作和智能游戏AI等领域的实际部署提供了可行的技术路径。
