---
title: "Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18218"
published: "2026-03-20"
summarized: "2026-03-20T15:06:48.264960"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种面向月球表面实时建图的框架，将语义分割与深度估计模型集成到3D高斯泼溅（3DGS）表示中。研究在LuPNT合成数据集上基准测试了多种模型，最终选用基于门控循环单元（GRU）的立体深度估计模型和卷积神经网络语义分割模型。该框架在120米路径重建中实现了约3厘米的几何高度精度，优于无LiDAR的传统点云基线，为月球探测任务提供了高精度、可实时优化的地图表示。

【方法概述 / Method】
论文采用3D高斯泼溅作为地图表示，结合GRU-based立体深度估计网络进行稠密深度预测，并使用CNN进行语义分割。通过使用地面真值位姿将局部场景理解与全局状态估计解耦，构建了一个完整的实时建图流水线。

【实验结果 / Results】
在合成月球数据集上，该方法在120米行驶路径的重建中达到了约3厘米的几何高度精度，显著优于无LiDAR的传统点云基线方法。重建的3DGS地图支持新视角合成，并具备联合地图与位姿优化的扩展潜力。

【应用价值 / Applications】
该研究可直接应用于未来月球探测任务的自主导航与建图系统，为在弱纹理、高对比度光照及计算资源受限等挑战性条件下的实时感知提供解决方案。其3DGS表示还可作为完整SLAM系统的基础，支持在线地图优化与语义增强的环境理解。
