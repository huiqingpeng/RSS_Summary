---
title: "MRD: Multi-resolution Retrieval-Detection Fusion for High-Resolution Image Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.02906"
published: "2026-03-20"
summarized: "2026-03-20T16:15:44.996173"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对多模态大语言模型（MLLMs）理解高分辨率（HR）图像的挑战，提出了Multi-resolution Retrieval-Detection（MRD）框架。现有基于视觉检索增强生成（RAG）的方法存在物体碎片化导致的语义偏差、检索不完整以及背景干扰等问题。MRD通过多分辨率语义融合实现跨尺度语义一致性，并整合开放词汇目标检测（OVD）作为全局定位先验，在无需训练的情况下显著提升了MLLMs对高分辨率图像的理解能力，在单目标和多目标理解任务上均达到SOTA性能。

【方法概述 / Method】
MRD采用双视角融合策略：局部层面通过多分辨率语义融合机制，聚合不同尺度裁剪区域的语义信息以消除单分辨率偏差和物体碎片化问题；全局层面将开放词汇目标检测作为定位先验整合到统一框架中，提供物体级别的空间定位信息。该方法完全无需训练，可直接应用于现有MLLMs。

【实验结果 / Results】
实验在多个高分辨率图像基准测试上验证了MRD的有效性，涵盖多种MLLM架构。结果表明MRD在单目标理解和多目标理解任务上均取得了最先进的性能，显著优于现有的视觉RAG方法，有效缓解了物体碎片化和背景噪声干扰问题。

【应用价值 / Applications】
MRD可广泛应用于需要精细视觉理解的高分辨率图像分析场景，如遥感图像解译、医学影像诊断、工业质检和文档理解等领域。该框架的即插即用特性使其能够快速集成到现有的多模态大模型系统中，提升对高分辨率视觉内容的理解精度和可靠性。
