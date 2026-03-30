---
title: "SPECTRA: An Efficient Spectral-Informed Neural Network for Sensor-Based Activity Recognition"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26482"
published: "2026-03-30"
summarized: "2026-03-31T07:24:52.083224"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SPECTRA，一种面向边缘部署的频谱感知神经网络架构，用于基于传感器的人类活动识别（HAR）。该架构通过整合短时傅里叶变换（STFT）、深度可分离卷积和通道自注意力机制，在严格资源约束下有效捕获频谱-时序依赖关系。实验表明，SPECTRA在五个公开HAR数据集上达到了与更大规模的CNN-LSTM和Transformer模型相当或接近的精度，同时显著降低了参数量、延迟和能耗，并成功部署于Google Pixel 9智能手机和STM32L4微控制器。

【方法概述 / Method】
SPECTRA采用"部署优先"的协同设计策略，核心包括：使用STFT提取频谱特征以显式建模信号的频域结构；采用深度可分离卷积降低计算复杂度；引入通道自注意力机制捕获跨通道的频谱-时序依赖；配合轻量级双向GRU与注意力池化，以低成本汇总窗口内动态特征。

【实验结果 / Results】
在五个公开HAR数据集上，SPECTRA在精度上匹配或接近CNN-LSTM和Transformer基线模型，同时实现大幅轻量化：参数量、推理延迟和能耗均显著降低。端到端部署验证于Google Pixel 9智能手机和STM32L4微控制器，证明了其实时、隐私保护和高效推理的可行性。

【应用价值 / Applications】
该研究适用于普适计算中的实时传感器应用，如可穿戴设备健康监测、智能家居交互和工业物联网场景，能够在保障用户隐私的低延迟边缘端实现高效人体活动识别，为资源受限设备上的深度学习部署提供了实用解决方案。
