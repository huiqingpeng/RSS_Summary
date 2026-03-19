---
title: "SpiderCam: Low-Power Snapshot Depth from Differential Defocus"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17910"
published: "2026-03-19"
summarized: "2026-03-19T16:18:19.263068"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SpiderCam，一种基于FPGA的快照式散焦深度相机，能够以32.5 FPS的实时速度生成480×400的稀疏深度图，工作范围52 cm，总功耗仅624 mW。该系统通过同时捕获两幅不同焦平面的图像，并在低功耗FPGA上实现差分散焦深度估计（DfDD）算法。作者针对低功耗传感器带来的挑战改进了DfDD算法，并设计了流式内存本地化的实现方案，首次实现了亚瓦特级功耗的被动式FPGA三维相机。

【方法概述 / Method】
SpiderCam采用定制双焦平面相机硬件同时获取同一场景的两幅不同聚焦图像，利用差分散焦深度估计（DfDD）原理计算深度。算法层面针对低功耗传感器的噪声特性进行了优化，硬件层面采用SystemVerilog实现流式处理架构，在无法存储完整图像对的极小FPGA资源约束下完成实时深度计算。

【实验结果 / Results】
系统在480×400分辨率下达到32.5 FPS的实时处理速度，有效工作距离为52 cm，总系统功耗为624 mW（首次实现亚瓦特级被动式FPGA深度相机）。该功耗指标显著优于现有文献中的同类FPGA深度相机方案，证明了低功耗嵌入式深度感知的技术可行性。

【应用价值 / Applications】
SpiderCam适用于电池供电的边缘设备和物联网场景，如微型无人机导航、可穿戴AR/VR设备、机器人避障等需要实时低功耗深度感知的应用。其亚瓦特功耗特性使其特别适合长期部署的能量受限环境，为移动平台和嵌入式系统提供了高效的被动式三维感知解决方案。
