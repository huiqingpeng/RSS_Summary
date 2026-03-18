---
title: "TAUE: Training-free Noise Transplant and Cultivation Diffusion Model"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.02580"
published: "2026-03-18"
summarized: "2026-03-18T17:12:42.481434"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了TAUE（Training-free Noise Transplantation and Cultivation Diffusion Model），一种无需训练或额外数据的层级图像生成框架，解决了文本到图像扩散模型只能输出扁平化单张图像的问题。TAUE通过将中间去噪潜变量的全局结构信息嵌入初始噪声以保持空间连贯性，并通过跨层注意力共享整合语义线索以维持层间上下文和视觉一致性。实验表明，TAUE在无需训练的方法中达到最优性能，图像质量可媲美微调模型，同时显著提升了层间一致性。

【方法概述 / Method】
TAUE采用噪声移植与培育机制，从中间去噪步骤提取全局结构信息并将其嵌入初始噪声，确保各层在空间布局上保持连贯；同时引入跨层注意力共享机制，使不同图层在生成过程中能够交换语义信息，从而实现上下文一致的层级图像合成。

【实验结果 / Results】
TAUE在无需训练的方法中实现了最先进的性能，生成的图像质量与经过微调的模型相当，同时显著改善了层间一致性；此外，该方法成功支持了布局感知编辑、多目标组合和背景替换等多种新应用。

【应用价值 / Applications】
TAUE可应用于专业创意工作流程中的交互式分层生成系统，如图像编辑软件中的布局感知编辑、广告设计中的多元素合成、以及影视后期制作中的背景替换等场景，为需要精确图层控制的专业应用提供了高效且无需重新训练模型的解决方案。
