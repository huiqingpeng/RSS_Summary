---
title: "Points-to-3D: Structure-Aware 3D Generation with Point Cloud Priors"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18782"
published: "2026-03-20"
summarized: "2026-03-20T15:16:16.501780"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了 Points-to-3D，一种基于扩散模型的 3D 生成框架，通过利用点云先验实现几何可控的 3D 资产生成。该方法在 TRELLIS 潜在 3D 扩散模型的基础上，将纯噪声稀疏结构潜在初始化替换为点云先验引导的输入形式，并引入结构补全网络学习全局结构修复。实验表明，该方法在渲染质量和几何保真度上均优于现有最优基线方法，能够有效利用显式几何约束实现更精确的 3D 生成。

【方法概述 / Method】
Points-to-3D 基于 TRELLIS 潜在 3D 扩散模型，采用两阶段采样策略：首先使用结构补全网络进行全局结构修复，随后进行边界细化。该框架支持两种输入模式——来自 LiDAR 等主动传感器的精确点云，或从单张图像通过 VGGT 估计的点云。

【实验结果 / Results】
在物体和场景生成任务上的实验表明，Points-to-3D 在渲染质量和几何保真度方面均显著优于现有最先进基线方法。该方法能够有效保持输入点云可见区域的几何结构，同时补全缺失的全局几何信息。

【应用价值 / Applications】
该研究可广泛应用于自动驾驶、机器人感知和增强现实等领域，其中 LiDAR 点云易于获取但通常不完整。通过结合现成的点云先验，Points-to-3D 能够实现高质量、结构可控的 3D 场景重建与资产生成，降低了对完整 3D 扫描数据的依赖。
