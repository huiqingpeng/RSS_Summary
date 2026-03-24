---
title: "Understanding Contextual Recall in Transformers: How Finetuning Enables In-Context Reasoning over Pretraining Knowledge"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20969"
published: "2026-03-24"
summarized: "2026-03-25T07:16:46.781318"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了Transformer模型中的"上下文回忆"（contextual recall）能力——即模型利用成对示例在新提示格式中回忆特定事实的能力。研究发现，仅靠预训练虽然能获得事实知识，但不足以实现上下文回忆；模型无法在没有语法统计信息的ICL提示中隐式推断属性类型。然而，在需要隐式推理的任务上进行微调（使用部分主题）可以触发所有主题的上下文回忆能力涌现，同时伴随共享属性类型的低维潜在编码形成。

【方法概述 / Method】
作者构建了一个受控的合成框架，其中预训练序列由"主语-语法-属性"三元组组成，属性类型与语法统计相关联。通过该框架，系统性地检验预训练、微调和ICL评估各阶段的能力表现，并推导了一个仅含注意力机制的Transformer构造来复现从事实回忆到上下文回忆的转换过程。

【实验结果 / Results】
预训练模型在标准事实回忆任务上表现良好，但在移除语法统计信息的ICL提示中失败；而经过隐式推理任务微调后，模型展现出跨主题的泛化性上下文回忆能力。机制分析表明，这一转变伴随着低维潜在编码的出现，且理论构造与实证验证高度一致。

【应用价值 / Applications】
该研究为理解大语言模型的上下文学习能力提供了机制层面的洞见，有助于指导更高效的微调策略设计，减少对大规模预训练的依赖。此外，对"预训练获取知识、微调激发推理"这一范式的澄清，可应用于提升模型在少样本场景下的适应性和可靠性。
