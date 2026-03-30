---
title: "Geometric Evolution Graph Convolutional Networks: Enhancing Graph Representation Learning via Ricci Flow"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26178"
published: "2026-03-30"
summarized: "2026-03-31T07:22:49.166775"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了几何演化图卷积网络（GEGCN），一种通过建模图上的几何演化来增强图表示学习的新框架。该方法利用长短期记忆网络（LSTM）对离散Ricci流生成的结构序列进行建模，并将学习到的动态表示注入图卷积网络。大量实验表明，GEGCN在多个基准数据集的分类任务上达到了最先进的性能，尤其在异配图（heterophilic graphs）上表现尤为出色。

【方法概述 / Method】
GEGCN的核心方法是将微分几何中的Ricci流理论引入图神经网络，通过离散Ricci流迭代演化图的曲率结构，生成一系列几何演化状态；随后使用LSTM捕捉这一结构序列的时序依赖关系，最终将这些动态几何特征融合到标准的GCN中进行节点表示学习。

【实验结果 / Results】
实验结果显示GEGCN在多个基准数据集上取得了最优的分类性能，特别是在异配图（节点倾向于与不同类别标签的邻居连接）上显著优于现有方法，证明了该方法能够有效捕获传统GNN难以处理的长距离结构信息和几何演化模式。

【应用价值 / Applications】
该研究适用于社交网络分析、分子性质预测、推荐系统等需要处理复杂图结构数据的场景，尤其擅长解决传统图神经网络在异配图上性能下降的问题，为图机器学习提供了融合几何分析与深度学习的有效途径。
