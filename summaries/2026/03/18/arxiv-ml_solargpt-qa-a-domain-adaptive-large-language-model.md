---
title: "SolarGPT-QA: A Domain-Adaptive Large Language Model for Educational Question Answering in Space Weather and Heliophysics"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.12131"
published: "2026-03-18"
summarized: "2026-03-18T17:04:12.899112"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SolarGPT-QA，一个面向空间天气与日球物理学教育问答的领域自适应大语言模型。该模型基于LLaMA-3架构，利用科学文献和由GPT-4生成、Grok-3优化的问答数据进行训练，采用学生友好的叙事风格。研究通过LLM-as-judge评估框架验证了模型在科学准确性、清晰度、完整性和教学有效性方面的优势，表明领域自适应预训练与微调相结合对平衡科学准确性和教育效果至关重要。

【方法概述 / Method】
SolarGPT-QA采用两阶段训练策略：首先进行领域自适应预训练，然后针对教育问答任务进行指令微调。训练数据包括专业科学文献以及由GPT-4生成、经Grok-3以故事化叙事风格精炼的大规模问答对。评估阶段引入LLM-as-judge框架，由强参考模型依据结构化标准对生成答案进行多维度质量评判。

【实验结果 / Results】
在零样本设置下，SolarGPT-QA显著优于通用大语言模型；与经过指令微调的模型相比，其在空间天气与日球物理学教育解释任务上达到具有竞争力的性能水平。消融实验证实，单纯预训练或单纯微调均无法同时保证科学准确性与教学有效性，二者结合是实现最优平衡的关键。

【应用价值 / Applications】
该研究为空间科学教育提供了专业化AI工具，可辅助学生理解太阳活动、日冕物质抛射等复杂概念，弥补通用模型在领域知识与教学能力上的不足。其方法论可推广至其他STEM教育领域，为构建学科专属的智能教育助手提供范式参考，同时支持公众科学传播与空间天气预警知识的普及。
