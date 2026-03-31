---
title: "Active In-Context Learning for Tabular Foundation Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27385"
published: "2026-03-31"
summarized: "2026-04-01T07:23:20.256898"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了表格主动上下文学习（Tab-AICL）框架，利用表格基础模型TabPFN的上下文学习能力解决传统主动学习在表格数据冷启动阶段不确定性估计不可靠的问题。研究设计了四种样本获取策略，包括基于不确定性的TabPFN-Margin、基于多样性的TabPFN-Coreset、混合策略TabPFN-Hybrid以及可扩展的两阶段方法TabPFN-Proxy-Hybrid。在20个分类基准数据集上的实验表明，Tab-AICL在100个标注样本以内的冷启动阶段，相比重新训练的梯度提升基线（CatBoost和XGBoost）具有更优的样本效率。

【方法概述 / Method】
Tab-AICL利用TabPFN的免训练上下文学习特性，将主动学习的优化目标从模型参数转向标注样本的上下文集合，通过迭代选择信息丰富的样本构建最优上下文。提出的四种获取规则分别针对不确定性量化、多样性覆盖、两者混合以及大规模场景下的可扩展性（先用轻量级线性代理模型筛选候选，再用TabPFN精细选择）。

【实验结果 / Results】
在20个表格分类基准数据集上，以归一化AULC（Area Under Learning Curve）为指标，Tab-AICL在冷启动阶段（≤100标注样本）显著优于传统的重新训练式主动学习方法。特别是TabPFN-Proxy-Hybrid在保持性能的同时大幅提升了计算效率，解决了TabPFN推理成本随上下文规模增长的问题。

【应用价值 / Applications】
该研究适用于标注成本高昂的表格数据场景，如医疗诊断、金融风控和科学实验设计等领域，能够在有限预算下快速构建高性能预测模型。Tab-AICL的免训练特性使其特别适合需要频繁重新部署或数据分布动态变化的实时决策系统。
