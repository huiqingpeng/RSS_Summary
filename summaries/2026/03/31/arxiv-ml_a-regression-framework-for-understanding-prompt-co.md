---
title: "A Regression Framework for Understanding Prompt Component Impact on LLM Performance"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26830"
published: "2026-03-31"
summarized: "2026-04-01T07:19:42.940133"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种统计回归框架，用于量化分析提示词（prompt）各组成部分对大型语言模型（LLM）性能的影响。该方法扩展了可解释人工智能（XAI）技术，通过拟合回归模型将提示词的不同部分与LLM评估结果关联起来。研究发现，错误示例会显著阻碍Mistral-7B和GPT-OSS-20B模型解决算术问题，而正负向指令对模型性能的影响存在矛盾效应，回归模型可分别解释两模型72%和77%的性能变异。

【方法概述 / Method】
作者采用基于回归的XAI方法，将提示词分解为多个组成部分（如指令、示例等），构建统计模型来量化各部分对LLM性能的独立贡献。该方法通过系统性操控提示词元素，建立提示特征与模型输出质量之间的可解释映射关系。

【实验结果 / Results】
在简单算术任务上，回归模型对Mistral-7B和GPT-OSS-20B的性能变异解释力分别达到72%和77%。关键发现包括：错误示例（misinformation）显著损害两模型表现；正向示例无显著效果；正负向指令对模型性能产生相互矛盾的影响。

【应用价值 / Applications】
该框架为关键决策场景（如医疗、法律、金融等高风险应用）提供了精细化工具，帮助决策者理解提示词如何影响LLM的任务解决行为。该方法可支持提示工程优化、模型可靠性评估及AI系统的透明化治理。
