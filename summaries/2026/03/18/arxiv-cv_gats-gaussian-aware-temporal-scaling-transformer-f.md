---
title: "GATS: Gaussian Aware Temporal Scaling Transformer for Invariant 4D Spatio-Temporal Point Cloud Representation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16154"
published: "2026-03-18"
summarized: "2026-03-18T18:07:00.131239"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GATS（Gaussian Aware Temporal Scaling Transformer），一种用于不变性4D时空点云表示的新型双不变框架。该框架通过不确定性引导的高斯卷积（UGGC）和时序缩放注意力（TSA）两个互补模块，分别解决点云分布不确定性和时序尺度偏差问题。在主流基准测试MSR-Action3D、NTU RGBD和Synthia4D上，该方法取得了显著的性能提升（分别提升6.62%、1.4%和1.8%），为4D点云视频理解提供了更高效、更鲁棒的解决方案。

【方法概述 / Method】
GATS框架包含两个核心模块：不确定性引导的高斯卷积（UGGC）将局部高斯统计与不确定性感知门控机制融入点卷积，实现密度变化、噪声和遮挡下的鲁棒邻域聚合；时序缩放注意力（TSA）引入可学习的缩放因子归一化时间距离，确保不同帧率下的帧分割不变性和一致的速度估计。两个模块协同工作，时序缩放先于高斯估计归一化时间间隔，而高斯建模增强对不规则分布的鲁棒性。

【实验结果 / Results】
GATS在多个主流基准上取得显著性能提升：MSR-Action3D数据集上准确率提升6.62%，NTU RGBD数据集上提升1.4%，Synthia4D数据集上mIoU提升1.8%。实验结果表明该方法相比基于Transformer的对比方法具有更优的准确性、鲁棒性和可扩展性。

【应用价值 / Applications】
该研究可广泛应用于智能机器人的动态环境感知、自动驾驶中的3D目标跟踪与行为预测、人机交互中的动作识别，以及增强/虚拟现实中的实时场景理解等领域。GATS通过解决帧率变化和点云不规则性带来的核心挑战，为实际部署中面临多样化传感器配置和复杂环境条件的4D视觉系统提供了可靠的技术基础。
