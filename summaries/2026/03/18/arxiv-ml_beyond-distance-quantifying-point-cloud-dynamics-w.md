---
title: "Beyond Distance: Quantifying Point Cloud Dynamics with Persistent Homology and Dynamic Optimal Transport"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15683"
published: "2026-03-18"
summarized: "2026-03-18T16:06:39.840194"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种分析时变点云拓扑突变（topological tipping）的框架，通过扩展拓扑最优传输（TpOT）距离来克服其全局标量距离难以捕捉动态相变中瞬态、局部结构重组的局限。作者构建了一个分层动态评估框架，采用新颖的拓扑和超图重建策略，通过插值底层空间几何而非抽象网络参数来确保物理保真度。该框架引入了多尺度指标：宏观指标（拓扑畸变和持续熵）捕捉全局变化，中观双视角超图熵（节点视角和边视角）检测高度敏感的异步局部重连，并将环级熵变化传播到单个顶点形成点级拓扑场。在物理动力系统（Rayleigh-Van der Pol极限环、双势阱聚类融合）、高维生物聚集（D'Orsogna模型）和纵向卒中fMRI数据上的广泛评估验证了该方法的有效性。

【方法概述 / Method】

论文的核心方法是在TpOT距离基础上构建分层动态评估框架，通过沿测地线插值底层空间几何而非直接插值抽象网络参数，并严格重新计算有效的拓扑结构。该方法引入了三层多尺度指标：宏观层面的拓扑畸变（Topological Distortion）和持续熵（Persistence Entropy），中观层面的双视角超图熵（节点视角和边视角），以及微观层面的点级拓扑场（通过将环级熵变化传播到单个顶点实现）。

【实验结果 / Results】

作者在三类系统上进行了广泛验证：物理动力系统（包括Rayleigh-Van der Pol极限环和双势阱聚类融合）、高维生物聚集模型（D'Orsogna模型）以及纵向卒中fMRI数据。实验结果表明，结合基于传输的对齐（transport-based alignment）与多尺度熵诊断能够有效捕捉动态拓扑分析中的关键特征，特别是传统全局标量距离无法检测的瞬态局部结构重组。

【应用价值 / Applications】

该研究具有广泛的实际应用价值，特别是在需要精细分析动态结构变化的领域：神经影像学中可用于追踪卒中后大脑功能网络的动态重组，生物物理学中可用于研究细胞聚集或群体行为模式，以及一般复杂系统科学中用于检测临界相变和拓扑突变。该方法的多尺度特性使其既能捕捉全局趋势又能定位微观变化，为动态点云分析提供了比传统距离度量更丰富的诊断工具。
