---
title: "ViT-AdaLA: Adapting Vision Transformers with Linear Attention"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16063"
published: "2026-03-18"
summarized: "2026-03-18T18:04:32.673655"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ViT-AdaLA，一种将预训练视觉基础模型（VFM）的知识有效迁移到线性注意力Vision Transformer的新框架。该方法通过三阶段策略（注意力对齐、特征对齐和监督微调）解决现有线性注意力方法需从头训练、计算成本高以及大语言模型线性化方法向ViT迁移效果差的问题。实验表明，ViT-AdaLA在分类和分割任务上优于现有最先进的线性注意力方法，具有良好的通用性和有效性。

【方法概述 / Method】
ViT-AdaLA采用三阶段渐进式适应策略：首先通过注意力对齐使每层线性注意力逼近原始softmax注意力的行为；然后通过特征对齐阶段，以冻结的softmax VFM教师模型为指导，微调线性化ViT的最终层特征以缓解跨层累积的近似误差；最后通过监督微调将适应后的先验知识迁移到下游任务。

【实验结果 / Results】
论文在图像分类和语义分割任务上进行了大量实验，结果表明ViT-AdaLA在多种架构上均优于现有的线性注意力方法。该方法成功实现了从预训练softmax注意力模型到线性注意力模型的高效知识迁移，在保持线性计算复杂度的同时显著提升了模型性能。

【应用价值 / Applications】
ViT-AdaLA可应用于需要处理高分辨率图像或长序列视觉任务的场景，如医学影像分析、遥感图像处理和视频理解等，其线性复杂度特性使模型能够扩展到更大规模的输入。该方法为高效部署视觉基础模型提供了新途径，有助于降低推理成本并促进在资源受限设备上的应用。
