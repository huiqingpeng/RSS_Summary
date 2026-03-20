---
title: "PowerFlow: Unlocking the Dual Nature of LLMs via Principled Distribution Matching"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18363"
published: "2026-03-20"
summarized: "2026-03-20T13:12:12.610815"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了PowerFlow框架，将无监督微调重新表述为分布匹配问题，通过将GFlowNet作为非归一化密度的摊销变分采样器，并设计长度感知的Trajectory-Balance目标来消除自回归生成中的结构长度偏差。该方法通过调控α-幂分布（α>1时锐化分布以增强逻辑推理，α<1时展平分布以激发创造性表达），实现了对LLM双重特性的定向引导，实验表明其性能持续优于现有RLIF方法，甚至达到或超过监督式GRPO水平，同时在创意任务中同时提升多样性与质量。

【方法概述 / Method】

PowerFlow核心在于将GFlowNet重新诠释为摊销变分采样器，用于学习非归一化密度函数的采样分布；针对自回归生成的固有特性，提出长度感知的Trajectory-Balance目标函数，显式中和序列长度带来的结构性偏差。通过引入α-幂分布作为优化目标，建立可 principled 调节的分布形态控制机制。

【实验结果 / Results】

PowerFlow在多项基准测试中一致性地超越现有无监督RLIF方法，性能达到或超过有监督GRPO基线；在已对齐模型中有效缓解过度锐化问题，实现多样性与生成质量的同步提升，显著推进了创意任务的帕累托前沿。

【应用价值 / Applications】

该研究为LLM的无监督能力激发提供了理论严谨的方法论基础，可广泛应用于需要灵活调控模型行为模式的场景——如教育领域的逻辑推理强化、内容创作领域的创意多样性增强，以及模型对齐后的性能恢复与优化，有望降低对昂贵人工标注数据的依赖。
