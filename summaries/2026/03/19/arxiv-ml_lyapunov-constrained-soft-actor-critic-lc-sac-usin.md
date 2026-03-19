---
title: "Lyapunov Constrained Soft Actor-Critic (LC-SAC) using Koopman Operator Theory for Quadrotor Trajectory Tracking"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.04132"
published: "2026-03-19"
summarized: "2026-03-19T14:18:26.496366"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种基于Koopman算子理论的Lyapunov约束软演员-评论家算法（LC-SAC），用于解决强化学习在安全关键物理系统中缺乏稳定性保证的问题。该研究利用扩展动态模态分解（EDMD）方法对非线性系统进行线性近似，并据此推导出候选Lyapunov函数的闭式解，将其整合到SAC算法中以提供策略稳定性保证。在基于safe-control-gym的二维四旋翼轨迹跟踪环境中，所提算法实现了训练收敛，且Lyapunov稳定性准则的违反程度随训练衰减，优于标准SAC基线算法。

【方法概述 / Method】

论文采用扩展动态模态分解（EDMD）技术构建系统动力学的线性Koopman算子近似，从而规避了传统方法中Lyapunov函数选择的难题。基于该线性近似，推导出可计算解析形式的候选Lyapunov函数，并将其作为约束条件嵌入SAC算法的策略优化过程中，在最大化累积奖励的同时确保闭环系统的稳定性。

【实验结果 / Results】

在二维四旋翼轨迹跟踪任务中，LC-SAC算法展现出稳定的训练收敛特性，且Lyapunov稳定性条件的违反量随训练进程逐步衰减。与无稳定性约束的标准SAC算法相比，所提方法有效抑制了策略引起的振荡和无界状态发散现象，验证了稳定性约束对策略安全性的提升作用。

【应用价值 / Applications】

该研究为无人机、自动驾驶汽车等安全关键系统的强化学习控制提供了理论保证，解决了传统RL算法在物理部署时的稳定性隐患。方法可扩展至其他需严格稳定性约束的机器人控制任务，为安全强化学习在真实世界的应用奠定了算法基础。
