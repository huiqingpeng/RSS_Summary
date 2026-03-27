---
title: "ReDiPrune: Relevance-Diversity Pre-Projection Token Pruning for Efficient Multimodal LLMs"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24680"
published: "2026-03-27"
summarized: "2026-03-28T07:14:31.129671"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了ReDiPrune，一种无需训练的token剪枝方法，用于提升多模态大语言模型的计算效率。该方法在视觉-语言投影器之前对视觉token进行剪枝，直接利用视觉编码器输出的丰富特征，而非压缩后的表示。ReDiPrune通过联合考虑文本条件相关性和最大-最小多样性的轻量级评分规则选择信息性token，在多个图像和视频基准测试中实现了准确率与效率的优化平衡，例如在EgoSchema数据集上仅保留15%视觉token即可提升2.0%绝对准确率，同时降低6倍以上计算量。

【方法概述 / Method】

ReDiPrune采用"预投影"剪枝策略，在视觉编码器输出后、投影器之前插入token选择模块，利用原始高维视觉特征进行决策。每个视觉token的评分由两部分组成：基于查询文本的CLIP风格相关性分数，以及基于最大-最小距离的核心集多样性分数，最终选择得分最高的token子集送入后续模块。

【实验结果 / Results】

在4个视频基准和5个图像基准上的实验表明，ReDiPrune在多种多模态LLM架构上均有效。具体而言，使用LLaVA-NeXT-Video-7B在EgoSchema上保留15% token时，准确率提升2.0%且TFLOPs降低超过6倍；该方法作为即插即用模块，无需重新训练或修改架构即可部署。

【应用价值 / Applications】

ReDiPrune适用于需要高效处理高分辨率图像或长视频的多模态AI系统，如实时视觉问答、视频理解、自动驾驶感知等场景。其训练无关特性使其可快速集成到现有商用多模态模型中，显著降低推理成本的同时提升或保持任务性能，对边缘设备部署和大规模服务具有重要实用价值。
