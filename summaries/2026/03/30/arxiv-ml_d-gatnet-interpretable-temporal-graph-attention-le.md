---
title: "D-GATNet: Interpretable Temporal Graph Attention Learning for ADHD Identification Using Dynamic Functional Connectivity"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26308"
published: "2026-03-30"
summarized: "2026-03-31T07:23:31.702163"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究提出D-GATNet，一种可解释的时序图注意力网络框架，用于基于动态功能连接（dFC）的ADHD自动分类。该模型结合图注意力网络学习空间依赖关系和时序注意力机制捕捉时间动态，在ADHD-200数据集上达到85.18%的平衡准确率和0.881 AUC，显著优于现有方法。注意力分析揭示了小脑和默认模式网络的功能紊乱，为ADHD神经影像标志物识别提供了新见解。

【方法概述 / Method】

研究采用滑动窗口Pearson相关构建时序功能脑网络，以感兴趣区（ROI）为节点、连接强度为边。模型架构融合多层图注意力网络（GAT）提取空间特征，并通过1D卷积结合时序注意力模块建模动态变化。可解释性通过三重注意力机制实现：图注意力权重显示主导ROI交互，ROI重要性评分识别关键脑区，时序注意力突出信息丰富的时间片段。

【实验结果 / Results】

在ADHD-200数据集北京大学站点上，采用分层10折交叉验证结合5种子集成策略，D-GATNet取得85.18% ± 5.64%的平衡准确率和0.881 AUC，超越现有最先进方法。注意力可视化分析发现小脑和默认模式网络（DMN）存在显著功能连接异常，为ADHD病理机制提供了潜在的神经影像生物标志物证据。

【应用价值 / Applications】

该研究为ADHD的客观辅助诊断提供了高精度、可解释的深度学习工具，有助于减少传统行为评估的主观性。模型揭示的可解释神经生物标志物（如小脑-DMN连接异常）可指导未来神经调控治疗靶点选择，并促进对ADHD时间动态神经机制的理解，具有临床转化和神经科学研究双重价值。
