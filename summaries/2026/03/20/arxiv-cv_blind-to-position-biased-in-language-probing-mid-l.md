---
title: "Blind to Position, Biased in Language: Probing Mid-Layer Representational Bias in Vision-Language Encoders for Zero-Shot Language-Grounded Spatial Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.23098"
published: "2026-03-20"
summarized: "2026-03-20T16:13:36.429335"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究揭示了视觉-语言编码器（VLEs）中层表示中存在的两种耦合偏差：最终层多模态嵌入过度关注全局语义对齐，导致视觉嵌入对位置线索敏感度不足，以及多语言文本嵌入在共享空间中形成语言依赖的几何偏移。通过逐层分析，作者发现中层表示可用于构建空间映射，将零样本指代图像分割（RIS）性能提升1-7 mIoU；同时利用混合语言中层嵌入可进一步增强空间定位准确性（+7-8 mIoU和IoU@50），并改善零样本文本到图像检索任务表现。

【方法概述 / Method】

作者采用逐层探测方法系统分析VLE各层表示，重点关注中层保留的位置和语言特定信息；基于发现的中层空间信息，构建空间映射（spatial map）用于改进零样本RIS；此外，通过混合多语言中层嵌入来利用语言依赖的几何偏移效应，以增强空间定位能力。

【实验结果 / Results】

在九个RefCOCO基准测试上，基于中层空间映射的方法实现零样本RIS性能提升1-7 mIoU；混合语言中层嵌入策略带来额外的7-8 mIoU和IoU@50增益，同时该方法也提升了零样本文本到图像检索任务的性能；值得注意的是，混合语言方法虽有效但增加了推理成本。

【应用价值 / Applications】

本研究为改进零样本视觉-语言任务（如指代图像分割和文本到图像检索）提供了无需额外训练的新途径，可直接应用于现有VLE架构；揭示的中层表示特性有助于开发更高效的模型解释和调试工具；同时，多语言嵌入的发现为跨语言视觉-语言模型设计和多语言场景理解提供了新思路。
