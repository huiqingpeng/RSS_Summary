---
title: "CBF-RL: Safety Filtering Reinforcement Learning in Training with Control Barrier Functions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.14959"
published: "2026-03-19"
summarized: "2026-03-19T14:17:33.163732"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了CBF-RL框架，通过在训练阶段引入控制屏障函数（CBF）来解决强化学习中安全性与性能之间的权衡问题。该框架通过最小化修改名义RL策略以编码安全约束，并在训练过程中对策略 rollout 进行安全过滤，使学习到的策略能够内化安全约束。理论证明连续时间安全滤波器可通过闭式表达式部署于离散时间 rollout，实验验证了该方法在导航任务和Unitree G1人形机器人上实现了无需在线安全滤波器的安全部署。

【方法概述 / Method】

CBF-RL采用双关键设计：（1）在策略优化目标中加入CBF项，以最小侵入方式修正名义RL策略；（2）在训练 rollout 阶段实施安全过滤，将连续时间CBF安全滤波器转化为离散时间闭式表达式进行部署。该方法使安全约束在训练过程中被策略主动学习，而非仅依赖在线修正。

【实验结果 / Results】

消融实验表明CBF-RL实现了更安全的探索、更快的收敛速度和不确定性下的鲁棒性能。在Unitree G1人形机器人上的真实世界验证显示，该方法使机器人能够在无运行时安全滤波器的情况下安全避障和爬楼梯，同时学习到的策略倾向于选择更安全的奖励。

【应用价值 / Applications】

CBF-RL适用于高风险的机器人控制场景，如人形机器人运动控制、自主导航等需要严格安全保证的物理系统。该框架消除了对计算昂贵的在线安全滤波器的依赖，使安全强化学习策略能够直接部署于资源受限的嵌入式系统，为安全关键型机器人的大规模实际应用提供了可行路径。
