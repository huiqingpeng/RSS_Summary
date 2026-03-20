---
title: "Universal Inverse Distillation for Matching Models with Real-Data Supervision (No GANs)"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.22459"
published: "2026-03-20"
summarized: "2026-03-20T14:16:50.017299"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了RealUID（Real-Data Universal Inverse Distillation），一种通用的知识蒸馏框架，能够适用于所有匹配模型（包括扩散模型、流匹配模型及其变体如桥匹配和随机插值）。该方法突破了现有蒸馏方法仅针对特定框架的限制，并创新性地无需GAN即可在蒸馏过程中有效利用真实数据监督，解决了传统方法依赖复杂对抗训练才能引入真实数据的难题。

【方法概述 / Method】

RealUID基于简单的理论基础，通过逆蒸馏（inverse distillation）机制将预训练教师模型的知识迁移到高效的一步生成器。该方法统一了此前针对流匹配和扩散模型的蒸馏方法，并通过非对抗的方式直接整合真实数据，避免了额外的判别器模型和复杂的对抗训练过程。

【实验结果 / Results】

论文从理论上证明了RealUID框架能够涵盖并扩展先前的蒸馏方法，实验验证表明该框架在多种匹配模型变体（包括Bridge Matching和Stochastic Interpolants）上均有效，实现了一步生成的同时保持了高质量的生成效果，且无需GAN即可利用真实数据提升性能。

【应用价值 / Applications】

RealUID可广泛应用于需要快速推理的生成任务场景，如实时图像生成、视频合成、科学模拟等，为扩散模型和流匹配模型的实际部署提供了高效的解决方案。其通用性和免GAN的特性降低了工程实现复杂度，使更多研究者和开发者能够便捷地构建高效的生成模型。
