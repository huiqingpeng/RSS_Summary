---
title: "Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.15190"
published: "2026-03-18"
summarized: "2026-03-18T17:03:09.521761"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 MARVAL（Masked Auto-regressive Variational Acceleration），一种基于蒸馏的框架，用于加速掩码自回归扩散模型（MAR）的推理过程。该方法将扩散去噪链压缩为单个自回归生成步骤，同时保留灵活的掩码自回归解掩码顺序，实现了超过30倍的推理加速。更重要的是，MARVAL 使基于可验证奖励的强化学习后训练变得实用，并提出了 MARVAL-RL 框架，在 ImageNet 256×256 上取得了 FID 2.00 的优异性能，同时在 CLIP 分数和图像奖励分数上实现了与人类偏好更好对齐的生成效果。

【方法概述 / Method】

MARVAL 采用基于分数的变分目标函数，通过知识蒸馏将掩码自回归扩散模型的多级扩散去噪过程压缩为单步生成，同时保持外层自回归解掩码循环的灵活性。该方法还扩展了 MARVAL-RL 框架，使掩码自回归模型能够高效地进行强化学习后训练，利用可验证奖励优化生成质量。

【实验结果 / Results】

在 ImageNet 256×256 数据集上，MARVAL-Huge 模型达到 FID 2.00 的生成质量，相比原始 MAR-diffusion 实现超过30倍的速度提升。在包含实体名称的 ImageNet 数据集上，MARVAL-RL 在 CLIP 分数和图像奖励（image-reward）指标上均取得一致提升，验证了快速采样与偏好对齐的可扩展性。

【应用价值 / Applications】

MARVAL 为掩码自回归扩散模型的实际部署提供了可行路径，解决了生成效率瓶颈，使其适用于需要实时响应的图像生成应用。该方法同时开启了高效强化学习微调的可能性，可用于构建更符合人类偏好的可控生成系统，如个性化内容创作、交互式编辑工具等场景。
