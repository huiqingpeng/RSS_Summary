---
title: "Statistical Testing Framework for Clustering Pipelines by Selective Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18413"
published: "2026-03-20"
summarized: "2026-03-20T13:12:50.050877"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对数据分析流程（data analysis pipelines）的统计可靠性量化问题，提出了一种基于选择性推断（selective inference）的新型统计检验框架。该框架专门用于评估聚类流程（clustering pipelines）的结果显著性，这些流程通常包含离群点检测、特征选择等数据依赖步骤。作者证明了所提检验能在任意名义水平下控制I类错误率，并通过合成数据集和真实数据集的实验验证了方法的有效性和正确性。

【方法概述 / Method】

本文采用选择性推断（selective inference）方法，为包含预定义步骤的聚类流程构建有效的统计检验。该方法通过考虑数据依赖步骤对最终聚类结果的选择效应，实现对聚类显著性的条件推断，从而解决传统假设检验在自适应分析流程中失效的问题。

【实验结果 / Results】

实验在合成数据集和真实数据集上验证了所提框架的有效性，结果表明该方法能够正确控制I类错误率。虽然具体数值指标未在摘要中详细给出，但实验证明了该检验框架在复杂异构数据分析场景下的统计有效性和实际可行性。

【应用价值 / Applications】

该研究为现代数据科学工作流提供了严格的统计推断工具，可应用于生物信息学、金融风控、医学影像分析等领域中涉及多步骤自适应分析的聚类任务。其价值在于使研究者能够对复杂数据分析流程的输出结果进行可靠的统计显著性评估，避免因数据窥探（data snooping）导致的假阳性发现。
