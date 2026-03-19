---
title: "HyPER-GAN: Hybrid Patch-Based Image-to-Image Translation for Real-Time Photorealism Enhancement"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.10604"
published: "2026-03-19"
summarized: "2026-03-19T16:32:16.943113"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了HyPER-GAN（Hybrid Patch Enhanced Realism Generative Adversarial Network），一种轻量级的图像到图像翻译方法，用于实时增强合成数据的视觉真实感。该模型采用U-Net风格的生成器，通过混合训练策略结合配对合成图像、真实感增强图像以及真实世界图像的匹配补丁进行训练。实验结果表明，HyPER-GAN在推理延迟、视觉真实感和语义鲁棒性方面均优于现有的轻量级配对图像翻译方法，且混合训练策略显著提升了视觉质量和语义一致性。

【方法概述 / Method】
HyPER-GAN基于U-Net架构的轻量级生成器，采用混合训练策略：使用配对的合成图像与真实感增强图像作为基础训练数据，同时引入来自真实世界图像的匹配补丁（matched patches）以提升视觉真实感和语义一致性。该设计旨在平衡计算效率与生成质量，满足实时推理需求。

【实验结果 / Results】
HyPER-GAN在推理延迟、视觉真实感和语义鲁棒性三个关键指标上均超越了当前最先进的轻量级配对图像到图像翻译方法。消融实验验证了混合训练策略的有效性——相比仅使用配对合成数据训练，引入真实图像补丁显著改善了生成图像的视觉质量和语义一致性。

【应用价值 / Applications】
该研究适用于需要实时生成高质量训练数据的计算机视觉应用场景，如自动驾驶仿真、机器人训练和增强现实等。HyPER-GAN的低延迟特性使其能够集成到实时训练或评估流程中，而减少视觉伪影的能力有助于提升下游视觉算法的准确性和鲁棒性。
