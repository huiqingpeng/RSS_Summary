---
title: "Cubic Discrete Diffusion: Discrete Visual Generation on High-Dimensional Representation Tokens"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19232"
published: "2026-03-20"
summarized: "2026-03-20T16:07:09.973152"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Cubic Discrete Diffusion (CubiD)，首个针对高维表示（768-1024维）的离散视觉生成模型，突破了现有方法仅限于低维潜在token（8-32维）的局限。CubiD通过在任意位置、任意维度进行细粒度掩码预测，实现了固定步数T的高效生成（T远小于特征维度乘积）。在ImageNet-256上，CubiD取得了离散生成的SOTA性能，并验证了其离散token可同时支持理解与生成任务，为统一多模态架构奠定基础。

【方法概述 / Method】
CubiD采用立方体离散扩散机制，在高维离散表示空间中进行细粒度掩码：任意空间位置的任意维度均可被独立掩码并基于部分观测预测。该方法通过维度级掩码策略，使模型学习空间位置内部及跨位置间的丰富相关性，且生成步数固定为T，与特征维度h×w×d无关。

【实验结果 / Results】
CubiD在ImageNet-256上达到离散生成SOTA性能，模型规模从9亿到37亿参数均呈现良好的扩展性。实验证实，经CubiD离散化后的高维token完整保留了原始表示的语义能力，同一套离散token可有效服务于视觉理解与生成双重任务。

【应用价值 / Applications】
该研究为构建统一的多模态架构提供了关键基础，使视觉生成模型能与语言模型共享相同的token预测范式。高维离散表示同时支持理解与生成的特性，可推动视觉-语言预训练、多模态大模型等方向的发展，实现真正意义上的模态统一。
