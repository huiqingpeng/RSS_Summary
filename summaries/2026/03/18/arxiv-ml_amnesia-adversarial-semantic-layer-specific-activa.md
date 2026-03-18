---
title: "Amnesia: Adversarial Semantic Layer Specific Activation Steering in Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.10080"
published: "2026-03-18"
summarized: "2026-03-18T17:15:38.826789"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Amnesia，一种轻量级的激活空间对抗攻击方法，通过操控开放权重LLMs的内部Transformer状态来绕过现有安全机制。研究表明，该攻击无需任何微调或额外训练即可有效生成有害内容，在基准数据集上成功诱导多种反社会行为。这些发现凸显了开放权重LLMs中更强大安全措施的紧迫需求，以及持续研究防止其潜在滥用的重要性。

【方法概述 / Method】
Amnesia采用对抗性语义层特定激活操控技术，在Transformer模型的特定语义层中注入精心设计的激活向量扰动，以干扰模型的安全对齐机制。该方法直接在推理阶段的激活空间进行操作，属于训练后攻击（post-training attack），无需访问训练数据或修改模型权重。

【实验结果 / Results】
实验在多个最先进的开放权重LLMs上进行，结果表明Amnesia能够有效绕过现有的安全防护措施，成功生成包括复杂钓鱼邮件和恶意代码在内的有害内容。攻击在基准数据集上展现出高成功率，能够诱导多种反社会行为，且攻击具有轻量级特性，计算开销极低。

【应用价值 / Applications】
本研究具有重要的安全警示价值：一方面为LLM安全研究者提供了红队测试（red-teaming）的新工具，用于评估和增强模型的鲁棒性；另一方面揭示了当前开放权重模型安全机制的脆弱性，推动开发更可靠的防御策略。研究成果对AI安全政策制定、模型部署风险评估以及负责任AI发展具有指导意义。
