---
title: "Fixed Anchors Are Not Enough: Dynamic Retrieval and Persistent Homology for Dataset Distillation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.24144"
published: "2026-03-18"
summarized: "2026-03-18T18:33:13.372664"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对解耦式数据集蒸馏（Decoupled Dataset Distillation）中静态锚点导致的拟合-复杂度差距和"拉向锚点"效应问题，提出了RETA框架。该框架通过动态检索连接（DRC）在教师特征空间中选择最优真实图像块，并利用持久拓扑对齐（PTA）基于持续同调理论正则化合成图像的拓扑结构。实验表明，RETA在CIFAR-100、Tiny-ImageNet和ImageNet-1K等多个基准上显著优于现有方法，在ImageNet-1K上使用ResNet-18达到64.3%的top-1准确率，较此前最优方法提升3.1%。

【方法概述 / Method】
RETA框架包含两个核心组件：动态检索连接（DRC）通过最小化拟合-复杂度分数，从预构建的真实图像池中动态选择最优图像块，并通过残差连接注入合成过程；持久拓扑对齐（PTA）则构建互k近邻特征图，计算连通分量和环路的持续同调图像，通过惩罚真实集与合成集之间的拓扑差异来缓解"拉向锚点"效应。

【实验结果 / Results】
RETA在多个标准基准上取得领先性能：在ImageNet-1K上使用ResNet-18、每类50张图像的条件下达到64.3% top-1准确率；该方法在CIFAR-100、Tiny-ImageNet及多个ImageNet子集上均一致超越各类基线方法，且在可比较的时间和内存开销下实现性能提升。

【应用价值 / Applications】
该研究适用于需要大规模数据集压缩的场景，如边缘设备模型训练、隐私保护数据发布、神经网络架构搜索加速以及持续学习中的记忆回放等，能够在保持模型泛化能力的同时显著降低存储和计算成本，对资源受限环境下的深度学习部署具有重要实践意义。
