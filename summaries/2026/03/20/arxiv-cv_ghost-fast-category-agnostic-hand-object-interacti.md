---
title: "GHOST: Fast Category-agnostic Hand-Object Interaction Reconstruction from RGB Videos using Gaussian Splatting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18912"
published: "2026-03-20"
summarized: "2026-03-20T15:17:42.593682"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出GHOST（Gaussian Hand-Object Splatting），首个基于2D高斯溅射的快速、类别无关的手-物交互重建框架。该方法将手和物体均表示为稠密、视角一致的高斯圆盘，通过三项关键创新——几何先验检索与一致性损失、抓取感知对齐机制、以及手部感知背景损失——解决了遮挡补全、物理一致接触和手部遮挡区域处理等核心挑战。GHOST在单目RGB视频上实现了完整、物理一致且可动画化的重建，速度比现有类别无关方法快一个数量级，在ARCTIC、HO3D及野外数据集上均达到最先进的3D重建精度和2D渲染质量。

【方法概述 / Method】
GHOST采用2D高斯溅射作为统一表示，将手和物体建模为可微分的各向异性高斯圆盘集合。方法核心包含三个技术创新：（1）利用几何先验数据库检索相似形状补全遮挡区域，并施加一致性约束；（2）基于抓取姿态估计的显式接触约束，联合优化手部平移和物体尺度；（3）设计手部感知掩码，避免对合理手部遮挡区域施加错误的背景重建损失。

【实验结果 / Results】
在ARCTIC和HO3D基准测试中，GHOST在3D重建精度（Chamfer距离、F-score）和2D渲染质量（PSNR、SSIM）上均超越现有类别无关方法，同时推理速度提升10倍以上。定性实验显示，该方法能有效处理复杂遮挡、生成物理合理的接触区域，并支持后续动画驱动。在野外视频上的泛化实验进一步验证了方法的鲁棒性。

【应用价值 / Applications】
GHOST可广泛应用于AR/VR中的真实手部交互模拟、机器人灵巧操作学习与仿真、以及具身智能中的交互数据生成。其类别无关特性使其无需预先定义物体模板即可处理新物体，而高计算效率（实时或近实时）支持在线应用，为构建大规模交互数据集和沉浸式虚拟环境提供了实用工具。
