---
title: "The impact of sensor placement on graph-neural-network-based leakage detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24076"
published: "2026-03-26"
summarized: "2026-03-27T07:20:11.718011"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了传感器部署位置对基于图神经网络（GNN）的供水管网泄漏检测性能的影响。作者提出了一种基于PageRank中心性的新型传感器部署方法，并在EPANET Net1基准网络上验证了该方法对压力重建、预测和泄漏检测任务的显著改进效果。研究表明，GNN的性能高度依赖于传感器测量的可用性和配置方式，合理的传感器布局是提升泄漏检测准确性的关键因素。

【方法概述 / Method】
论文采用PageRank中心性算法来确定供水管网中的最优传感器部署位置，利用图结构特征识别网络中对信息传播最关键的节点。该方法将管网拓扑建模为图结构，通过计算节点中心性得分来指导传感器选址，以最大化GNN对未测量节点的状态估计能力。

【实验结果 / Results】
在EPANET Net1网络上的实验表明，所提出的PageRank-Centrality传感器部署方法显著优于随机部署和基于度的部署策略。该方法在压力重建、预测和泄漏检测三项任务中均取得了性能提升，证明了传感器位置优化对GNN-based泄漏检测系统的重要性。

【应用价值 / Applications】
该研究为水务公司提供了经济高效的传感器网络规划方案，可在有限预算下实现最优监测覆盖。研究成果可直接应用于智慧水务基础设施的漏损管理系统，帮助降低非收益水损失，提升供水管网运营的可靠性和可持续性。
