---
title: "Q-Drift: Quantization-Aware Drift Correction for Diffusion Model Sampling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18095"
published: "2026-03-20"
summarized: "2026-03-20T13:08:38.456296"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出Q-Drift，一种针对扩散模型后训练量化（PTQ）的采样器端漂移校正方法。该方法将量化误差建模为去噪过程中的隐式随机扰动，推导出保持边缘分布的漂移调整策略。仅需约5次全精度/量化模型配对的校准运行即可估计时间步方差统计量，且校正模块可与主流采样器、扩散模型和PTQ方法即插即用。实验表明，Q-Drift在多种设置下显著改善量化模型的FID指标，最高可在PixArt-Sigma（SVDQuant W3A4）上降低4.59 FID，同时保持CLIP分数。

【方法概述 / Method】

Q-Drift从概率角度重新解释量化误差：将其视为每个去噪步骤上的加性随机扰动，通过推导修正后的漂移项来保持边际分布不变。具体实现上，该方法在校准阶段计算各时间步的量化噪声方差统计量，并在推理时将此方差纳入采样器的漂移校正，无需修改模型权重或重新训练。

【实验结果 / Results】

研究在6个文本到图像模型（涵盖DiT和U-Net架构）、3种采样器（Euler、flow-matching、DPM-Solver++）及2种PTQ方法（SVDQuant、MixDQ）上进行了广泛验证。Q-Drift在绝大多数设置中优于量化基线，典型提升包括：PixArt-Sigma（SVDQuant W3A4）FID降低4.59，且CLIP评分保持稳定；推理开销可忽略不计。

【应用价值 / Applications】

Q-Drift为大规模扩散模型的高效部署提供了实用解决方案，特别适用于需要低比特量化（如W3A4）的边缘设备和实时生成场景。其即插即用特性使其可无缝集成到现有量化框架和采样流程中，降低内存与计算成本的同时维持生成质量，推动扩散模型在资源受限环境中的普及应用。
