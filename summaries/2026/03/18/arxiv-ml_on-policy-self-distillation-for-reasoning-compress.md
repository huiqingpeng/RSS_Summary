---
title: "On-Policy Self-Distillation for Reasoning Compression"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.05433"
published: "2026-03-18"
summarized: "2026-03-18T17:05:31.346846"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出OPSDC（On-Policy Self-Distillation for Reasoning Compression），一种通过自我蒸馏让推理模型学会更简洁推理的方法。该方法无需标准答案、token预算或难度估计器，仅需让同一模型在"be concise"指令下生成教师logits，并在学生自身rollout上最小化per-token反向KL散度。实验表明，该方法在Qwen3-8B和Qwen3-14B上实现57-59%的token压缩，同时MATH-500准确率提升9-16个百分点，AIME 2024上14B模型提升10分且压缩41%。关键发现是：推理模型产生的许多token不仅是冗余的，而且是有害的，会随不必要token累积错误。

【方法概述 / Method】
OPSDC采用在线策略自我蒸馏框架，核心为同一模型双重角色机制：添加"be concise"指令作为教师生成简洁推理的logits分布，无指令版本作为学生生成标准rollout，通过最小化per-token反向KL散度将简洁行为蒸馏回模型自身。该方法完全自举，不依赖外部监督信号或问题难度先验。

【实验结果 / Results】
在MATH-500基准上，Qwen3-8B和Qwen3-14B分别实现59%和57%的token压缩率，准确率从基线提升9-16个百分点；在AIME 2024上，14B模型获得10分绝对提升，同时实现41%压缩。模型展现出自适应压缩特性：对简单问题激进压缩，对困难问题保留必要推理深度。

【应用价值 / Applications】
该方法可显著降低推理模型部署的推理成本与延迟，适用于需要高效数学推理的教育辅助、科研计算及实时交互系统。其自举特性使其易于扩展到新领域或更大规模模型，为推理模型的实际产业化部署提供了即插即用的效率优化方案。
