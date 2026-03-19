---
title: "TrackDeform3D: Markerless and Autonomous 3D Keypoint Tracking and Dataset Collection for Deformable Objects"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17068"
published: "2026-03-19"
summarized: "2026-03-19T15:04:40.189052"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了TrackDeform3D，一个低成本且自主的框架，仅使用RGB-D相机即可收集可变形物体的3D数据集。该方法能够识别3D关键点并稳健跟踪其轨迹，通过引入运动一致性约束生成时间平滑且几何连贯的数据。实验表明，该方法在多种物体类别上均优于现有最先进的跟踪方法，并基于此框架构建了一个包含6个可变形物体、总计110分钟轨迹数据的大规模高质量数据集。

【方法概述 / Method】

TrackDeform3D采用无标记（markerless）的RGB-D感知方案，结合运动一致性约束来实现3D关键点的检测与跟踪。该方法通过优化关键点的时序轨迹，确保几何一致性和时间平滑性，从而避免传统方法中劳动密集型标注或昂贵动作捕捉设备的需求。

【实验结果 / Results】

与多种最先进的跟踪方法相比，TrackDeform3D在几何精度和跟踪准确性方面均表现出一致的改进。利用该框架，研究团队成功采集了一个大规模数据集，涵盖6类不同可变形物体，累计110分钟的轨迹数据，为后续研究提供了宝贵的基准资源。

【应用价值 / Applications】

该研究可广泛应用于可变形物体的动力学建模、运动规划等下游任务，特别适用于机器人操作、虚拟现实和增强现实中的柔性物体交互。其低成本、自主化的数据采集方案显著降低了3D数据集构建的门槛，有助于推动可变形物体感知领域的标准化基准建立和算法发展。
