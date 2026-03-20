---
title: "CeRA: Breaking the Linear Ceiling of Low-Rank Adaptation via Manifold Expansion"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.22911"
published: "2026-03-20"
summarized: "2026-03-20T14:11:42.084769"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CeRA（Capacity-enhanced Rank Adaptation），一种突破低秩适应（LoRA）"线性天花板"的参数高效微调方法。研究发现LoRA在复杂推理任务中存在固有线性约束，单纯增加秩会导致收益递减。CeRA通过权重级并行适配器引入SiLU门控和结构化dropout实现流形扩展，在SlimOrca基准上以rank 64超越LoRA rank 512的性能，并在高复杂度MATH数据集上以1/8参数量实现更优推理准确率。

【方法概述 / Method】
CeRA采用权重级并行适配器架构，在保持低秩结构的同时注入SiLU激活门控机制和结构化dropout策略，诱导表示流形的非线性扩展。该方法通过奇异值分解分析验证其能够激活传统线性方法中处于休眠状态的奇异值谱尾部，有效避免秩坍缩问题。

【实验结果 / Results】
在SlimOrca基准上，CeRA（rank 64，PPL 3.89）显著优于LoRA（rank 512，PPL 3.90）；在MATH复杂数学推理数据集上，CeRA rank 64取得Pass@1 16.36%，超越LoRA rank 512的15.72%。SVD机制分析证实CeRA能激活奇异值谱的休眠尾部，而简单算术任务GSM8K上两者表现相当，凸显任务复杂度对方法选择的关键影响。

【应用价值 / Applications】
CeRA适用于大语言模型在资源受限环境下的高效微调，特别是需要复杂推理能力的数学求解、代码生成和科学计算等场景。该方法以极低参数开销（1/8于传统LoRA）实现更高性能，为边缘设备部署和快速领域适配提供了实用解决方案，同时其流形扩展机制为理解神经网络表示学习提供了新的分析视角。
