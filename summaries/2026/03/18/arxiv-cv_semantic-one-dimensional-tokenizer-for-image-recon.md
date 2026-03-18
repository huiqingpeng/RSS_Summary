---
title: "Semantic One-Dimensional Tokenizer for Image Reconstruction and Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16373"
published: "2026-03-18"
summarized: "2026-03-18T18:12:07.311127"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SemTok，一种语义一维分词器（Semantic One-Dimensional Tokenizer），将二维图像压缩为一维离散token，同时保留高层语义信息。该方法在图像重建任务上取得了新的最优性能，以极其紧凑的token表示实现了卓越的重建保真度。基于SemTok构建的掩码自回归生成框架在下游图像生成任务中也展现出显著改进，突破了传统2D空间网格分词器在捕获紧凑全局语义方面的局限。

【方法概述 / Method】
SemTok采用三项关键创新：一是2D到1D的分词方案，将图像空间结构转换为一维序列；二是语义对齐约束，确保token携带高层语义信息而非仅像素级细节；三是两阶段生成训练策略，优化重建与生成能力的协同。该框架通过协同设计实现了紧凑表示与高质量重建的平衡。

【实验结果 / Results】
实验表明，SemTok在图像重建任务上达到了新的最优水平（state-of-the-art），在显著降低token数量的同时保持了优异的重建保真度。基于SemTok构建的掩码自回归生成模型在下游图像生成任务中取得了明显提升，验证了一维语义分词的有效性和优越性。

【应用价值 / Applications】
SemTok可广泛应用于高效图像生成、多模态大模型对齐及视觉-语言预训练等场景，其紧凑的语义表示大幅降低计算开销，有利于模型规模化扩展。该方法为视觉生成模型提供了更高效的潜在空间表示方案，在实时图像合成、低带宽视觉传输及边缘设备部署等实际应用中具有重要价值。
