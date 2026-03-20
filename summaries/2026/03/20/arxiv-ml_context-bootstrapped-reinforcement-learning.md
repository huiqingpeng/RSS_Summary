---
title: "Context Bootstrapped Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18953"
published: "2026-03-20"
summarized: "2026-03-20T12:17:12.030674"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对可验证奖励强化学习（RLVR）中探索效率低下的问题，提出了一种名为上下文引导强化学习（CBRL）的新方法。CBRL通过在训练提示中随机前置少量示例演示，并采用从高概率逐渐退火至零的课程策略，强制策略从演示中内化解题模式而非依赖提示。该方法在两个模型家族的五个Reasoning Gym任务上验证有效，并在领域特定的Q编程语言上展示了实际应用价值。

【方法概述 / Method】
CBRL的核心机制是在RLVR训练过程中，以概率p将少量示例演示（few-shot demonstrations）前置到训练提示中，该概率遵循从高到零的课程退火策略。早期高概率注入演示以引导探索，后期逐步取消辅助迫使模型独立推理，从而将外部知识转化为内部化能力。

【实验结果 / Results】
实验表明CBRL在两个模型家族和五个Reasoning Gym任务上持续提升成功率，并显著改善探索效率；该方法具有算法无关性，可与不同RLVR算法兼容。在Q编程语言的实际应用中，CBRL成功帮助模型掌握了与主流语言规范差异显著的领域特定知识。

【应用价值 / Applications】
CBRL适用于需要获取新推理模式或领域特定知识的复杂任务，如专业编程语言学习、数学推理和科学计算等领域。该方法通过课程式引导机制降低了RLVR的训练门槛，为提升大语言模型在专业领域的自主推理能力提供了可扩展的解决方案。
