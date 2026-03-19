---
title: "KGS-GCN: Enhancing Sparse Skeleton Sensing via Kinematics-Driven Gaussian Splatting and Probabilistic Topology for Action Recognition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16943"
published: "2026-03-19"
summarized: "2026-03-19T14:21:45.406858"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出KGS-GCN，一种用于基于稀疏骨架动作识别的图卷积网络，通过运动学驱动的高斯溅射（KGS）将离散关节点转换为连续生成表示，解决传感器数据稀疏性问题；同时采用基于Bhattacharyya距离的概率拓扑构建方法，突破预定义物理拓扑的刚性约束，自适应建模潜在长程依赖关系。实验表明该方法显著增强了复杂时空动态建模能力，为低质量传感器数据提供了鲁棒解决方案。

【方法概述 / Method】
该方法包含两个核心模块：运动学驱动的高斯溅射模块利用瞬时关节速度向量动态构建各向异性协方差矩阵，将稀疏骨架序列渲染为富含时空语义的多视角连续热图；概率拓扑构建方法通过量化关节高斯分布间的Bhattacharyya距离统计相关性，生成自适应先验邻接矩阵。最终通过视觉上下文门控机制，将渲染的视觉特征自适应调制到GCN主干网络。

【实验结果 / Results】
论文指出KGS-GCN显著提升了复杂时空动态的建模能力，通过解决稀疏输入的固有局限性，为处理低保真传感器数据提供了鲁棒解决方案（注：原文未提供具体数据集上的定量精度指标）。

【应用价值 / Applications】
该研究为人机交互和智能监控等传感器系统提供了实用途径，能够提升真实世界感知应用中的感知可靠性，特别适用于当前传感器设备生成稀疏骨架数据的实际场景，为低质量传感器数据的鲁棒处理建立了可行方案。
