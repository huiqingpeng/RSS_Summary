---
title: "BEV-SLD: Self-Supervised Scene Landmark Detection for Global Localization with LiDAR Bird's-Eye View Images"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17159"
published: "2026-03-19"
summarized: "2026-03-19T15:06:00.327522"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了BEV-SLD，一种基于场景地标检测（SLD）概念的LiDAR全局定位方法。与场景无关的传统方法不同，该自监督方法利用鸟瞰图（BEV）图像以预设空间密度发现场景特定模式并将其作为地标。通过一致性损失将可学习的全局地标坐标与每帧热力图对齐，实现了场景中一致的地标检测。该方法在校园、工业和森林等多种环境中展现出鲁棒的定位性能，并与最先进方法相比取得了优异表现。

【方法概述 / Method】
BEV-SLD采用自监督学习框架，从LiDAR点云生成的BEV图像中自动学习场景特定的地标表示。核心创新在于设计了一致性损失函数，将全局可学习的地标坐标与每帧预测的热力图进行对齐，从而确保同一地标在不同观测视角下保持检测一致性。

【实验结果 / Results】
实验在多种挑战性环境（校园、工业区和森林）中进行验证，结果表明BEV-SLD在全局定位任务中表现出强鲁棒性。与现有最先进方法相比，该方法在定位精度和场景泛化能力方面均取得显著提升。

【应用价值 / Applications】
该研究适用于自动驾驶、机器人导航和无人机定位等需要全局位姿估计的应用场景。特别是在GPS拒止或特征稀疏的复杂户外环境（如森林、工业设施）中，BEV-SLD提供了一种无需人工标注、可自适应场景特征的可靠定位解决方案。
