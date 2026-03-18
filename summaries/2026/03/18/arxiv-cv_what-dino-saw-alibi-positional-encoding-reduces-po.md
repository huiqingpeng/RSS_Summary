---
title: "What DINO saw: ALiBi positional encoding reduces positional bias in Vision Transformers"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16840"
published: "2026-03-18"
summarized: "2026-03-18T18:21:10.217490"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究发现视觉Transformer（ViT）架构中的位置编码会导致模型产生与语义内容无关的位置偏差和伪影，特别是在材料科学等领域的零样本迁移中造成困难。作者通过线性探测验证了多种目标函数和位置编码方案下均存在位置偏差，并提出通过微调引入ALiBi相对位置编码来有效降低这种偏差。实验表明，采用ALiBi的模型在保留通用语义能力的同时，其无偏特征可成功应用于复杂显微镜图像的可训练分割任务。

【方法概述 / Method】
研究采用线性探测方法系统分析不同ViT模型中的位置偏差，对比了包括绝对位置编码、相对位置编码在内的多种方案。核心方法是通过微调将ALiBi（Attention with Linear Biases）相对位置编码引入预训练视觉模型，替换原有的位置编码机制。

【实验结果 / Results】
ALiBi位置编码显著降低了ViT中的位置偏差，同时保持了模型的语义表征能力；在材料科学显微镜图像分割任务中，基于ALiBi微调模型的特征成功实现了复杂微观结构的可训练分割，验证了无偏特征的实际有效性。

【应用价值 / Applications】
该研究对材料科学等需要分析无优选方向均匀微观结构图像的领域具有重要价值，可提升视觉基础模型在科学成像中的零样本迁移能力。ALiBi编码方案可广泛应用于需要消除位置敏感性的计算机视觉任务，促进ViT在科学计算和工业检测中的部署。
