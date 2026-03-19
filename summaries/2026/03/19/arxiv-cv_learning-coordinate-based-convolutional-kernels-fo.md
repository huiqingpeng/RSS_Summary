---
title: "Learning Coordinate-based Convolutional Kernels for Continuous SE(3) Equivariant and Efficient Point Cloud Analysis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17538"
published: "2026-03-19"
summarized: "2026-03-19T15:13:19.505439"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种名为ECKConv（Equivariant Coordinate-based Kernel Convolution）的新型卷积方法，用于解决3D点云分析中的SE(3)等变性与计算可扩展性之间的权衡问题。该方法基于双陪集空间（double coset space）中的核域设计，利用坐标网络（coordinate-based networks）实现显式核函数建模，从而在保证严格SE(3)等变性的同时提升学习能力和内存效率。实验表明，ECKConv在分类、位姿配准、部件分割和大规模语义分割等多样化点云任务上均优于现有最先进的等变方法。

【方法概述 / Method】

ECKConv采用交织子（intertwiner）框架，将卷积核定义在双陪集空间上以获得SE(3)等变性；通过坐标网络（如MLP）显式参数化核函数，替代传统的离散核或预定义基函数，实现连续域上的灵活核学习。这种设计避免了昂贵的群积分运算，同时保持了严格的数学等变性保证。

【实验结果 / Results】

ECKConv在多个基准测试中展现出优异性能：在ModelNet40分类任务上达到领先水平，在7Scenes位姿配准中实现高精度估计，在ShapeNet部件分割和大规模语义分割（如S3DIS、ScanNet）中均取得竞争力或最优结果。关键的是，该方法在保持严格SE(3)等变性的同时，内存占用显著低于现有等变网络，支持大规模点云处理。

【应用价值 / Applications】

ECKConv适用于需要旋转等变性的机器人感知、自动驾驶和增强现实等场景，特别是在处理大规模室内/室外场景扫描时具有显著优势。其高效内存特性使复杂等变网络可部署于资源受限设备，而严格的数学等变性保证了对任意旋转输入的稳健预测，提升了系统在真实环境中的可靠性。
