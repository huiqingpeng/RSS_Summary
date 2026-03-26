---
title: "i-IF-Learn: Iterative Feature Selection and Unsupervised Learning for High-Dimensional Complex Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24025"
published: "2026-03-26"
summarized: "2026-03-27T07:19:50.539235"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出i-IF-Learn，一种迭代式无监督学习框架，能够联合执行特征选择与聚类任务。核心创新在于设计了一种自适应特征选择统计量，动态融合伪标签监督信号与无监督信号，根据中间标签的可靠性进行调整，有效缓解迭代框架中的误差传播问题。该框架在低维嵌入（PCA或拉普拉斯特征映射）后结合k-means聚类，同时输出有影响力的特征子集和聚类标签。实验表明，该方法在基因微阵列和单细胞RNA测序数据集上显著优于经典和深度聚类基线，且所选特征作为预处理能显著提升DeepCluster、UMAP和VAE等下游深度模型的性能。

【方法概述 / Method】
i-IF-Learn采用迭代优化策略，交替执行特征选择与聚类：首先通过PCA或拉普拉斯特征映射将高维数据降维，然后进行k-means聚类生成伪标签；核心在于自适应特征选择统计量，该统计量结合伪标签监督信息与无监督信号（如特征方差或结构信息），并根据当前迭代中伪标签的可靠性动态调整权重，从而在迭代过程中逐步精炼有影响力的特征子集。

【实验结果 / Results】
在基因微阵列和单细胞RNA-seq数据集上的数值实验表明，i-IF-Learn显著超越经典聚类方法（如k-means、层次聚类）和深度聚类基线（如DeepCluster）；此外，将i-IF-Learn选出的有影响力特征作为预处理输入，能够大幅提升下游深度模型（包括DeepCluster、UMAP和VAE）的聚类性能，验证了目标化特征选择的重要性与有效性。

【应用价值 / Applications】
该研究主要应用于高维生物医学数据分析，特别是基因表达数据（微阵列和单细胞RNA测序）的降维与聚类，有助于识别驱动细胞类型或疾病状态的关键基因特征；同时，其特征选择结果可作为通用预处理模块，增强各类下游深度学习模型的表现，具有广泛的生物信息学和精准医学研究价值。
