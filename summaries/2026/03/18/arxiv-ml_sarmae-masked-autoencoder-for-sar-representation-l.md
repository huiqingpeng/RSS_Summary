---
title: "SARMAE: Masked Autoencoder for SAR Representation Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.16635"
published: "2026-03-18"
summarized: "2026-03-18T17:13:22.757246"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SARMAE，一种面向合成孔径雷达（SAR）图像的噪声感知掩码自编码器，用于自监督表示学习。研究团队构建了首个百万级SAR数据集SAR-1M，并配套光学图像以支持大规模预训练。该方法通过两项创新设计——散斑感知表示增强（SARE）和语义锚点表示约束（SARC），有效解决了SAR图像中散斑噪声干扰和语义表示学习困难的问题，在分类、检测和分割任务上均达到最优性能。

【方法概述 / Method】
SARMAE基于掩码自编码器架构，创新性地引入SARE模块，将SAR特有的散斑噪声显式注入预训练过程，增强模型对噪声的感知与鲁棒性；同时设计SARC模块，利用配对的光学图像作为语义锚点，约束SAR特征与光学特征的对齐，确保语义一致性。

【实验结果 / Results】
在多个SAR数据集上的大量实验表明，SARMAE在分类、目标检测和语义分割等下游任务中均取得当前最优性能，验证了所提方法的有效性；基于SAR-1M的大规模预训练显著提升了模型的泛化能力和迁移学习效果。

【应用价值 / Applications】
SARMAE可广泛应用于全天候、全天时的遥感监测场景，如灾害应急评估、海洋目标监视、军事侦察及农业资源调查等；其自监督预训练范式降低了对标注数据的依赖，为SAR智能解译提供了可扩展的技术基础。
