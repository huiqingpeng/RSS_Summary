---
title: "Structured SIR: Efficient and Expressive Importance-Weighted Inference for High-Dimensional Image Registration"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17415"
published: "2026-03-19"
summarized: "2026-03-19T13:12:14.233642"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为 Structured SIR 的高效高维图像配准推理方法，通过结合采样重要性重采样（SIR）算法与新颖的内存高效协方差参数化（低秩协方差与稀疏空间结构Cholesky精度因子之和），解决了变分推断因后验形式假设受限而导致的表征不足、过度自信和低质量采样问题。该方法在3D脑部MRI密集配准任务中实现了显著更优的校准不确定性估计，同时保持相当或更好的精度，并能有效捕获高度结构化的多模态后验分布。

【方法概述 / Method】
核心方法采用 Sampled Importance Resampling（SIR）算法进行重要性加权推断，并创新性地将高维协方差矩阵参数化为低秩分量与稀疏空间结构Cholesky精度因子的组合，从而在表达复杂空间相关性的同时保持计算可处理性。

【实验结果 / Results】
在3D脑部MRI密集配准这一极高维问题上，所提方法产生的确定性估计相比变分方法具有显著更优的校准性，同时达到相当或更优的配准精度；模型能够有效生成高质量样本，并揭示高度结构化的多模态后验分布。

【应用价值 / Applications】
该方法适用于医学影像分析中的高维密集配准任务（如脑部MRI配准），可为临床诊断和手术规划提供更可靠的不确定性量化和多模态解表征；其内存高效的特性使其能够扩展至实际临床场景中大规模3D医学图像的处理需求。
