---
title: "Collaborative Temporal Feature Generation via Critic-Free Reinforcement Learning for Cross-User Sensor-Based Activity Recognition"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16043"
published: "2026-03-18"
summarized: "2026-03-18T15:39:50.956368"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对基于可穿戴惯性传感器的人类活动识别（HAR）中跨用户泛化难题，提出了一种新的域泛化范式——将可泛化特征提取建模为强化学习驱动的协作序列生成过程。作者设计了CTFG框架，采用基于Transformer的自回归生成器逐步构建特征序列，并通过无critic的Group-Relative Policy Optimization算法进行优化。该框架在DSADS和PAMAP2数据集上取得了最先进的跨用户识别准确率（88.53%和75.22%），显著降低了训练方差并加速了收敛。

【方法概述 / Method】

CTFG框架核心包含：基于Transformer的自回归生成器，以编码后的传感器输入为条件逐步生成特征token序列；采用Group-Relative Policy Optimization（GRPO）这一无critic强化学习算法，通过组内归一化而非学习价值估计来推导优势信号；设计三目标奖励函数，联合优化类判别性、跨用户不变性和时间保真度，以分离活动类别、对齐用户分布并保留细粒度时序信息。

【实验结果 / Results】

在DSADS和PAMAP2两个基准数据集上，CTFG分别达到88.53%和75.22%的跨用户准确率，创下当前最优水平；相比现有方法，该框架显著降低了任务间训练方差，实现了更快的收敛速度，并在不同动作空间维度变化下展现出稳健的泛化能力。

【应用价值 / Applications】

该研究可直接应用于健康监测、健身分析和情境感知计算等依赖可穿戴传感器的实际场景，解决模型在新用户身上部署时因生理特征、运动习惯和传感器佩戴位置差异导致的性能下降问题；其无critic的强化学习优化机制为其他存在分布漂移的时序建模任务提供了可迁移的技术方案。
