---
title: "Mamba2D: A Natively Multi-Dimensional State-Space Model for Vision Tasks"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2412.16146"
published: "2026-03-18"
summarized: "2026-03-18T18:25:10.657810"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 Mamba2D，一种原生多维状态空间模型（M2D-SSM），专门针对视觉任务重新设计了选择性状态空间技术。与现有将一维 SSM 直接应用于图像的视觉模型不同，M2D-SSM 采用单一 2D 扫描机制，原生地同时考虑图像的两个空间维度。该模型在 ImageNet-1K 分类任务上取得了优异性能（M2D-T 以 27M 参数达到 84.0% 准确率，M2D-S 达到 85.3%），并在 MS-COCO 目标检测和 ADE20K 语义分割等下游任务中展现出强大的泛化能力和效率优势。

【方法概述 / Method】

M2D-SSM 从零开始重新推导了选择性状态空间技术，使其适用于多维数据，而非简单地将 NLP 中的 1D SSM 通过光栅化扫描应用于图像。核心创新在于采用单一 2D 扫描策略，同时沿高度和宽度两个空间维度处理信息，消除了现有方法中因顺序扫描带来的空间结构破坏问题。

【实验结果 / Results】

在 ImageNet-1K 分类任务中，M2D-T 以仅 27M 参数达到 84.0% top-1 准确率，超越所有同规模 SSM 视觉模型；M2D-S 进一步达到 85.3%，创下 SSM 架构的新 SOTA。在下游任务中，Mamba2D 在 MS-COCO 目标检测（3× 训练 schedule）上取得 52.2 box AP，在 ADE20K 语义分割上达到 51.7 mIoU，显示出良好的扩展性和任务迁移能力。

【应用价值 / Applications】

Mamba2D 为高效视觉模型设计提供了新范式，可广泛应用于图像分类、目标检测、语义分割等核心计算机视觉任务。其原生 2D 设计克服了传统 SSM 在视觉领域的结构性局限，为需要长程依赖建模且计算资源受限的场景（如边缘设备部署、高分辨率图像处理）提供了 Transformer 的高效替代方案。
