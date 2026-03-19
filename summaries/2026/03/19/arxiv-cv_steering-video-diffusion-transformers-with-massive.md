---
title: "Steering Video Diffusion Transformers with Massive Activations"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17825"
published: "2026-03-19"
summarized: "2026-03-19T16:16:56.674067"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了视频扩散Transformer中的Massive Activations（MAs）——即罕见的高幅度隐藏状态峰值现象。作者发现MAs在所有视觉token中呈现结构化层次：首帧token幅度最大，潜在帧边界token次之，内部token幅度相对温和。基于该发现，提出无需训练的Structured Activation Steering（STAS）方法，通过将首帧和边界token的MA值导向全局最大参考幅度，在可忽略计算开销下显著提升视频质量与时序一致性。

【方法概述 / Method】
STAS是一种类自引导的训练无关方法，利用视频扩散Transformer中MAs的固有空间层次结构。该方法识别首帧和潜在帧边界token作为关键位置，将其激活幅度向缩放后的全局最大参考值进行引导，无需额外训练或模型微调即可实现生成过程的干预控制。

【实验结果 / Results】
STAS在多个文本到视频模型上均实现一致的性能提升，包括视频质量指标（如FVD、IS）和时序连贯性指标的改善。关键优势在于引入的计算开销可忽略不计，同时方法具有模型无关性，可即插即用于不同架构的视频扩散Transformer。

【应用价值 / Applications】
该研究为视频生成质量优化提供了零成本的后处理方案，特别适用于计算资源受限场景下的高质量视频合成。STAS可广泛应用于内容创作、影视制作、游戏动画等领域的文本驱动视频生成系统，也为理解扩散Transformer的内部机制提供了新的分析视角。
