---
title: "Dynamic Memory Transformer for Hyperspectral Image Classification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2504.13242"
published: "2026-03-18"
summarized: "2026-03-18T18:25:46.667369"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为MemFormer的轻量级Transformer架构，用于高光谱图像分类（HSIC）。该架构通过动态记忆增强注意力机制，在多头自注意力中引入紧凑的全局记忆模块，逐层聚合上下文信息，从而有效建模长距离依赖关系并减少注意力冗余。此外，论文还设计了空间-光谱位置嵌入（SSPE），联合编码空间连续性和光谱顺序，无需依赖卷积即可提供结构一致的表征。在三个基准数据集上的实验表明，MemFormer在Indian Pines数据集上达到了99.55%的总体准确率、99.38%的平均准确率和99.49%的Kappa系数，显著优于现有的卷积、混合和基于Transformer的方法。

【方法概述 / Method】
MemFormer的核心创新在于动态记忆增强注意力机制，该机制通过可学习的全局记忆向量存储和更新跨层上下文信息，替代传统Transformer中计算密集型的成对注意力计算。同时，论文提出了空间-光谱位置嵌入（SSPE），直接利用高光谱数据的物理结构特性，将空间坐标和光谱波段索引分别编码后融合，避免了卷积操作带来的归纳偏置。

【实验结果 / Results】
在Indian Pines、WHU-Hi-HanChuan和WHU-Hi-HongHu三个基准数据集上，MemFormer均取得了最优的分类性能。特别是在Indian Pines数据集上，该方法达到了99.55%的总体准确率（OA）、99.38%的平均准确率（AA）和99.49%的Kappa系数。实验结果还表明，MemFormer在参数量和计算效率方面具有优势，能够以更轻量的架构实现更高的分类精度。

【应用价值 / Applications】
该研究在精准农业、环境监测、矿物勘探和城市规划等领域具有重要应用价值，高光谱图像分类可用于作物健康评估、污染物检测、地质制图等任务。MemFormer的轻量化设计使其更适合部署于资源受限的遥感平台，如无人机或卫星边缘计算设备。此外，该方法减少了对大量标注数据的依赖，为标注成本高昂的高光谱遥感应用提供了更实用的解决方案。
