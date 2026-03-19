---
title: "GIFT: Reconciling Post-Training Objectives via Finite-Temperature Gibbs Initialization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.09233"
published: "2026-03-19"
summarized: "2026-03-19T14:11:26.405629"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对大型推理模型（LRMs）后训练范式中监督微调（SFT）与强化学习（RL）之间的优化不匹配问题，提出了一种名为GIFT（有限温度Gibbs初始化）的新方法。标准SFT被视为抑制基础先验的零温度极限，导致分布坍缩并耗尽RL所需的探索空间；而GIFT将监督信号作为有限温度能量势引入，建立了促进后训练阶段目标一致性的分布桥梁。实验表明，GIFT作为RL初始化显著优于标准SFT及其他竞争基线，为保留探索能力并对齐两个后训练阶段提供了数学上严谨的途径。

【方法概述 / Method】

GIFT通过能量建模视角重新形式化SFT，将标准SFT的硬性监督转化为有限温度下的Gibbs分布采样。具体而言，该方法将监督信号编码为能量函数中的势能项，通过调节温度参数控制分布的熵水平，从而在保持监督信号的同时保留基础模型的先验分布特性，避免分布坍缩。

【实验结果 / Results】

GIFT在作为RL初始化时显著优于标准SFT方法，有效提升了后续强化学习阶段的探索效率和最终性能。相比其他竞争性基线方法，GIFT在保持目标一致性的同时，成功缓解了SFT与RL之间的优化冲突，为大型推理模型的后训练提供了更优的初始化方案。

【应用价值 / Applications】

该研究可直接应用于大型推理模型（如DeepSeek-R1、OpenAI o1等）的后训练流程优化，提升SFT到RL阶段的知识迁移效率。GIFT为工业界构建高性能推理模型提供了理论指导，特别是在需要复杂推理能力的数学、编程和科学问答等任务场景中，有望降低训练成本并提高模型可靠性。
