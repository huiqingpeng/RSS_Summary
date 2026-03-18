---
title: "Probing Cultural Signals in Large Language Models through Author Profiling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16749"
published: "2026-03-18"
summarized: "2026-03-18T16:14:34.281175"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究通过零样本作者画像任务（从歌词推断歌手的性别和种族）探测大型语言模型（LLMs）中的文化信号。研究发现，多个开源模型在超过10,000首歌词上展现出非平凡的性能，但存在系统性文化对齐：大多数模型默认偏向北美种族，而DeepSeek-1.5B则更强烈地对齐亚洲种族。研究还提出了两种公平性指标（MAD和RD），发现Ministral-8B种族偏见最强，Gemma-12B最为均衡。

【方法概述 / Method】
研究者采用零样本设置，让LLMs直接从歌词文本推断歌手的性别和种族属性，无需任务特定微调。通过分析模型的预测分布和生成的推理依据（rationales）来识别文化偏见模式，并引入模态准确率差异（MAD）和召回率差异（RD）两种新指标量化公平性 disparities。

【实验结果 / Results】
在超过10,000首歌词的评估中，多个开源LLMs展现出可识别的作者画像能力，但表现出显著的文化对齐差异：DeepSeek-1.5B偏向亚洲种族，而大多数其他模型偏向北美种族。量化分析显示Ministral-8B的种族偏见最为严重，Gemma-12B表现最为平衡。

【应用价值 / Applications】
该研究为审计LLMs中的文化偏见提供了可扩展的零样本评估框架，有助于开发更公平、文化包容的AI系统。提出的MAD和RD指标可广泛应用于模型公平性评测，对需要处理多元文化内容的社会影响型应用（如内容推荐、自动审核）具有重要指导意义。
