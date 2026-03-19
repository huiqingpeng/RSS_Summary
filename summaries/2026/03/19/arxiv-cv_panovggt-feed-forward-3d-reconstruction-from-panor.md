---
title: "PanoVGGT: Feed-Forward 3D Reconstruction from Panoramic Imagery"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17571"
published: "2026-03-19"
summarized: "2026-03-19T15:14:14.596384"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了PanoVGGT，首个专为全景图像设计的端到端前馈3D重建框架，能够同时预测相机位姿、深度图和3D点云。该模型通过球面感知位置编码和SO(3)旋转增强技术处理全景图像的非针孔畸变，并采用随机锚定策略解决全局坐标系模糊问题。此外，作者构建了大规模户外全景数据集PanoCity，实验表明PanoVGGT在精度和跨域泛化能力上均达到领先水平。

【方法概述 / Method】
PanoVGGT基于置换等变Transformer架构，引入球面感知位置编码以适配360°球面几何特性，并设计全景专用的三轴SO(3)旋转数据增强策略。针对全景重建中固有的全局坐标系不确定性，训练时采用随机锚定机制随机选取参考帧建立局部坐标系。

【实验结果 / Results】
PanoVGGT在自建的大规模户外数据集PanoCity及标准基准测试上均取得竞争性精度，展现出强鲁棒性和优异的跨域泛化能力。作为前馈网络，其单次前向传播即可完成多帧全景图像的联合位姿估计与稠密重建，推理效率显著高于传统优化方法。

【应用价值 / Applications】
该研究可直接应用于VR/AR内容生成、室内导航与机器人定位、自动驾驶环视感知等依赖全景视觉的场景。随着消费级全景相机（如Insta360、Ricoh Theta）的普及，PanoVGGT为快速、无需标定的三维场景理解提供了实用工具，降低了专业3D重建的技术门槛。
