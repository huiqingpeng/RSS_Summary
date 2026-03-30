---
title: "DPD-Cancer: Explainable Graph-based Deep Learning for Small Molecule Anti-Cancer Activity Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26114"
published: "2026-03-30"
summarized: "2026-03-31T07:21:58.823951"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DPD-Cancer，一种基于图注意力Transformer（GAT）的深度学习模型，用于小分子抗癌活性分类和细胞系特异性反应（pGI50）的定量预测。该模型在严格划分的NCI60数据集上AUC达0.87，在ACLPred/MLASM数据集上AUC高达0.98，pGI50预测的Pearson相关系数达0.72，显著优于现有方法（pdCSM-cancer、ACLPred和MLASM）。研究证实注意力机制在提取有意义的分子表征方面具有显著优势，并通过可视化分子亚结构提供可解释性，为候选药物优先级排序和先导化合物优化提供了有力工具。

【方法概述 / Method】
DPD-Cancer采用图注意力Transformer（Graph Attention Transformer, GAT）框架，将小分子建模为图结构，利用注意力机制学习分子中原子与化学键之间的复杂非线性关系。该方法整合了分子结构信息与细胞系上下文，通过多头注意力机制提取层次化的分子表征，实现对抗癌活性的分类预测和pGI50值的回归预测。

【实验结果 / Results】
在抗癌活性分类任务中，DPD-Cancer在NCI60数据集上AUC达0.87，在ACLPred和MLASM数据集上分别达0.98和0.97，显著优于pdCSM-cancer、ACLPred和MLASM等基线方法。在pGI50定量预测任务中，模型在涵盖10种癌症类型和73个细胞系的独立测试集上，Pearson相关系数最高达0.72，展现出良好的泛化能力和细胞系特异性预测性能。

【应用价值 / Applications】
DPD-Cancer可作为计算药物发现中的候选药物优先级排序工具，加速抗癌药物的筛选流程。其可解释性特性能够识别并可视化对活性预测起关键作用的分子亚结构，为药物化学家提供可操作的结构优化指导，支持先导化合物的定向改造。该模型已部署为免费网络服务器，便于生物医学研究人员实际应用。
