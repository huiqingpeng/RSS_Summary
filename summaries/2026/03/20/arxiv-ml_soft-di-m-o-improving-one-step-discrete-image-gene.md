---
title: "Soft-Di[M]O: Improving One-Step Discrete Image Generation with Soft Embeddings"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.22925"
published: "2026-03-20"
summarized: "2026-03-20T14:17:01.031055"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出Soft-Di[M]O方法，通过引入软嵌入（soft embeddings）解决一步式离散图像生成器的两大局限：继承教师模型的建模偏差以及离散token输出阻断梯度流的问题。软嵌入用输出分布的期望嵌入替代离散token，在保持表示保真度的同时实现完全可微的连续替代，使一步式生成器能够进行端到端训练，并支持GAN优化、可微奖励微调和测试时嵌入优化（TTEO）等后蒸馏改进。实验表明，该方法在多个MDM教师模型上取得最先进的单步生成结果，包括ImageNet-256上FID达1.56。

【方法概述 / Method】
核心创新是软嵌入机制：将生成器输出的离散token分布转化为连续可微的期望嵌入，既兼容教师骨干网络和tokenizer解码器，又打通了梯度传播路径。该方法被集成到Di[M]O蒸馏框架中，形成Soft-Di[M]O，使原本不可微的一步式离散生成器变为端到端可训练。

【实验结果 / Results】
在多个MDM教师模型（如MaskBit、MaskGen）上，Soft-Di[M]O实现了最先进的单步生成性能：ImageNet-256类别条件生成经GAN优化后FID降至1.56；文本到图像生成在奖励微调后获得更高的GenEval和HPS评分；测试时嵌入优化（TTEO）进一步带来额外性能提升。

【应用价值 / Applications】
该方法可广泛应用于高效图像合成场景，包括实时文本到图像生成、类别条件图像合成等需要单步推理的应用；其可微特性还使生成器能够直接对接下游优化技术（如人类偏好对齐、对抗训练），为部署轻量级高质量生成模型提供了可行路径。
