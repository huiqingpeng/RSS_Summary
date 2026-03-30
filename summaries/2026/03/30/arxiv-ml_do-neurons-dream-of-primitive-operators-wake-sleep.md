---
title: "Do Neurons Dream of Primitive Operators? Wake-Sleep Compression Rediscovers Schank's Event Semantics"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25975"
published: "2026-03-30"
summarized: "2026-03-31T07:20:27.475772"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文首次证明事件基元可以通过纯压缩压力自动发现。研究者将DreamCoder的"觉醒-睡眠"库学习框架应用于事件状态转换，从四个通用基元出发，系统发现了与Schank手工编码的概念依赖理论（ATRANS、PTRANS、MTRANS等）直接对应的原语算子，同时还识别出Schank分类体系中缺失的心理/情感状态算子。在ATOMIC常识知识图谱上的实验表明，Schank原语仅能解释10%的自然事件，而发现的原语库可解释100%，且心理情感类算子（如CHANGE_wants、CHANGE_feels）占据主导地位。

【方法概述 / Method】
该方法将DreamCoder的觉醒-睡眠架构适配于事件理解任务：在"觉醒"阶段，系统寻找解释每个事件（以前/后世界状态对表示）的算子组合；在"睡眠"阶段，依据最小描述长度（MDL）原则提取重复出现的模式并优化为新算子。整个流程从四个通用基元开始，通过迭代压缩自动构建可复用的原语库。

【实验结果 / Results】
在合成数据上，发现的原语在贝叶斯MDL指标上达到Schank手工原语的96%，且能解释100%的事件（Schank原语仅81%）。在真实世界的ATOMIC数据上差距更为显著：Schank原语仅能覆盖10%的自然事件，而自动发现的原语库实现全覆盖；主导算子为CHANGE_wants（20%）、CHANGE_feels（18%）、CHANGE_is（18%）等心理情感类原语，而非Schank理论中的物理动作原语。

【应用价值 / Applications】
该研究为计算语义学和常识推理提供了信息论上可解释的事件表示框架，可应用于自然语言理解、知识图谱构建和认知建模。发现的心理/情感原语对社交推理、情感计算和对话系统具有重要价值，同时"压缩即认知"的范式为自动发现人类可解释的概念结构开辟了新路径。
