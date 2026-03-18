---
title: "CLRNet: Targetless Extrinsic Calibration for Camera, Lidar and 4D Radar Using Deep Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15767"
published: "2026-03-18"
summarized: "2026-03-18T17:18:20.416140"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CLRNet，一种端到端的多模态深度学习网络，用于解决相机、激光雷达和4D雷达之间的外参标定问题。针对4D雷达数据稀疏导致的标定困难，该网络通过等距柱状投影、基于相机的深度图像预测、额外雷达通道以及共享特征空间和闭环损失函数等技术，实现了联合或成对的三传感器标定。在View-of-Delft和Dual-Radar数据集上的实验表明，该方法相比现有最先进方法将平移和旋转标定误差的中位数降低了至少50%，并具有良好的跨数据集域迁移能力。

【方法概述 / Method】
CLRNet采用端到端深度学习架构，整合等距柱状投影处理、相机深度预测网络、扩展雷达通道信息，并构建激光雷达与雷达的共享特征空间。网络引入闭环损失函数（loop closure loss）来约束多传感器间的几何一致性，支持灵活的三传感器联合标定或任意两两传感器之间的成对标定。

【实验结果 / Results】
在View-of-Delft和Dual-Radar数据集上进行的大量实验显示，CLRNet在标定精度上显著优于现有最先进方法，平移和旋转标定误差的中位数均减少50%以上。此外，跨数据集评估验证了该网络具备良好的域迁移能力，表明其在不同数据分布下的泛化性能。

【应用价值 / Applications】
该研究可广泛应用于自动驾驶和机器人感知系统中多传感器融合的前期标定环节，无需人工标定靶标即可实现相机-激光雷达-雷达的精确外参估计。其无目标（targetless）特性和深度学习方法降低了部署成本，提升了标定效率，适用于大规模车队运营和在线自标定场景。
