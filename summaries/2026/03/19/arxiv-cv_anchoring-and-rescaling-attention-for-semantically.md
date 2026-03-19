---
title: "Anchoring and Rescaling Attention for Semantically Coherent Inbetweening"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17651"
published: "2026-03-19"
summarized: "2026-03-19T15:15:21.227877"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对生成式中间帧插值（Generative Inbetweening, GI）任务中序列稀疏、运动幅度大时出现的帧不一致、节奏不稳定和语义错位等问题，提出了Keyframe-anchored Attention Bias和Rescaled Temporal RoPE两种技术，通过关键帧和文本提供语义与时间引导，无需额外训练即可在短序列和长序列上实现最先进的帧一致性、语义保真度和节奏稳定性。同时，作者还构建了首个专门针对文本条件GI评估的基准测试TGI-Bench。

【方法概述 / Method】
本文提出Keyframe-anchored Attention Bias机制，将关键帧和文本的语义与时间引导注入到每个中间帧；同时设计Rescaled Temporal RoPE，通过重新缩放时间位置编码使自注意力更忠实地关注关键帧，从而增强帧间一致性。这两种方法均无需额外训练，可直接应用于预训练模型。

【实验结果 / Results】
在TGI-Bench基准测试上，该方法在多样化挑战中均达到最优性能，显著提升了帧一致性、语义保真度和节奏稳定性，且适用于短序列和长序列场景。实验表明，该方法有效解决了先前GI模型在稀疏序列和大运动情况下的失效问题。

【应用价值 / Applications】
该技术可广泛应用于动画制作、视频内容生成、电影特效等领域，帮助艺术家和创作者基于关键帧和文本描述自动生成高质量的中间过渡帧，大幅提升制作效率并降低人工成本，同时保证生成内容的语义连贯性和视觉一致性。
