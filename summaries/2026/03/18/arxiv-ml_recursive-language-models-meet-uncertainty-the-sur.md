---
title: "Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15653"
published: "2026-03-18"
summarized: "2026-03-18T16:05:48.368572"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了SRLM框架，通过引入不确定性感知的自我反思机制来增强递归语言模型（RLM）的程序化上下文交互。研究发现，简单的自反思程序搜索无需显式递归即可匹敌或超越RLM，且RLM在模型上下文窗口内的任务中常表现劣于基线模型，而SRLM在长短文本上均能带来稳定提升。该工作挑战了"递归是RLM性能关键"的固有认知，为长上下文处理提供了更高效可靠的替代方案。

【方法概述 / Method】

SRLM采用程序化上下文交互结合不确定性感知的自我反思机制，利用三种内在信号（自一致性、推理长度和言语化置信度）作为模型内部不确定性的互补指标，用于评估和比较候选的上下文交互程序，从而指导程序搜索过程。

【实验结果 / Results】

在多样化基准数据集、不同上下文长度和骨干模型上的广泛实验表明，SRLM持续优于最先进基线，在相同时间预算下较RLM提升高达22%。研究还发现RLM在语义密集型任务中效果较差，而SRLM的自我反思机制能提供更优的语义信号来引导推理。

【应用价值 / Applications】

该研究为长上下文语言模型推理提供了实用改进方案，特别适用于需要可靠信息提取和复杂推理的文档分析、多轮对话和知识密集型任务。SRLM框架可无缝集成到现有语言模型推理流程中，在提升性能的同时降低了对复杂递归机制的依赖，具有较好的部署可行性和计算效率优势。
