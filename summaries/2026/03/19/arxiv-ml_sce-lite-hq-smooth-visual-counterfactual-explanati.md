---
title: "SCE-LITE-HQ: Smooth visual counterfactual explanations with generative foundation models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17048"
published: "2026-03-19"
summarized: "2026-03-19T12:06:58.377943"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SCE-LITE-HQ，一种基于预训练生成式基础模型的可扩展反事实解释生成框架，无需针对特定任务重新训练。该方法在生成器的潜在空间中操作，结合平滑梯度优化和基于掩码的多样化策略，以生成有效、真实且结构多样的高分辨率反事实样本。实验表明，该方法在自然图像和医学数据集上达到或超越了现有基线性能，同时避免了训练专用生成模型的高昂计算开销。

【方法概述 / Method】
SCE-LITE-HQ利用预训练生成式基础模型（如Stable Diffusion）的潜在空间进行反事实优化，而非从头训练数据集特定的生成模型。核心技术创新包括：引入平滑梯度（smoothed gradients）提升优化过程的稳定性，以及采用基于掩码的多样化机制（mask-based diversification）促进生成样本的结构多样性。

【实验结果 / Results】
研究在自然图像和医学数据集上采用基于期望指标的评估协议进行验证。结果表明，SCE-LITE-HQ生成的反事实解释在有效性、真实性和多样性方面与现有基线方法相当或更优，同时显著降低了计算成本，实现了对高分辨率数据的扩展能力。

【应用价值 / Applications】
该方法可广泛应用于需要解释黑盒模型决策的高风险视觉领域，如医学影像诊断（帮助医生理解AI诊断依据）、自动驾驶（解释场景识别模型的判断逻辑）和内容审核等。其无需任务特定训练的特性使其能够快速部署到新的视觉任务中，提升AI系统的可解释性和用户信任度。
