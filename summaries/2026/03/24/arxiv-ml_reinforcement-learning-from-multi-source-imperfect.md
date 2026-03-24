---
title: "Reinforcement Learning from Multi-Source Imperfect Preferences: Best-of-Both-Regimes Regret"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20453"
published: "2026-03-24"
summarized: "2026-03-25T07:10:09.321720"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了多源不完美偏好下的强化学习问题，突破了传统RLHF理论假设单一真实目标函数的局限。作者提出了一个累积不完美预算框架，为每个反馈源定义其与理想预言机的总偏差上限ω。他们设计了一种统一算法，实现了$\tilde{O}(\sqrt{K/M}+\omega)$的遗憾界，展现出"双机制最优"特性：当不完美程度较小时获得$M$（源数量）相关的统计增益，当不完美较大时保持对ω的鲁棒加性依赖。研究还建立了匹配的下界$\tilde{\Omega}(\max\{\sqrt{K/M},\omega\})$，并证明朴素处理不完美反馈可能导致$\tilde{\Omega}(\min\{\omega\sqrt{K},K\})$的线性遗憾。

【方法概述 / Method】

论文核心技术包括三项创新：不完美自适应加权比较学习，根据各源可靠性动态调整权重；值目标转移估计，控制隐藏反馈引起的分布偏移；以及子重要性采样，保证加权目标的可分析性。这些方法协同作用，使算法能够同时利用多源信息并量化累积不完美带来的根本限制。

【实验结果 / Results】

理论分析表明，所提算法在$K$个回合后达到$\tilde{O}(\sqrt{K/M}+\omega)$的遗憾上界，与下界$\tilde{\Omega}(\max\{\sqrt{K/M},\omega\})$匹配，证明了其最优性。关键对比显示，若将不完美反馈直接视为预言机一致，可能产生高达$\tilde{\Omega}(\min\{\omega\sqrt{K},K\})$的灾难性遗憾，凸显了算法设计的必要性。

【应用价值 / Applications】

该研究对实际RLHF系统具有直接指导意义，如大语言模型对齐中常见的多标注者、专家反馈、奖励模型与启发式规则的混合使用场景。理论框架为系统设计提供了原则性指导：明确量化何时多源反馈能提升性能（ω较小时），以及不完美累积如何设定性能上限，助力构建更可靠的人机协作智能系统。
