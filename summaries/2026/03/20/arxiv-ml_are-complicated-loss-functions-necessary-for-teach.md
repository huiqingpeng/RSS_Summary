---
title: "Are complicated loss functions necessary for teaching LLMs to reason?"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18756"
published: "2026-03-20"
summarized: "2026-03-20T12:15:36.283518"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究系统分析了 Group Relative Policy Optimization (GRPO) 在提升大语言模型推理能力时的核心组件必要性。研究发现：引入负反馈信号对学习至关重要，而 PPO 风格的策略比率裁剪等约束并非必需。基于此，作者提出了简化的 REINFORCE with Group Relative Advantage (RGRA) 方法，在标准数学基准测试中展现出优于 GRPO 的潜力，表明简单的 REINFORCE 类方法即可有效增强 LLM 推理能力。

【方法概述 / Method】

作者对 GRPO 进行组件消融分析，识别出关键设计要素：保留群组相对优势估计（group relative advantage estimation）以利用组内样本的相对比较，但去除 PPO 风格的策略比率裁剪（policy ratio clipping）和 KL 正则化项。最终提出的 RGRA 是一种更透明、更简洁的强化学习变体，核心仅包含带有群组相对优势估计的 REINFORCE 梯度更新。

【实验结果 / Results】

实验在标准数学推理基准上进行，结果表明 RGRA 能够达到比 GRPO 更强的性能。具体而言，去除 PPO 风格约束并未损害、反而有助于提升数学推理能力；同时验证仅训练高于基线的动作会限制学习效果，而纳入负反馈能显著改善训练动态和最终表现。

【应用价值 / Applications】

该研究为 LLM 推理能力的后训练提供了更高效、更易实现的方案，降低了计算资源门槛和算法复杂度，便于研究者和工业界快速部署。简化的 RGRA 方法提升了训练过程的透明度和可解释性，有助于进一步理解强化学习在推理任务中的工作机制，推动更轻量、更可控的 LLM 推理优化技术发展。
