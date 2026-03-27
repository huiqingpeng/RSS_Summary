---
title: "OpenCap Monocular: 3D Human Kinematics and Musculoskeletal Dynamics from a Single Smartphone Video"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24733"
published: "2026-03-27"
summarized: "2026-03-28T07:16:16.265703"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了OpenCap Monocular，一种仅需单个智能手机视频即可估计3D人体骨骼运动学（kinematics）和肌肉骨骼动力学（kinetics）的算法。该方法通过优化单目姿态估计模型（WHAM）的输出，结合生物力学约束的骨骼模型和物理仿真与机器学习，实现了对关节运动和外力的精确估计。验证实验表明，该方法在旋转自由度上平均绝对误差为4.8°、骨盆平移误差为3.4 cm，显著优于纯回归的计算机视觉基线方法，且已通过手机应用、网页应用和云端计算平台免费开放使用。

【方法概述 / Method】
OpenCap Monocular首先利用WHAM模型从单目视频获取初始3D人体姿态估计，然后通过优化算法对其进行精修；随后将优化后的姿态映射到生物力学约束的骨骼模型上计算运动学参数，最后结合物理仿真和机器学习方法估计地面反作用力和关节力矩等动力学参数。

【实验结果 / Results】
在行走、深蹲和坐-站转换任务中，OpenCap Monocular的旋转精度比纯回归基线提升48%（p=0.036），平移精度提升69%（p<0.001）；行走时的地面反作用力估计精度达到或超过此前双相机OpenCap系统水平。该方法还能以临床有意义的精度估计与虚弱和膝骨关节炎相关的关键动力学指标，如坐-站转换时的膝伸力矩和行走时的膝内收力矩。

【应用价值 / Applications】
OpenCap Monocular通过智能手机即可实现免费、可扩展的生物力学评估，无需昂贵的实验室设备和专业人员，可广泛应用于临床运动功能监测、老年虚弱评估、膝骨关节炎治疗决策和康复效果追踪等场景，有望推动移动健康（mHealth）和远程医疗中的个性化运动医学发展。
