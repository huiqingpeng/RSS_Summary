---
title: "On the Use of Bagging for Local Intrinsic Dimensionality Estimation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24384"
published: "2026-03-26"
summarized: "2026-03-27T07:23:20.479245"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了使用Bagging集成方法降低局部内在维度（LID）估计方差的问题。作者提出通过子采样Bagging策略保持最近邻距离的局部分布，同时分析了采样率、k-NN邻域大小和集成规模等超参数之间的复杂交互关系。理论分析和实验结果表明，在广泛的超参数范围内，Bagging估计器能显著降低方差和均方误差，且与邻域平滑结合可进一步提升估计性能。

【方法概述 / Method】

论文采用子采样Bagging（subbagging）作为方差缩减策略，通过对原始样本进行有放回抽样生成多个子样本，在每个子样本上独立计算LID估计后进行聚合。该方法的核心挑战在于处理采样率与邻域大小之间的耦合关系——子采样会降低有效样本量，从而扩大k-NN的搜索半径，影响估计的局部性和分辨率。

【实验结果 / Results】

实验表明，在合理选择的超参数区域内，Bagging估计器相比非Bagging基线能显著降低估计方差和均方误差，同时保持可控的偏差增长。研究还量化了采样率、k值和集成大小对估计性能的影响规律，并验证了Bagging与邻域平滑结合可带来进一步的性能提升。

【应用价值 / Applications】

该研究为数据挖掘和机器学习中的LID估计提供了更稳定可靠的计算工具，可应用于异常检测、流形学习、数据复杂度分析和神经网络鲁棒性评估等任务。通过提供超参数选择的理论指导，该方法使从业者能够根据具体应用需求（如偏好方差缩减或偏差控制）进行 informed 的参数配置。
