---
title: "From Drop-off to Recovery: A Mechanistic Analysis of Segmentation in MLLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17228"
published: "2026-03-19"
summarized: "2026-03-19T13:10:53.851806"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究通过逐层线性探测评估，系统分析了多模态大语言模型（MLLMs）在像素级分割任务中的内在空间理解能力。研究发现，适配器（adapter）会导致分割表征的"下降"（drop-off），但LLM层通过注意力介导的精细化机制逐步恢复表征质量，其中正确分类的token会引导错误分类的相邻token趋向正确标签。此外，研究揭示了因果注意力在早期图像token位置对恢复的限制，以及双向注意力在缓解这一问题中的作用，为理解MLLMs的视觉处理机制提供了系统性解释。

【方法概述 / Method】
论文采用三种核心分析方法：（1）逐层线性探测评估，覆盖视觉编码器、适配器和LLM全流程，量化各阶段的分割表征质量；（2）基于干预的注意力敲除分析（attention knockout），验证跨token注意力是否逐步精细化视觉表征；（3）图像token间双向注意力评估，检验空间一致性建模机制。这些方法共同构成了从表征学习到注意力机制的完整分析框架。

【实验结果 / Results】
实验发现适配器阶段出现显著的分割表征退化，而LLM深层逐步恢复至甚至超越视觉编码器的性能；注意力敲除分析证实了"正确token引导邻居修正"的协同精细化机制；早期图像token因因果注意力掩码导致恢复受限，而引入双向注意力可有效缓解该边界效应，提升空间一致性。

【应用价值 / Applications】
该研究为设计更高效的分割导向MLLM架构提供了直接指导，如优化适配器设计以减少表征退化、在关键层引入双向注意力机制等；同时，其 mechanistic analysis 方法论可推广至其他像素级视觉任务（如深度估计、姿态估计）的模型可解释性研究，助力构建更具可解释性和可控性的多模态系统。
