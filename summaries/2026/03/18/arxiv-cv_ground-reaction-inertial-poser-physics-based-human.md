---
title: "Ground Reaction Inertial Poser: Physics-based Human Motion Capture from Sparse IMUs and Insole Pressure Sensors"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16233"
published: "2026-03-18"
summarized: "2026-03-18T18:08:30.148462"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Ground Reaction Inertial Poser (GRIP)，一种仅使用四个可穿戴设备即可重建物理合理人体运动的方法。GRIP创新性地将IMU信号与足底压力数据相结合，并通过物理仿真器中的数字孪生人体模型来重建真实且物理一致的运动。实验表明，GRIP在全局姿态精度和物理一致性方面均优于现有的纯IMU及IMU-压力融合方法。

【方法概述 / Method】
GRIP包含两个核心模块：KinematicsNet从传感器数据估计人体姿态和速度；DynamicsNet则利用KinematicsNet预测与仿真人体状态之间的残差来控制物理仿真器中的人类模型。该方法通过物理仿真约束确保了运动的真实性和物理合理性。

【实验结果 / Results】
GRIP在所有评估数据集上均超越了现有的纯IMU和IMU-压力融合方法，实现了更高的全局姿态精度和更优的物理一致性。研究还构建了大规模数据集PRISM，包含同步IMU和鞋垫压力传感器的多样化人体运动数据，以支持模型训练和公平评估。

【应用价值 / Applications】
该技术可广泛应用于虚拟现实/增强现实、运动生物力学分析、康复医疗监测以及影视动画制作等领域。稀疏传感器配置（仅四个设备）使其具备良好的可穿戴性和实用性，而物理一致的运动重建能力对于需要真实人体动力学模拟的应用场景尤为重要。
