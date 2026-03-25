---
title: "A Multi-Modal CNN-LSTM Framework with Multi-Head Attention and Focal Loss for Real-Time Elderly Fall Detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22313"
published: "2026-03-25"
summarized: "2026-03-26T07:09:51.269441"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对全球老龄化加剧背景下老年人跌倒检测的需求，提出了一种名为MultiModalFallDetector的多模态深度学习框架。该框架融合了三轴加速度计、陀螺仪和四通道生理信号，通过多尺度CNN特征提取器、多头自注意力机制和Focal Loss等多项创新，在SisFall数据集上实现了98.7%的F1分数和99.4%的AUC-ROC，显著优于传统机器学习和标准深度学习方法。模型在边缘设备上保持低于50ms的推理延迟，证实了其在老年护理场景中实时部署的可行性。

【方法概述 / Method】
该研究采用CNN-LSTM架构作为基础框架，其中多尺度CNN用于捕获不同时间分辨率的运动动态特征，LSTM层处理时序依赖关系。核心创新包括引入多头自注意力机制实现动态时间加权、采用Focal Loss解决类别不平衡问题、设计辅助活动分类任务进行正则化，以及从UCI HAR数据集到SisFall数据集的迁移学习策略。

【实验结果 / Results】
在包含60-85岁老年人真实模拟跌倒试验的SisFall数据集上，该框架取得了F1-score 98.7%、Recall 98.9%和AUC-ROC 99.4%的优异性能。实验结果表明，该方法显著优于传统机器学习方法和标准深度学习基线，同时模型在边缘设备上的推理延迟低于50毫秒，满足实时性要求。

【应用价值 / Applications】
该研究可直接应用于可穿戴设备的老年健康监测系统，实现居家和社区环境中的实时跌倒检测与预警。其低延迟特性支持边缘计算部署，有助于降低医疗机构监护成本、缩短应急响应时间，对提升老年人独立生活安全和质量具有重要社会价值，同时为多模态生理信号融合在智能医疗领域的应用提供了可扩展的技术范式。
