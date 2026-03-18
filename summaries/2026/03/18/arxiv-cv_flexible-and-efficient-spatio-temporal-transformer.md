---
title: "Flexible and Efficient Spatio-Temporal Transformer for Sequential Visual Place Recognition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.04282"
published: "2026-03-18"
summarized: "2026-03-18T18:27:28.596776"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对序列视觉地点识别（Seq-VPR）任务中现有方法在灵活性、推理速度和内存效率方面的不足，提出了Adapt-STformer方法。该方法基于新颖的循环可变形Transformer编码器（Recurrent-DTE），通过迭代循环机制融合多帧时序信息，实现了对可变序列长度的自然支持。在Nordland、Oxford和NuScenes数据集上的实验表明，该方法在召回率提升最高达17%的同时，序列提取时间减少36%，内存使用降低35%。

【方法概述 / Method】
Adapt-STformer的核心是Recurrent Deformable Transformer Encoder（Recurrent-DTE），该编码器采用迭代循环机制逐步融合多个连续帧的时空特征，而非传统的一次性处理整个序列。这种设计使得模型能够动态适应不同的序列长度，避免了为固定长度重新训练或调整网络结构的需求。

【实验结果 / Results】
在三个标准数据集（Nordland、Oxford、NuScenes）上的综合评估显示，Adapt-STformer相比最优对比基线实现了显著的性能提升：召回率最高提升17%，同时推理效率大幅改善——序列特征提取时间减少36%，GPU内存占用降低35%，在保持高精度的同时满足了实时应用的需求。

【应用价值 / Applications】
该研究对自动驾驶和机器人导航中的视觉定位系统具有重要价值，特别是在计算资源受限的边缘设备上需要实时处理可变长度视频序列的场景。其高效灵活的设计使得Seq-VPR模型能够部署于从高性能服务器到低功耗嵌入式平台的多种硬件环境，推动了视觉地点识别技术的实际落地应用。
