---
title: "ANTS: Adaptive Negative Textual Space Shaping for OOD Detection via Test-Time MLLM Understanding and Reasoning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.03951"
published: "2026-03-18"
summarized: "2026-03-18T18:27:13.012449"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种名为ANTS（Adaptive Negative Textual Space）的新方法，通过利用多模态大语言模型（MLLM）的理解与推理能力，自适应地构建负文本空间以增强分布外（OOD）检测。该方法针对远OOD场景，通过缓存历史测试中的疑似OOD图像并由MLLM生成描述性负标签；针对近OOD场景，则通过缓存与测试图像视觉相似的ID类别子集，生成语义相近的负标签以减少假阴性。实验表明，ANTS在ImageNet基准上将FPR95降低了3.1%，达到新的最先进水平，且无需训练、支持零样本推理。

【方法概述 / Method】

ANTS采用测试时MLLM理解与推理机制，动态构建两类负文本空间：一是基于缓存的疑似OOD图像生成精确描述OOD分布的负句子；二是基于视觉相似的ID类别子集，通过MLLM推理生成语义相近的负标签。最终通过自适应加权分数平衡两类负空间，使方法能够灵活应对近OOD与远OOD的不同任务设定。

【实验结果 / Results】

在ImageNet基准数据集上，ANTS显著将FPR95指标降低3.1%，创下OOD检测的新最优性能。该方法无需任何训练过程，以零样本方式实现，展现出良好的可扩展性与实用性。

【应用价值 / Applications】

ANTS可广泛应用于开放环境下的视觉识别系统安全增强，如自动驾驶中的异常物体检测、医学影像中的未知病变识别，以及内容审核中的新型违规内容发现等场景。其训练无关、零样本的特性使其易于部署到现有MLLM架构中，为实际应用提供高效且可扩展的OOD检测解决方案。
