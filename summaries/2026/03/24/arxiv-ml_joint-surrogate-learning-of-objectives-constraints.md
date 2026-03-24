---
title: "Joint Surrogate Learning of Objectives, Constraints, and Sensitivities for Efficient Multi-objective Optimization of Neural Dynamical Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20984"
published: "2026-03-24"
summarized: "2026-03-25T07:17:10.093396"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了DMOSOPT，一种可扩展的多目标优化框架，用于解决生物物理神经系统模拟中的高维参数优化问题。该框架通过统一联合学习的替代模型（surrogate model）同时捕捉目标函数、约束条件和参数敏感性之间的相互作用，为原本缺乏梯度信号的二元可行/不可行分区问题提供平滑近似。实验表明，该框架在超算规模下能够以显著更少的问题评估次数高效优化高度约束的神经动力学系统，且方法具有通用性，适用于科学和工程领域的约束多目标优化问题。

【方法概述 / Method】

DMOSOPT采用联合替代学习策略，构建一个统一的代理模型来同时学习目标函数、约束可行边界和参数敏感性。该替代模型提供统一梯度，同时引导搜索向更优目标值和更高约束满足度方向进行；其偏导数则产生逐参数敏感性估计，实现更有针对性的探索。该方法特别针对神经动力学系统中约束条件形成的二元可行/不可行分区缺乏梯度信号的核心难点。

【实验结果 / Results】

研究从单细胞动力学到群体水平网络活动的神经回路建模工作流多个增量阶段验证了框架的有效性。实验表明，DMOSOPT在超计算规模下实现了高度约束问题的高效优化，相比传统方法大幅减少了问题评估次数（具体数值未在摘要中给出，但强调"substantially fewer"）。

【应用价值 / Applications】

该框架主要应用于计算神经科学中生物物理神经系统的模拟优化，可处理从单神经元到大规模神经网络的复杂动力学模型。同时，方法具有普适性，可推广至科学和工程领域中存在复杂约束的多目标优化问题，尤其适用于计算昂贵、参数空间高维且约束条件严格的仿真优化场景。
