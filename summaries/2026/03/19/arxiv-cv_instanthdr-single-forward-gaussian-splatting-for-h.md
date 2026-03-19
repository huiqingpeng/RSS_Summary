---
title: "InstantHDR: Single-forward Gaussian Splatting for High Dynamic Range 3D Reconstruction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.11298"
published: "2026-03-19"
summarized: "2026-03-19T16:32:39.132710"
ai_provider: "openai"
---

【论文摘要 / Abstract】
InstantHDR 提出了一种前馈网络，能够从未经标定的多曝光低动态范围（LDR）图像集合中，通过单次前向传播重建高动态范围（HDR）3D 场景。该方法通过几何引导的外观建模实现多曝光融合，并引入元网络进行可泛化的场景特定色调映射。相比现有优化方法，InstantHDR 在保持相当合成质量的同时，实现了约 700 倍的重建速度提升。

【方法概述 / Method】
InstantHDR 基于 3D 高斯泼溅（Gaussian Splatting）框架，设计了两种核心组件：一是几何引导的外观建模模块，用于融合不同曝光条件下的多视角图像特征；二是元网络（meta-network），用于学习可泛化的场景特定色调映射函数。此外，研究团队构建了包含 168 个 Blender 渲染场景的 HDR-Pretrain 预训练数据集，涵盖多样化光照类型和相机响应函数，以支持前馈模型的泛化训练。

【实验结果 / Results】
实验表明，InstantHDR 在 HDR 新视角合成任务上达到了与最先进优化方法相当的合成性能，同时重建速度提升约 700 倍（单次前向设置）和约 20 倍（后优化设置）。该结果证明了前馈方法在 HDR 3D 重建中的可行性与效率优势。

【应用价值 / Applications】
InstantHDR 适用于需要快速 HDR 场景重建的实际应用，如虚拟现实内容生成、沉浸式游戏开发、建筑可视化以及摄影测量等领域。其单次前向推理能力使其特别适合实时或近实时应用，同时无需相机标定和密集点云初始化的特性降低了使用门槛，便于非专业用户部署。
