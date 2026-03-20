---
title: "RPiAE: A Representation-Pivoted Autoencoder Enhancing Both Image Generation and Editing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19206"
published: "2026-03-20"
summarized: "2026-03-20T16:05:52.114472"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种基于表征的自动编码器RPiAE（Representation-Pivoted AutoEncoder），旨在同时提升图像生成和编辑的质量。现有方法利用预训练视觉表征模型作为tokenizer先验时，常因编码器冻结导致重建保真度不足、编辑质量下降，且高维潜变量增加了扩散建模难度。RPiAE通过表征枢轴正则化策略和变分桥接技术，在保持语义结构的同时实现高效重建，并采用目标解耦的分阶段训练策略。实验表明，RPiAE在文本到图像生成和图像编辑任务上均优于其他视觉tokenizer，同时在基于表征的tokenizer中实现了最佳重建保真度。

【方法概述 / Method】

RPiAE的核心方法包括三个关键组件：（1）**表征枢轴正则化（Representation-Pivot Regularization）**：允许以表征初始化的编码器在微调过程中兼顾重建任务，同时保持预训练表征空间的语义结构；（2）**变分桥接（Variational Bridge）**：将高维潜变量压缩为紧凑的低维潜空间，降低扩散建模复杂度；（3）**目标解耦的分阶段训练（Objective-Decoupled Stage-Wise Training）**：依次优化生成可处理性和重建保真度两个目标，避免训练过程中的目标冲突。

【实验结果 / Results】

RPiAE在文本到图像生成和图像编辑任务上均超越了其他视觉tokenizer，同时在基于表征的tokenizer中取得了最高的重建保真度。具体而言，该方法成功解决了现有表征tokenizer中重建质量与语义保持之间的权衡问题，生成的潜变量具有更低的维度，显著简化了后续的扩散建模过程。

【应用价值 / Applications】

RPiAE可广泛应用于高效高质量的图像生成系统（如文本到图像合成）、精确的图像编辑工具（如语义操控和风格迁移），以及需要紧凑潜表示的实时视觉应用。该方法通过提供语义丰富且重建准确的潜空间，为下游扩散模型提供了更优的基础，有望推动生成式AI在内容创作、虚拟现实和交互式媒体等领域的实际部署。
