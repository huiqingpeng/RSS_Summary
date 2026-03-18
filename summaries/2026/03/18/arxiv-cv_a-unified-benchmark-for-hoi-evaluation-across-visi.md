---
title: "A Unified Benchmark for HOI Evaluation across Vision-Language Models and HOI-Specific Methods"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2508.18753"
published: "2026-03-18"
summarized: "2026-03-18T18:27:02.383069"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CrossHOI-Bench，一个统一的多选式人机交互（HOI）评测基准，解决了现有基准（如HICO-DET）因不完全标注导致对视觉语言模型（VLM）不公平惩罚的问题。该基准通过显式正样本和精心设计的负样本，实现了VLM与专用HOI方法的可靠跨范式比较。实验发现，大型VLM在零样本设置下表现竞争力强，但在多并发动作和动作归属判断上存在不足；而专用HOI方法则在多动作识别和人物-动作匹配上更具优势，揭示了两种范式互补的优劣特性。

【方法概述 / Method】
作者设计了多选格式的HOI评测框架，每个测试样本包含一个图像查询、一个正确答案和多个经过筛选的干扰项（curated negatives），从而避免不完全标注带来的评测偏差。该基准特别聚焦于挑战性场景，包括多人交互场景和细粒度交互区分任务，以充分检验模型在复杂情境下的真实能力。

【实验结果 / Results】
实验表明，大型生成式VLM在零样本HOI检测中达到了与专用方法相当甚至更优的性能；然而，VLM在处理多个并发动作以及正确将交互分配给目标人物方面表现较差。相比之下，专用HOI方法在一般HOI推理能力上较弱，但在多动作识别和人物-动作对应关系的判断上更为可靠，现有基准因错误惩罚机制未能揭示这些差异。

【应用价值 / Applications】
该研究为HOI领域的模型选型提供了重要参考：需要零样本泛化能力的场景可优先考虑大型VLM，而要求精确动作定位和多人交互分析的应用则更适合专用HOI方法。CrossHOI-Bench的评测范式也可推广至其他视觉-语言任务的标准化评估，促进通用模型与专用模型的公平比较与协同发展。
