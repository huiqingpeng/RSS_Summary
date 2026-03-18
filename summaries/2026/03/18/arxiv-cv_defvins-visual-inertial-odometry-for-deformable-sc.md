---
title: "DefVINS: Visual-Inertial Odometry for Deformable Scenes"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.00702"
published: "2026-03-18"
summarized: "2026-03-18T19:06:51.688076"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了DefVINS，首个面向可变形场景的视觉-惯性里程计（VIO）系统，解决了传统VIO刚性假设在变形环境中的失效问题。该方法将里程计状态分解为刚性IMU锚定分量与基于嵌入变形图的非刚性场景形变，并首次发布了真实可变形场景VIO基准数据集VIMandala。理论分析揭示了惯性测量如何约束相机运动并使原本不可观的模态变得可识别，实验表明DefVINS在合成与真实基准上均优于刚性VIO和非刚性视觉里程计基线。

【方法概述 / Method】

DefVINS采用双分量状态建模：刚性部分由IMU积分锚定，非刚性部分通过嵌入变形图（embedded deformation graph）表示场景形变。基于可观性分析，设计了基于条件数的激活策略，在激励不足时避免病态更新，确保数值稳定性。

【实验结果 / Results】

在合成Drunkard's基准（扩展IMU仿真）和真实VIMandala基准上的评估显示，DefVINS显著优于传统刚性VIO方法（有效抑制位姿漂移）和非刚性视觉里程计基线（避免局部非刚性运动过拟合），验证了IMU锚定策略在可变形场景中的有效性。

【应用价值 / Applications】

该研究适用于医疗内窥镜导航、软体机器人交互、弹性材料操作等可变形环境场景，为需要同时估计相机位姿和动态场景形变的应用提供了首个鲁棒的视觉-惯性解决方案，填补了该领域基准数据集的空白。
