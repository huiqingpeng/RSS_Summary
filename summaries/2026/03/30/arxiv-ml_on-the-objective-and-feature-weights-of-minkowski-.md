---
title: "On the Objective and Feature Weights of Minkowski Weighted k-Means"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25958"
published: "2026-03-30"
summarized: "2026-03-31T07:20:21.379950"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了Minkowski加权k-means（mwk-means）算法的理论性质，该算法通过引入特征权重和Minkowski距离扩展了经典k-means。作者证明了mwk-means目标函数可表示为簇内离散度的幂均值聚合，其中Minkowski指数p控制着特征选择性与均匀性使用的过渡。基于此，论文推导了目标函数的边界，刻画了特征权重的结构特性，并证明了算法收敛性，为mwk-means行为提供了统一的理论解释。

【方法概述 / Method】

论文采用理论分析方法，将mwk-means目标函数重新表述为幂均值聚合形式，揭示Minkowski指数p与特征权重分配机制的关系。通过数学推导分析特征权重对相对离散度的依赖关系，并建立目标函数的上界与下界。

【实验结果 / Results】

研究发现特征权重仅依赖于相对离散度，并与离散度比率呈幂律关系；该特性为高离散度特征的抑制提供了显式理论保证。此外，论文严格证明了mwk-means算法的收敛性，完善了其理论基础。

【应用价值 / Applications】

该研究为高维数据聚类中自动特征选择机制提供了理论依据，有助于理解mwk-means在不同p值参数下的行为模式。研究成果可指导实际应用中Minkowski指数的选取，并为开发具有可解释特征加权策略的聚类算法奠定理论基础。
