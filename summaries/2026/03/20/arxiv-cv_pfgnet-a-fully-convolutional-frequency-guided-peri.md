---
title: "PFGNet: A Fully Convolutional Frequency-Guided Peripheral Gating Network for Efficient Spatiotemporal Predictive Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.20537"
published: "2026-03-20"
summarized: "2026-03-20T16:17:55.667642"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出PFGNet，一种用于时空预测学习（STPL）的全卷积网络框架。该网络受生物中心-周边组织结构和频率选择性信号处理的启发，通过像素级频率引导门控机制动态调节感受野，实现空间自适应的时空建模。PFGNet在多个基准数据集上达到或接近最优性能，同时显著降低参数量和计算量，且无需循环结构或注意力机制。

【方法概述 / Method】

PFGNet的核心是**周边频率门控（PFG）块**，该模块提取局部频谱特征，并通过可学习的中心抑制机制自适应融合多尺度大核周边响应，形成空间自适应的带通滤波器。为保持计算效率，所有大核卷积均分解为可分离的1D卷积（1×k后接k×1），将每通道计算复杂度从O(k²)降至O(2k)。

【实验结果 / Results】

在Moving MNIST、TaxiBJ、Human3.6M和KTH四个标准数据集上的实验表明，PFGNet以显著更少的参数量和FLOPs实现了SOTA或接近SOTA的预测性能。全卷积设计保证了完全并行计算能力，相比循环或混合架构具有更高的推理效率。

【应用价值 / Applications】

该研究为视频预测、交通流量预测、人体姿态预测等时空预测任务提供了高效轻量的解决方案。PFGNet的纯卷积架构特别适合边缘设备部署和实时应用场景，其频率引导的空间自适应机制为设计高效视觉模型提供了新思路。
