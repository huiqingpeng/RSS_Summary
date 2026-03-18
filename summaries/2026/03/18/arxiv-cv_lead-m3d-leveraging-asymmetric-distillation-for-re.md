---
title: "LeAD-M3D: Leveraging Asymmetric Distillation for Real-Time Monocular 3D Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.05663"
published: "2026-03-18"
summarized: "2026-03-18T18:30:20.154209"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了LeAD-M3D，一种无需额外传感器（如LiDAR）即可实现实时推理的单目3D目标检测器。该方法通过三个核心组件——非对称增强去噪蒸馏（A2D2）、3D感知一致匹配（CM₃D）和置信度门控3D推理（CGI₃D）——在KITTI、Waymo和Rope3D数据集上取得了最先进的精度，同时推理速度比此前高精度模型（如MonoDiff）快达3.6倍，证明了单目3D检测可以同时实现高保真度和实时性。

【方法概述 / Method】

LeAD-M3D采用非对称蒸馏策略，其中A2D2通过质量和重要性加权深度特征损失，将干净图像教师模型的几何知识迁移至MixUp噪声学生模型，增强深度推理能力；CM₃D通过将3D MGIoU整合到匹配分数中，优化预测与真实标签的分配策略；CGI₃D则通过将计算代价较高的3D回归限制在高置信度区域，实现推理加速。

【实验结果 / Results】

LeAD-M3D在KITTI和Waymo数据集上达到最先进的精度，并在Rope3D数据集上取得最佳汽车类别AP；与此前高精度模型相比，推理速度提升最高达3.6倍，在精度-效率权衡上建立了新的帕累托前沿。

【应用价值 / Applications】

该研究为自动驾驶、机器人导航等需要实时3D环境感知的应用提供了低成本解决方案，无需依赖昂贵的LiDAR传感器或立体相机，仅需单目摄像头即可实现高精度实时检测，具有重要的实际部署价值和商业化潜力。
