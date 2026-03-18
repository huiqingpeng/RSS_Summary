---
title: "Multi-objective Optimization for Over-the-Air Federated Edge Learning-enabled Collaborative Integrated Sensing and Communications"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2603.15783"
published: "2026-03-18"
summarized: "2026-03-18T19:07:49.650802"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种新颖的多目标集成感知与通信（ISAC）框架，实现基于空中联邦边缘学习（OTA-FEEL）的协作无线感知。该框架支持感知与学习的多任务OTA聚合，利用上行信号同时服务于通信和目标感知双重目的。研究通过表征局部充分统计量、设计正交脉冲整形方法抑制干扰，并推导目标坐标的最优无偏估计，最终建立了多目标优化问题以同时最小化均方误差（MSE）和感知误差界，数值结果表明该框架能在不影响OTA-FEEL主任务性能的前提下提升感知精度。

【方法概述 / Method】
论文首先表征各边缘设备的局部充分统计量并建立其平稳性，提出一种新颖的正交脉冲整形方法通过匹配滤波抑制其他设备上行传输的干扰；然后将所有设备的联合似然函数最大化问题转化为各设备的分布式似然最大化问题，推导目标坐标的最优无偏估计，并利用克拉美-罗界（CRB）表征感知误差方差下界。

【实验结果 / Results】
数值结果表明，所提出的双用途OTA-FEEL赋能协作ISAC框架能够在不损害主OTA-FEEL任务性能的情况下提升感知精度；与传统单次协作感知方案受限于局部估计器平均误差不同，所提算法达到了所考虑问题的CRB下界。

【应用价值 / Applications】
该研究适用于需要同时进行分布式机器学习模型训练和目标感知的边缘计算场景，如智能交通系统中的车辆协同感知与模型更新、工业物联网中的设备状态监测与预测性维护，以及智慧城市中的多源数据融合与实时决策，实现了通信与感知资源的高效复用。
