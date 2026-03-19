---
title: "ASAP: Attention-Shift-Aware Pruning for Efficient LVLM Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14549"
published: "2026-03-19"
summarized: "2026-03-19T14:20:03.397879"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出ASAP（Attention-Shift-Aware Pruning），一种针对大型视觉语言模型（LVLMs）的高效推理加速方法。该方法通过动态双向软注意力掩码缓解LVLMs固有的"注意力偏移"现象，并引入加权软合并机制减少视觉token的语义冗余。ASAP在无需训练且兼容KV-Cache的情况下，对LLaVA-NeXT-7B实现约80%的FLOPs削减，同时保留99.02%的原始性能。

【方法概述 / Method】
ASAP采用两阶段策略：首先利用动态双向软注意力掩码纠正注意力偏移问题，确保选择真正信息丰富的视觉token而非依赖失真的注意力分数；其次通过加权软合并组件将语义相似的token融合，仅保留特征最密集的视觉块传递到后续层。整个流程无需训练，可直接应用于预训练模型。

【实验结果 / Results】
在LLaVA-NeXT-7B上的实验表明，ASAP实现了近乎无损的视觉上下文压缩，保留99.02%的原始模型性能，同时将计算FLOPs大幅降低约80%。该方法在保持多模态能力的同时显著缓解了高分辨率视觉token带来的二次计算成本瓶颈。

【应用价值 / Applications】
ASAP适用于需要实时推理的边缘设备部署、高分辨率图像理解场景以及多模态对话系统等资源受限环境。其训练无关特性使其可直接集成到现有LVLM服务中，为视觉问答、文档理解和自动驾驶视觉感知等应用提供高效的模型加速方案。
