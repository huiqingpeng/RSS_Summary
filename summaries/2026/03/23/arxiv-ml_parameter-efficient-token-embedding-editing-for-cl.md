---
title: "Parameter-Efficient Token Embedding Editing for Clinical Class-Level Unlearning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19302"
published: "2026-03-23"
summarized: "2026-03-24T07:16:09.639242"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对临床语言模型中的机器遗忘问题，提出了一种参数高效的类别级遗忘方法——稀疏词嵌入遗忘（STEU）。该方法仅通过更新PMI选择的词嵌入和一个小型分类器头部，在保持所有编码器层冻结的情况下，实现了对目标类别的有效遗忘。在MIMIC-IV、MIMIC-III和eICU数据集上的实验表明，STEU在仅修改0.19%模型参数的情况下，实现了近乎完全的遗忘（遗忘F1=0.0004），同时保持了较好的保留任务性能（保留平均F1=0.4766）。

【方法概述 / Method】

STEU采用点互信息（PMI）筛选与目标类别最相关的关键token，仅对这些token的嵌入层进行稀疏更新，并配合一个轻量级分类器头进行微调，而深层Transformer编码器参数保持冻结。这种设计将遗忘操作集中在输入嵌入空间，避免了昂贵的大规模参数重训练。

【实验结果 / Results】

在MIMIC-IV主实验设置中，STEU实现了近乎完全的类别遗忘（forget F1 ≈ 0），同时保留任务平均F1达到0.4766；跨BioClinicalBERT、BERT-base和DistilBERT三个模型架构均验证了方法的有效性。相比需要修改全部参数的传统重训练方法，STEU仅修改0.19%的参数即可达到相当的遗忘效果，显著降低了计算开销和模型存储成本。

【应用价值 / Applications】

该研究为医疗AI系统的合规部署提供了实用解决方案，特别适用于需要响应患者隐私删除请求（如GDPR"被遗忘权"）或移除特定敏感疾病类别知识的场景。方法的高效性使其适合资源受限的临床环境，能够在不牺牲模型整体性能的前提下快速、低成本地实现知识擦除，保障医疗数据隐私安全与法规合规。
