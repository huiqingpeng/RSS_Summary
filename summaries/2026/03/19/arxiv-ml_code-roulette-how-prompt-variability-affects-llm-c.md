---
title: "Code Roulette: How Prompt Variability Affects LLM Code Generation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2506.10204"
published: "2026-03-19"
summarized: "2026-03-19T14:15:53.714892"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了提示词（prompt）变化对大型语言模型（LLM）代码生成质量的影响。作者指出，尽管LLM降低了编程门槛，但生成代码的功能性和质量对用户背景和软件开发熟悉度高度敏感。为此，论文提出了一种与具体编程任务和LLM无关的评估流程，用于量化LLM对提示词增强的敏感性，并通过大量实验验证了其有效性。

【方法概述 / Method】
论文设计了一个通用的评估管道（evaluation pipeline），通过系统性地对输入提示词进行增强和变体处理，来测量LLM代码生成输出的稳定性和一致性。该方法不依赖于特定的编程任务或LLM模型，具有广泛的适用性。

【实验结果 / Results】
作者提供了广泛的实验证据，展示了该方法在评估LLM代码生成敏感性方面的实用性（具体性能指标未在提供的摘要中详述）。相关代码已开源供社区使用。

【应用价值 / Applications】
该研究可帮助开发者和研究者更好地理解LLM对提示词的敏感程度，从而指导更鲁棒的提示工程设计。其通用评估框架可应用于不同LLM和编程任务的基准测试，对提升AI辅助编程工具的可靠性和用户体验具有重要价值。
