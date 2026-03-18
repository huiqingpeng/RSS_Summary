---
title: "Leveling3D: Leveling Up 3D Reconstruction with Feed-Forward 3D Gaussian Splatting and Geometry-Aware Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16211"
published: "2026-03-18"
summarized: "2026-03-18T18:08:25.063685"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Leveling3D，一种将前馈3D重建与几何一致性生成相结合的新颖框架，实现了整体化的同步重建与生成。该方法通过轻量级的几何感知leveling适配器，将扩散模型的内部知识与来自前馈模型的几何先验对齐，从而修复外推新视角中因3D表示欠约束区域导致的伪影。实验表明，增强后的外推新视角可重新输入前馈3DGS以提升3D重建质量，在公开数据集的新视角合成和深度估计任务上达到SOTA性能。

【方法概述 / Method】
Leveling3D的核心是几何感知leveling适配器，用于桥接前馈3D高斯溅射（3DGS）模型与扩散模型，使扩散生成过程能够遵循输入的几何约束。为学习更多样化的生成分布，研究引入了调色板过滤训练策略，并设计了测试时掩码细化机制以避免修复区域的边界混乱。

【实验结果 / Results】
该方法在多个公开数据集上取得了最先进（SOTA）的性能，涵盖新视角合成和深度估计等任务。通过迭代地将增强后的外推视角反馈至前馈3DGS，实现了3D重建质量的持续提升，有效解决了传统方法在外推视角中缺失区域填充失败的问题。

【应用价值 / Applications】
Leveling3D可广泛应用于需要高质量3D重建和新颖视角合成的场景，如虚拟现实/增强现实内容创作、数字孪生构建、自动驾驶仿真环境生成等。其前馈推理特性使其适合实时或近实时应用，而几何感知的生成能力确保了重建结果的一致性和完整性。
