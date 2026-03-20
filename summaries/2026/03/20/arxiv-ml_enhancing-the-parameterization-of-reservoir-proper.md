---
title: "Enhancing the Parameterization of Reservoir Properties for Data Assimilation Using Deep VAE-GAN"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18766"
published: "2026-03-20"
summarized: "2026-03-20T12:15:42.573715"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对油藏历史拟合中迭代集合平滑器（特别是ESMDA方法）的两个关键局限性——有限集合尺寸对分布的表示不足以及参数和数据不确定性中的高斯假设问题，提出了一种创新的解决方案。作者将变分自编码器生成对抗网络（VAE-GAN）与ESMDA集成，结合了GAN生成地质真实感强的模型和VAE在数据同化中表现优异的双重优势。在两个案例研究（分类变量和连续渗透率值）中，该方法同时实现了高质量的油藏描述和良好的生产曲线历史拟合。

【方法概述 / Method】
本研究采用深度VAE-GAN模型进行参数化，将非高斯参数映射到高斯场进行更新，再映射回原始域以驱动油藏模拟器。该方法将VAE-GAN与迭代集合平滑器ESMDA深度集成，形成端到端的油藏属性参数化与数据同化框架。

【实验结果 / Results】
研究在两个案例上验证了方法的有效性：一个为分类变量案例，另一个为连续渗透率值案例。实验结果表明，VAE-GAN模型能够同时达到与GAN相当的高质量地质模型生成效果，以及媲美VAE的优秀历史拟合性能，克服了单一方法的局限性。

【应用价值 / Applications】
该方法可广泛应用于石油油藏工程中的历史拟合与不确定性量化，特别适用于具有复杂非高斯分布的地质属性建模。通过提升参数化质量和数据同化精度，该技术有助于优化油藏开发决策、降低勘探风险，并提高剩余油分布预测的可靠性。
