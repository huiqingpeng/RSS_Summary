---
title: "Interpretable Zero-shot Referring Expression Comprehension with Query-driven Scene Graphs"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.25004"
published: "2026-03-27"
summarized: "2026-03-28T07:20:20.413700"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SGREC，一种基于查询驱动场景图的可解释零样本指代表达理解（REC）方法。该方法通过构建显式编码空间关系、描述性标题和对象交互的场景图，弥合了低级图像区域与高级语义理解之间的鸿沟。实验表明，SGREC在多个零样本REC基准测试上取得了最优性能，包括RefCOCO val（66.78%）、RefCOCO+ testB（53.43%）和RefCOCOg val（73.28%），同时提供可解释的推理过程。

【方法概述 / Method】
SGREC采用三阶段架构：首先利用视觉-语言模型（VLM）构建与查询相关的场景图，显式编码空间关系、描述性标题和对象交互；然后将该结构化文本表示输入大语言模型（LLM）进行推理；最终LLM推断目标对象并生成决策解释，确保推理过程的可解释性。

【实验结果 / Results】
SGREC在主流零样本REC基准上达到顶尖性能：RefCOCO验证集66.78%、RefCOCO+测试集B 53.43%、RefCOCOg验证集73.28%，在大多数基准上取得top-1准确率。这些结果显著超越了直接测量文本查询与图像区域特征相似性的传统CLIP类方法。

【应用价值 / Applications】
该方法适用于需要零样本视觉-语言理解的场景，如机器人导航中的自然语言指令执行、智能监控中的目标检索、以及无障碍辅助技术中的视觉内容描述。其可解释性特点使其特别适合医疗诊断、自动驾驶等对决策透明度要求高的安全关键领域。
