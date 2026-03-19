---
title: "Variational Rectification Inference for Learning with Noisy Labels"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17255"
published: "2026-03-19"
summarized: "2026-03-19T12:09:40.176944"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种变分修正推理（Variational Rectification Inference, VRI）方法，用于解决深度模型在含噪声标签数据上的过拟合问题。该方法将损失函数的自适应修正建模为摊销变分推理问题，并在元学习框架下推导出证据下界。VRI 通过将修正向量视为隐变量构建层次贝叶斯模型，引入额外的随机性正则化来修正噪声样本的损失，从而增强对标签噪声的鲁棒性。实验表明，该方法在特别是开放集噪声场景下具有显著的鲁棒学习效果。

【方法概述 / Method】

VRI 将损失修正向量作为隐变量，构建层次贝叶斯模型，并通过摊销元网络（amortization meta-network）近似其条件后验分布。该方法在变分推理中引入变分项，使条件后验估计更准确，避免坍缩为狄拉克δ函数；同时，精心设计的元网络和先验网络遵循平滑性假设，以生成可靠的修正向量。

【实验结果 / Results】

综合对比实验验证了 VRI 在含噪声标签学习中的有效性，特别是在开放集噪声（open-set noise）场景下表现突出。理论分析保证了元网络可被高效学习，且变分推理机制显著提升了模型的泛化性能，避免了模型坍缩问题。

【应用价值 / Applications】

VRI 可广泛应用于真实世界中存在标签噪声的机器学习场景，如众包标注数据、医疗影像诊断标签错误、网络爬取数据的自动标注等。该方法仅需少量干净的元数据即可进行高效元学习，为实际部署中数据质量受限的深度学习应用提供了可靠的鲁棒训练方案。
