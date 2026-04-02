---
title: "Unsupervised 4D Flow MRI Velocity Enhancement and Unwrapping Using Divergence-Free Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00205"
published: "2026-04-02"
summarized: "2026-04-03T07:18:27.737204"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种无监督的无散度和混叠神经网络（DAF-FlowNet），用于四维血流磁共振成像（4D Flow MRI），能够联合增强噪声速度场并校正相位卷折伪影。该方法通过将速度参数化为向量势的旋度，从结构上保证质量守恒，避免了显式的散度惩罚调参。在合成主动脉4D Flow MRI数据及10例肥厚型心肌病患者数据集上，DAF-FlowNet在速度误差、方向误差和散度控制等指标上均优于现有技术，同时保留了精细的血流特征并改善了内部血流一致性。

【方法概述 / Method】

DAF-FlowNet采用物理启发的神经网络架构，将速度场表示为向量势的旋度，从而隐式满足无散度条件（质量守恒）。该方法设计了余弦数据一致性损失函数，可直接从卷折的相位图像中同时实现去噪和解卷折，无需地面真值标签进行监督训练。

【实验结果 / Results】

在计算流体力学生成的合成主动脉数据中，DAF-FlowNet相比最优对比方法实现了高达11%的速度归一化均方根误差降低、11%的方向误差降低和44%的散度降低。对于解卷折任务，在峰值速度与速度编码比为1.4和2.1时，残余卷折体素分别降至0.18%和5.2%。在噪声与混叠并存场景下，单阶段DAF-FlowNet较最先进序贯流程误差降低达15%。

【应用价值 / Applications】

该研究为心血管4D Flow MRI提供了统一的速度增强与相位解卷折框架，可提升临床血流测量的可靠性，特别适用于肥厚型心肌病等心血管疾病的精细血流动力学评估。该方法符合4D Flow MRI共识指南的质量要求，有望改善主动脉和肺动脉质量守恒分析中的跨平面流量偏差问题。
