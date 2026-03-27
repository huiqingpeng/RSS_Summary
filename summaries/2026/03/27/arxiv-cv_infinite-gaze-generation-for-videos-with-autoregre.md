---
title: "Infinite Gaze Generation for Videos with Autoregressive Diffusion"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24938"
published: "2026-03-27"
summarized: "2026-03-28T07:18:42.413840"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种用于任意长度视频的无限时域原始注视点预测生成框架。该研究利用自回归扩散模型，合成具有连续空间坐标和高分辨率时间戳的注视轨迹，并以显著性感知的视觉潜在空间为条件。实验表明，该方法在长程时空准确性和轨迹真实性方面显著优于现有方法，突破了传统模型仅适用于3-5秒短时窗口的限制。

【方法概述 / Method】
论文采用自回归扩散模型（autoregressive diffusion model）作为核心生成架构，通过逐步去噪的方式生成注视轨迹序列。模型以显著性感知的视觉潜在空间（saliency-aware visual latent space）为条件，将视觉内容编码为低维表示以指导注视点的生成，从而实现对任意长度视频的连续预测。

【实验结果 / Results】
定量和定性评估表明，该方法在长程时空准确性（long-range spatio-temporal accuracy）和轨迹真实性（trajectory realism）方面显著优于现有方法。模型成功捕捉了真实世界内容中固有的长程行为依赖关系，突破了传统方法受限于短时窗口的瓶颈。

【应用价值 / Applications】
该研究可应用于场景理解、多模态交互、人机交互界面优化、虚拟现实/增强现实中的注视渲染，以及视频内容分析和推荐系统等领域。无限时域预测能力使其特别适用于长视频分析、实时监控和需要持续注意力建模的交互式应用场景。
