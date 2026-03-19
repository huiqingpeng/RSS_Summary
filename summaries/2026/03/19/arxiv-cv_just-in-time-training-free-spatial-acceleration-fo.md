---
title: "Just-in-Time: Training-Free Spatial Acceleration for Diffusion Transformers"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.10744"
published: "2026-03-19"
summarized: "2026-03-19T16:32:28.979383"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 Just-in-Time (JiT)，一种针对扩散 Transformer（Diffusion Transformers）的新型免训练空间加速框架。JiT 通过识别生成过程中的空间冗余（全局结构早于细节形成）来加速推理，而非仅关注时域压缩。该方法构建了基于稀疏锚点 token 的空间近似生成常微分方程（ODE），并通过确定性微流（deterministic micro-flow）实现 token 动态扩展时的无缝过渡。在 FLUX.1-dev 模型上的实验表明，JiT 可实现高达 7 倍加速且几乎无损性能，显著优于现有加速方法。

【方法概述 / Method】

JiT 的核心方法是构建空间近似的生成 ODE，仅对动态选择的稀疏锚点 token 进行完整计算，而非处理全部空间区域。为解决 token 扩展时的维度变化问题，作者提出了确定性微流——一种有限时间 ODE，能够在保持结构一致性和统计正确性的前提下，实现 latent 状态维度的平滑扩展。

【实验结果 / Results】

在 FLUX.1-dev 这一最先进的扩散 Transformer 模型上，JiT 实现了最高 7 倍的推理加速，同时保持了近乎无损的生成质量。该方法在推理速度与生成保真度之间建立了新的更优权衡，显著超越了现有的加速方法。

【应用价值 / Applications】

JiT 可直接部署于高分辨率图像生成、实时内容创作等计算资源受限的场景，无需重新训练模型即可大幅降低推理成本。该框架为扩散模型在边缘设备、交互式应用和规模化生产环境中的实际部署提供了可行路径，有望推动生成式 AI 技术的广泛普及。
