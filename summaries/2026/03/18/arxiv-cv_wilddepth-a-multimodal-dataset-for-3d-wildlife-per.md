---
title: "WildDepth: A Multimodal Dataset for 3D Wildlife Perception and Depth Estimation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16816"
published: "2026-03-18"
summarized: "2026-03-18T18:20:53.380585"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了WildDepth，首个面向动物的多模态数据集与基准套件，包含从家养到野生环境中多种动物类别的同步RGB与LiDAR数据，支持深度估计、行为检测和三维重建任务。研究解决了现有动物深度估计模型缺乏度量尺度的问题，实验表明多模态数据可将深度可靠性提升达10%（RMSE），RGB-LiDAR融合可将三维重建保真度提升12%（Chamfer距离）。该工作旨在推动能够跨领域泛化的鲁棒多模态感知系统的发展。

【方法概述 / Method】

本研究构建了一个大规模多模态数据集WildDepth，通过同步采集RGB图像与LiDAR点云数据，为动物目标提供精确的度量深度真值。数据集涵盖从家养到野外的多样化动物类别及环境场景，并配套建立了深度估计、行为检测和三维重建的基准测试框架。

【实验结果 / Results】

实验结果表明，利用多模态数据进行训练可将深度估计的可靠性提升最高达10%（以RMSE衡量）；采用RGB-LiDAR融合方法进行三维重建，其保真度相比单模态方法提升了12%（以Chamfer距离衡量）。这些结果验证了多模态感知在野生动物三维理解任务中的显著优势。

【应用价值 / Applications】

WildDepth可广泛应用于野生动物监测与保护、动物行为学研究、生态学调查等领域，为无人值守的野外智能感知系统提供技术支撑。该数据集还有助于推动面向非刚性形变目标的深度估计与三维重建算法发展，促进计算机视觉技术在自然场景中的泛化应用。
