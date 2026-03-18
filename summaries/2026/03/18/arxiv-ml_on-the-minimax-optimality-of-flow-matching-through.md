---
title: "On the minimax optimality of Flow Matching through the connection to kernel density estimation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2504.13336"
published: "2026-03-18"
summarized: "2026-03-18T17:10:00.692621"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文建立了Flow Matching（流匹配）与核密度估计（KDE）之间的理论联系，证明了核密度估计器在Wasserstein距离下达到最优收敛速率（至多对数因子）。基于此，作者证明对于足够大的神经网络，Flow Matching同样能达到最优收敛速率。当目标分布位于低维流形上时，核密度估计器在流形邻域内受益于内在维度的降低，这一更快速率同样适用于Flow Matching，为其在高维场景中的实证成功提供了理论基础。

【方法概述 / Method】

本文采用理论分析方法，通过将Flow Matching与核密度估计建立联系，而非沿用扩散模型分析中的现有工具。作者首先分析核密度估计器在Wasserstein距离下的收敛性质，特别是针对高斯核改进了已有界，然后将这些结果迁移到Flow Matching的理论保证中，并进一步扩展到低维流形情形。

【实验结果 / Results】

论文的主要理论结果表明：（1）核密度估计器在Wasserstein距离下达到最优收敛速率，改进了高斯核的现有界；（2）对于充分大的网络，Flow Matching达到最优速率至多对数因子；（3）当目标分布位于低维流形时，估计器在流形的小邻域内获得由内在维度决定的更快收敛速率，该性质同样适用于Flow Matching。

【应用价值 / Applications】

本研究为Flow Matching在生成建模中的应用提供了严格的统计理论支撑，特别是在高维数据生成和低维流形数据建模场景中。该理论结果有助于指导神经网络架构设计和训练策略选择，并为理解扩散模型类方法的样本效率与收敛行为提供了新的分析视角，对图像生成、分子建模等需要处理高维复杂分布的实际应用具有重要指导意义。
