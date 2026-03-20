---
title: "Epistemic Generative Adversarial Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18348"
published: "2026-03-20"
summarized: "2026-03-20T12:10:54.065600"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种基于Dempster-Shafer证据理论的GAN损失函数泛化方法，可同时应用于生成器和判别器。作者还设计了一种生成器架构增强方案，使其能够为每个图像像素预测质量函数（mass function），从而量化输出不确定性并利用该不确定性生成更多样化、更具代表性的样本。实验结果表明，该方法不仅提升了生成多样性，还为生成过程中的不确定性建模与解释提供了原则性框架。

【方法概述 / Method】

论文将Dempster-Shafer证据理论引入GAN框架，构建了一种新的认知损失函数（epistemic loss），替代传统的对抗损失。生成器被扩展为输出像素级质量函数而非确定性像素值，显式建模生成过程中的认知不确定性（epistemic uncertainty）。

【实验结果 / Results】

实验表明，该方法在保持样本质量的同时显著提升了生成多样性，有效缓解了模式坍塌（mode collapse）问题。模型输出的质量函数为生成结果提供了可解释的不确定性度量，有助于识别模型置信度较低的区域。

【应用价值 / Applications】

该方法适用于需要高多样性生成的场景，如图像合成、数据增强和创意内容生成。像素级不确定性量化还可用于安全关键应用中的风险感知决策，以及生成结果的可靠性评估与人工审核优先级排序。
