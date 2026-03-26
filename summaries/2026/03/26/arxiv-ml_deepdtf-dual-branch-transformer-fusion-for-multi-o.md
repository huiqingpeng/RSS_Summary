---
title: "DeepDTF: Dual-Branch Transformer Fusion for Multi-Omics Anticancer Drug Response Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24265"
published: "2026-03-26"
summarized: "2026-03-27T07:22:39.076189"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DeepDTF，一种端到端的双分支Transformer融合框架，用于联合预测抗癌药物反应的log(IC50)回归值和药物敏感性分类。该框架通过模态特异性编码器和Transformer模块处理多组学数据，同时利用GNN-Transformer编码药物分子图，有效解决了高维多组学与化学结构药物之间的跨模态对齐难题。在公共药物基因组学基准测试中，DeepDTF在5折冷启动细胞系评估下显著优于强基线方法，使用全多组学输入时达到RMSE=1.248、R²=0.875和AUC=0.987的最佳性能，并将分类错误率降低9.5%。此外，该框架通过SHAP基因归因和预排序GSEA通路富集分析提供生物学可解释性。

【方法概述 / Method】
DeepDTF采用双分支架构：细胞系分支使用模态特异性编码器处理多组学谱，并通过Transformer块捕获长距离依赖关系；药物分支将化合物表示为分子图，采用GNN-Transformer编码器整合局部拓扑与全局上下文信息。两个分支的表征通过基于Transformer的融合模块进行交互，建模跨模态关系并缓解特征错位问题。

【实验结果 / Results】
在多种组学设置下，DeepDTF在5折冷启动细胞系评估中持续超越强基线方法；使用完整多组学输入时，模型取得RMSE=1.248、R²=0.875的回归性能和AUC=0.987的分类性能；相比对比方法，分类错误率（1-ACC）降低9.5%，展现出优异的预测精度和鲁棒性。

【应用价值 / Applications】
DeepDTF为精准肿瘤学提供计算决策支持，可辅助临床医生针对患者特定分子特征预测抗癌药物反应，指导个性化治疗方案选择；其SHAP-based可解释性分析有助于识别关键基因和生物通路，促进药物作用机制研究和潜在治疗靶点发现，加速精准医疗的临床转化应用。
