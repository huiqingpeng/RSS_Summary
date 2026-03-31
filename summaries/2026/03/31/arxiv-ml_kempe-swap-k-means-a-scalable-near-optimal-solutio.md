---
title: "Kempe Swap K-Means: A Scalable Near-Optimal Solution for Semi-Supervised Clustering"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27417"
published: "2026-03-31"
summarized: "2026-04-01T07:23:59.466178"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为 Kempe Swap K-Means 的新型基于质心的启发式算法，用于处理带有刚性 must-link（ML）和 cannot-link（CL）约束的半监督聚类问题。该算法采用双阶段迭代过程：分配步骤利用 Kempe 链交换在约束解空间中优化当前聚类，质心更新步骤计算最优聚类中心。通过在更新阶段引入受控扰动以增强全局搜索能力并避免局部最优，实验表明该方法在保持高计算效率和可扩展性的同时实现了接近最优的划分，在聚类准确率和算法效率方面均优于现有最优基准方法。

【方法概述 / Method】
Kempe Swap K-Means 采用双阶段迭代框架：首先通过 Kempe 链交换机制在约束解空间中进行样本分配优化，确保满足 must-link 和 cannot-link 约束；然后在质心更新阶段引入受控扰动策略以增强全局探索能力，避免陷入局部最优解。

【实验结果 / Results】
实验结果表明，Kempe Swap K-Means 在大规模数据集上实现了接近最优的聚类划分，同时在聚类准确率和算法运行效率方面均显著优于现有最先进的基准方法，展现出良好的计算效率和可扩展性。

【应用价值 / Applications】
该研究适用于需要利用少量先验知识（如样本必须属于同一类或必须属于不同类）进行数据分组的场景，如文档分类、图像分割、客户细分和生物信息学中的基因表达聚类等大规模半监督聚类任务，能够在保证约束满足的同时高效处理大规模数据。
