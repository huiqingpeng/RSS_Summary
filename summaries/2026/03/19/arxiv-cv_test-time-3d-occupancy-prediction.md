---
title: "Test-Time 3D Occupancy Prediction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2503.08485"
published: "2026-03-19"
summarized: "2026-03-19T16:23:55.334831"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了TT-Occ，一种新颖的测试时3D占据预测框架，通过增量构建、优化和体素化时序感知的3D高斯表示，在运行时集成视觉基础模型（VFMs）来实现无需训练的占据预测。该方法克服了传统自监督方法需要数百GPU小时训练且难以适应不同体素分辨率或新类别的局限，实现了任意分辨率体素化和开放词汇识别能力。

【方法概述 / Method】
TT-Occ采用3D高斯作为灵活的场景表示，从原始传感器流中增量构建并优化时序感知的3D高斯点云，并利用视觉基础模型的强大泛化能力进行几何推理和语义理解。该框架包含LiDAR-based和vision-centric两个变体，均无需任何网络训练或微调即可在测试时直接推理。

【实验结果 / Results】
在Occ3D-nuScenes和nuCraft基准测试上的大量实验表明，TT-Occ在不同体素分辨率设置下均显著优于计算成本高昂的自监督预训练方法，在无需训练的情况下实现了更优的占据预测性能。

【应用价值 / Applications】
TT-Occ可广泛应用于自动驾驶场景理解，支持实时灵活的3D环境感知；其任意分辨率体素化和开放词汇识别能力使其适用于快速部署到新场景、新车型以及需要动态调整感知精度的实际自动驾驶系统。
