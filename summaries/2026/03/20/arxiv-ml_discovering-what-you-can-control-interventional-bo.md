---
title: "Discovering What You Can Control: Interventional Boundary Discovery for Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18257"
published: "2026-03-20"
summarized: "2026-03-20T12:09:29.265932"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对强化学习中存在混杂干扰变量时的状态维度选择问题，提出了一种因果识别方法。作者将问题形式化为发现智能体的"因果影响范围"（Causal Sphere of Influence），并提出了干预边界发现（Interventional Boundary Discovery, IBD）方法。IBD 利用 Pearl 的 do-算子对智能体自身动作进行干预，并通过双样本检验生成可解释的状态维度二值掩码。该方法无需学习模型，可作为预处理步骤与任何下游 RL 算法结合使用。

【方法概述 / Method】
IBD 的核心思想是通过主动干预（do-operator）来区分"动作导致的状态变化"与"仅与动作相关的干扰变量"。具体而言，该方法对动作分布进行干预，比较干预前后的状态分布变化，使用双样本统计检验来识别哪些状态维度真正受到动作因果影响，最终输出一个二值掩码用于筛选相关状态特征。

【实验结果 / Results】
实验在 12 个连续控制环境中进行，干扰变量维度最高达 100 维。研究发现：（1）基于观察的特征选择方法会主动选择混杂干扰变量并丢弃真正的因果维度；（2）当干扰变量与相关特征比例约为 3:1 时，全状态 RL 性能急剧下降；（3）IBD 在所有干扰水平下均接近 Oracle 性能，且增益可迁移至 SAC 和 TD3 等不同算法。

【应用价值 / Applications】
IBD 可广泛应用于存在大量传感器数据但仅有部分与任务因果相关的强化学习场景，如机器人控制（视觉干扰、本体感觉噪声）、自动驾驶（无关环境物体）和医疗决策（混杂患者特征）。该方法提升了 RL 系统在复杂环境中的样本效率和鲁棒性，同时增强了模型的可解释性。
