---
title: "SF-Mamba: Rethinking State Space Model for Vision"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16423"
published: "2026-03-18"
summarized: "2026-03-18T18:12:58.174555"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了SF-Mamba，一种重新思考视觉任务中状态空间模型扫描机制的新型视觉编码器。针对现有Mamba模型中非因果交互受限、多扫描策略效率低下以及短序列计算速度慢等问题，作者提出了辅助块交换（auxiliary patch swapping）和批折叠周期性状态重置（batch folding with periodic state reset）两种关键技术。实验表明，SF-Mamba在图像分类、目标检测、实例分割和语义分割等任务上均显著优于现有基线，同时提升了不同模型规模的吞吐量。

【方法概述 / Method】

SF-Mamba的核心创新包括两方面：一是辅助块交换机制，通过在不增加额外扫描方向的情况下实现双向信息流编码，避免了传统多扫描策略带来的数据重排开销；二是批折叠与周期性状态重置技术，通过优化GPU并行计算来加速短序列情况下的推理速度。这两种设计共同实现了高效且具备全局建模能力的单向扫描视觉编码器。

【实验结果 / Results】

在多个视觉基准任务上的广泛实验表明，SF-Mamba在不同模型规模下均取得了一致的性能提升，同时显著改善了计算吞吐量。具体而言，该方法在保持与Vision Transformer相当或更优精度的同时，克服了Mamba在短token长度下计算速度较慢的固有缺陷，实现了真正的计算效率优势。

【应用价值 / Applications】

SF-Mamba可作为高效视觉骨干网络广泛应用于各类视觉任务，包括图像分类、目标检测和语义分割等，特别适用于对实时性和计算资源敏感的场景。其高效的单向扫描设计和高GPU并行性使其成为部署在边缘设备或大规模视觉系统中的理想选择，为Mamba替代Vision Transformer提供了更具竞争力的解决方案。
