---
title: "Clust-Splitter - an Efficient Nonsmooth Optimization-Based Algorithm for Clustering Large Datasets"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.04389"
published: "2026-03-19"
summarized: "2026-03-19T13:20:10.621976"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Clust-Splitter，一种基于非光滑优化的高效聚类算法，用于解决大规模数据集上的最小平方和聚类问题。该算法通过求解三个非光滑优化问题的序列（两个辅助问题生成合适的初始点，以及一个主聚类问题）来实现聚类任务。实验结果表明，该方法在处理大规模数据集时具有高效率，且解的质量与现有最优方法相当。

【方法概述 / Method】
Clust-Splitter采用有限内存束方法（limited memory bundle method）结合增量式策略来求解非光滑优化问题序列。该方法通过两个辅助优化问题生成高质量的初始聚类中心，再求解主聚类问题，从而避免传统方法易陷入局部最优的问题。

【实验结果 / Results】
在具有大量属性和大量数据点的真实世界数据集上的评估显示，Clust-Splitter在聚类效率和解的质量方面均表现出色，与多种最先进的大规模聚类算法相比具有竞争力，能够有效处理超大规模数据集。

【应用价值 / Applications】
该算法适用于需要处理海量高维数据的场景，如大规模客户细分、图像数据库聚类、基因组数据分析以及工业传感器数据聚类等，为数据挖掘和机器学习领域提供了一种兼具效率与精度的大规模聚类解决方案。
