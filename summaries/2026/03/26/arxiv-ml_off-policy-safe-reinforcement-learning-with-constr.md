---
title: "Off-Policy Safe Reinforcement Learning with Constrained Optimistic Exploration"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23889"
published: "2026-03-26"
summarized: "2026-03-27T07:18:35.409156"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对离策略安全强化学习中因成本无关探索与累积成本估计偏差导致的约束违反问题，提出了一种名为COX-Q（Constrained Optimistic eXploration Q-learning）的新算法。该算法通过成本约束的乐观探索策略解决奖励与成本在动作空间中的梯度冲突，并采用截断分位数critic稳定成本价值学习。实验表明，COX-Q在安全速度控制、安全导航和自动驾驶任务中实现了高样本效率、优异的测试安全性性能以及可控的数据收集成本。

【方法概述 / Method】
COX-Q采用成本约束的乐观探索策略，通过自适应调整信任区域来控制训练成本，同时解决奖励与成本的梯度冲突问题；此外，该方法引入截断分位数critic进行保守的离线分布价值学习，利用分位数critic量化认知不确定性以指导探索。

【实验结果 / Results】
在安全速度控制、安全导航和自动驾驶三类任务上的实验表明，COX-Q在保持高样本效率的同时，实现了具有竞争力的测试安全性能，并有效控制了数据收集阶段的成本约束违反。

【应用价值 / Applications】
该研究适用于自动驾驶、机器人控制等安全关键型应用场景，能够在保证探索效率的同时严格控制安全约束，为实际部署中需要兼顾性能与安全的决策系统提供了一种可靠的离策略强化学习解决方案。
