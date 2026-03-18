---
title: "MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.17392"
published: "2026-03-18"
summarized: "2026-03-18T18:29:08.869870"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出MorphSeek，一种细粒度潜在表示级策略优化范式，将可变形图像配准（DIR）重新表述为潜在特征空间中的空间连续优化过程。该方法通过在编码器顶部引入随机高斯策略头来建模潜在特征分布，实现高效探索与粗到精的细化，并结合无监督预热与弱监督微调（采用组相对策略优化）来提升标签效率。在三个3D配准基准测试（OASIS脑MRI、LiTS肝CT和腹部MR-CT）中，MorphSeek在保持高标签效率和低计算开销的同时，实现了比竞争基线更优的Dice分数。

【方法概述 / Method】
MorphSeek采用编码器-解码器架构，在编码器顶端引入随机高斯策略头对潜在特征分布进行建模，将高维变形场的优化转化为潜在空间中的策略搜索问题。训练过程分为两阶段：首先进行无监督预热以学习合理的初始策略，随后利用组相对策略优化（GRPO）进行弱监督微调，通过多轨迹采样机制稳定训练并减少标注依赖。

【实验结果 / Results】
在OASIS脑MRI、LiTS肝CT和腹部MR-CT三个3D配准数据集上，MorphSeek相比现有竞争方法取得一致的Dice分数提升，同时仅需极少量的标注数据。该方法保持了较低的参数量开销和步骤级延迟，证明了其在高维变形优化中的计算效率与配准精度的良好平衡。

【应用价值 / Applications】
MorphSeek为医学图像分析中的可变形配准问题提供了一种与主干网络和优化器无关的通用解决方案，适用于多模态（如MR-CT）和单模态医学图像对齐任务。其高标签效率特性可降低医学图像标注成本，空间连贯的变形优化能力使其特别适用于需要精细解剖对齐的临床场景，如手术导航、放疗计划和纵向病变监测。
