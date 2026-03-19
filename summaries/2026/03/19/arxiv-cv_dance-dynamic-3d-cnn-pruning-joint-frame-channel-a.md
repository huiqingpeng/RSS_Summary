---
title: "DANCE: Dynamic 3D CNN Pruning: Joint Frame, Channel, and Feature Adaptation for Energy Efficiency on the Edge"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17275"
published: "2026-03-19"
summarized: "2026-03-19T15:07:26.793270"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DANCE，一种细粒度、输入感知的3D CNN动态剪枝框架，用于在边缘设备上最大化能效且对性能影响极小。该方法采用两步策略：首先通过激活变异性放大（AVA）重新训练模型以增加神经元激活幅度的方差，然后通过自适应激活剪枝（AAP）训练轻量级控制器网络，根据第一层输出动态剪枝帧、通道和特征。硬件验证表明，该方法在NVIDIA Jetson Nano和Qualcomm Snapdragon 8 Gen 1平台上分别实现1.37倍和2.22倍加速，能效比现有最优方法提升高达1.47倍。

【方法概述 / Method】
DANCE采用两阶段方法：第一阶段（AVA）通过重新训练3D CNN模型，放大神经元激活幅度的变异性，为多样化输入场景下的剪枝决策创造条件；第二阶段（AAP）训练一个轻量级激活控制器网络，该网络基于首层输出统计信息，为每一层动态决定帧、通道和特征的剪枝策略。

【实验结果 / Results】
该方法通过在卷积层内引入稀疏性，显著减少了乘加运算（MAC）和内存访问次数。在NVIDIA Jetson Nano GPU上实现1.37倍加速，在Qualcomm Snapdragon 8 Gen 1平台上实现2.22倍加速，能效相比当前最先进方法提升最高达1.47倍，且对模型性能影响可忽略不计。

【应用价值 / Applications】
DANCE适用于边缘设备上的实时视频分析和图像处理任务，如智能监控、自动驾驶和移动AR/VR应用，能够在严格的功耗约束下实现高效的深度学习推理。该框架为资源受限环境下的3D CNN部署提供了实用的能效优化方案，有助于延长电池寿命并降低散热需求。
