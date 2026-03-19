---
title: "Look Before You Fuse: 2D-Guided Cross-Modal Alignment for Robust 3D Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2507.16861"
published: "2026-03-19"
summarized: "2026-03-19T16:25:26.253250"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对自动驾驶中LiDAR与相机特征的空间错位问题，提出了一种2D引导的跨模态对齐方法。核心发现是投影误差并非随机分布，而是高度集中于物体-背景边界区域，而2D检测器能够可靠识别这些区域。基于该洞察，作者设计了三阶段框架（PGDC、DAGF、SGDM）实现预对齐融合，在nuScenes验证集上达到71.5% mAP和73.6% NDS的SOTA性能，在Argoverse 2上取得41.7% mAP。

【方法概述 / Method】
论文提出Prior Guided Depth Calibration（PGDC）利用2D先验缓解局部错位并保留正确的跨模态特征对；Discontinuity Aware Geometric Fusion（DAGF）抑制残余噪声并显式增强物体-背景边界的深度突变；Structural Guidance Depth Modulator（SGDM）通过门控注意力机制高效融合对齐的深度与图像特征，形成"先对齐后融合"的流水线。

【实验结果 / Results】
在nuScenes验证集上，该方法以71.5% mAP和73.6% NDS超越现有方法达到SOTA；在Argoverse 2验证集上取得41.7% mAP的竞争力表现。实验表明2D引导的对齐策略有效解决了由标定误差和卷帘快门导致的投影误差问题。

【应用价值 / Applications】
该方法可直接部署于自动驾驶车辆的3D感知系统，提升多传感器融合在复杂场景（如标定退化、高速运动）下的鲁棒性。通过利用成熟的2D检测技术指导3D融合，降低了高精度传感器标定的依赖，具有工程实用价值和成本优化潜力。
