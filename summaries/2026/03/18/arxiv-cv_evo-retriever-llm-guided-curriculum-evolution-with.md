---
title: "Evo-Retriever: LLM-Guided Curriculum Evolution with Viewpoint-Pathway Collaboration for Multimodal Document Retrieval"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16455"
published: "2026-03-18"
summarized: "2026-03-18T18:14:00.583505"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了Evo-Retriever，一种用于多模态文档检索的新型检索框架。针对视觉-语言模型在处理真实世界文档时面临的异质性和非结构化问题，以及传统静态训练策略无法适应模型动态演化的挑战，作者设计了基于LLM引导的课程进化机制。该框架通过"视角-路径"协作，结合多视角图像对齐、双向对比学习策略和LLM元控制器自适应调整训练课程，在ViDoRe V2和MMEB (VisDoc)基准上取得了最先进的性能。

【方法概述 / Method】

Evo-Retriever的核心方法包含三个关键组件：首先，采用多视角图像对齐技术，通过多尺度和多方向视角增强细粒度匹配能力；其次，设计双向对比学习策略生成"困难查询"，为视觉和文本消歧建立互补学习路径以重新平衡监督信号；最后，将模型状态总结输入LLM元控制器，利用专家知识自适应调整训练课程以促进模型进化。

【实验结果 / Results】

在ViDoRe V2和MMEB (VisDoc)两个多模态文档检索基准数据集上，Evo-Retriever达到了最先进的性能水平，nDCG@5得分分别达到65.2%和77.1%。实验结果表明，该框架能够有效解决跨模态检索混淆问题，显著优于现有的后期交互方法。

【应用价值 / Applications】

Evo-Retriever可广泛应用于企业文档智能检索、数字图书馆多模态搜索、法律/医疗档案跨模态查询等场景，有效解决真实环境中扫描文档、PDF、图表等异质化内容的精准检索需求。该研究为构建能够持续自我进化的多模态检索系统提供了新范式，对提升大规模文档库的智能化管理和访问效率具有重要价值。
