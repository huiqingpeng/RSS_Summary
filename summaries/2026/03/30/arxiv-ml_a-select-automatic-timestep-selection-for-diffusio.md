---
title: "A-SelecT: Automatic Timestep Selection for Diffusion Transformer Representation Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25758"
published: "2026-03-30"
summarized: "2026-03-31T07:26:59.801682"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为 A-SelecT（Automatically Selected Timestep）的自动时间步选择方法，用于提升扩散Transformer（DiT）的表征学习能力。该方法能够从选定的Transformer特征中动态定位DiT信息最丰富的时间步，无需耗时的穷举搜索和次优的特征选择。实验表明，A-SelecT赋能的DiT在分类和分割任务上高效且有效地超越了此前所有基于扩散模型的方法。

【方法概述 / Method】
A-SelecT通过分析DiT的Transformer特征，在单次前向传播中自动识别最具判别性的时间步，避免了传统方法中需要对大量时间步进行遍历搜索的计算开销。该方法充分利用了DiT特有的特征表示，实现了时间步选择的动态化和自适应化。

【实验结果 / Results】
在分类和分割基准测试上的大量实验表明，配备A-SelecT的DiT在效率和效果上均优于现有基于扩散模型的表征学习方法。该方法显著提升了DiT的训练效率和表征能力，为生成式预训练在判别任务中的应用开辟了新途径。

【应用价值 / Applications】
A-SelecT可广泛应用于计算机视觉的判别任务，如图像分类、语义分割等需要高质量视觉表征的场景。该方法降低了扩散模型用于表征学习的计算成本，使DiT的生成式预训练优势能够更高效地迁移到下游判别任务，具有重要的实际部署价值。
