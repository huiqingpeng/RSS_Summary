---
title: "Semi-supervised Latent Disentangled Diffusion Model for Textile Pattern Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16747"
published: "2026-03-18"
summarized: "2026-03-18T18:20:10.411455"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为SLDDM-TPG的新型半监督潜在解耦扩散模型，用于解决纺织图案生成（TPG）任务中现有图像到图像模型产生的特征混淆问题。该方法通过构建多维独立的服装特征空间，有效分离复杂纺织图案与服装非刚性纹理变形，实现了高保真度的纺织图案生成。实验表明，该方法在CTPHD数据集上将FID降低4.1、SSIM提升0.116，并在VITON-HD数据集上展现出良好的泛化能力。

【方法概述 / Method】
该方法包含两个阶段：（1）潜在解耦网络（LDN），用于解析服装表示中的特征混淆并构建多维独立的服装特征空间；（2）半监督潜在扩散模型（S-LDM），接收LDN的引导信号，通过半监督扩散训练结合细粒度对齐策略生成忠实结果。

【实验结果 / Results】
在CTPHD数据集上，SLDDM-TPG相比基线方法将FID降低4.1，SSIM提升高达0.116；同时在VITON-HD数据集上的测试证明了该方法具有良好的跨数据集泛化性能。

【应用价值 / Applications】
该研究可直接应用于服装电商平台的虚拟试衣、时尚设计辅助工具以及纺织品数字化生产等领域，为服装行业提供高质量的自动化纺织图案生成解决方案，降低设计成本并提升生产效率。
