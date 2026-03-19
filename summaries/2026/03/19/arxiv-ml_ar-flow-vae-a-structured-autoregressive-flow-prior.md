---
title: "AR-Flow VAE: A Structured Autoregressive Flow Prior Variational Autoencoder for Unsupervised Blind Source Separation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14441"
published: "2026-03-19"
summarized: "2026-03-19T14:19:57.993537"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出AR-Flow VAE，一种用于无监督盲源分离（BSS）的新型变分自编码器框架。该框架为每个潜在源信号配备参数自适应的自回归流先验，显著增强了潜在源建模的灵活性，能够捕捉复杂的非高斯行为和结构化依赖（如时间相关性）。此外，结构化先验设计为不同潜在维度分配不同的先验，促使潜在成分在异构先验约束下分离为不同的源信号。实验结果验证了该架构在盲源分离中的有效性。

【方法概述 / Method】
AR-Flow VAE采用变分自编码器架构，将编码器视为从观测信号到源信号的解混映射，解码器视为从推断源信号重构观测的混音过程。核心创新在于使用参数自适应的自回归流作为潜在变量的先验分布，替代传统的高斯先验，从而建模更复杂的源信号统计特性。

【实验结果 / Results】
论文通过实验验证了AR-Flow VAE在盲源分离任务上的有效性，表明该框架能够成功分离混合信号中的潜在源成分。自回归流先验的引入使模型能够捕捉传统方法难以表示的非高斯特性和时间结构，提升了分离性能。

【应用价值 / Applications】
该研究可应用于音频信号处理（如音乐源分离、语音分离）、神经信号分析（如脑电信号分解）以及金融时间序列分解等领域。AR-Flow VAE为探索VAE在盲源分离中的可识别性和可解释性提供了理论基础，有望推动无监督信号分离技术的进一步发展。
