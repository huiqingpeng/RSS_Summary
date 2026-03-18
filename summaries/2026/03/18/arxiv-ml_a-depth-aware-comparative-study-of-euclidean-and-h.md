---
title: "A Depth-Aware Comparative Study of Euclidean and Hyperbolic Graph Neural Networks on Bitcoin Transaction Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16080"
published: "2026-03-18"
summarized: "2026-03-18T15:40:30.228390"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究对比了欧几里得空间和双曲空间图神经网络（GNN）在比特币交易网络节点分类任务上的表现。通过固定模型架构和维度，系统性地变化邻域聚合深度，分析两种嵌入空间的差异。研究发现学习率与曲率的联合选择对高维双曲嵌入的稳定性至关重要，为计算社会系统中的超图神经网络部署提供了实践指导。

【方法概述 / Method】
采用控制实验设计，在固定模型架构和嵌入维度的条件下，显式变化邻域采样深度（neighborhood depth），对比欧几里得GNN与切空间双曲GNN（tangent-space hyperbolic GNN）。通过联合调优学习率和曲率参数，优化高维双曲嵌入的训练稳定性。

【实验结果 / Results】
实验在大型比特币交易图（Elliptic数据集）上进行节点分类任务。结果表明嵌入几何与邻域深度存在显著交互效应，且双曲GNN的优化行为对学习率和曲率的联合选择高度敏感。高维双曲嵌入的稳定性可通过适当的超参数组合实现。

【应用价值 / Applications】
该研究为金融欺诈检测、实体识别等比特币交易分析任务提供了模型选择依据。研究成果可推广至其他大规模社会技术系统（如社交网络、供应链网络）的图表示学习，指导从业者根据数据层次结构特征和可用计算资源合理选择嵌入几何与邻域聚合策略。
