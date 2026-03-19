---
title: "Efficient Diffusion as Low Light Enhancer"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2410.12346"
published: "2026-03-19"
summarized: "2026-03-19T16:23:42.789911"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对基于扩散模型的低光照图像增强（LLIE）中迭代采样过程计算负担重的问题，提出了ReDDiT框架。作者识别出导致加速方法性能下降的两个关键因素：拟合误差和推理差距，并分别通过线性外推错误分数函数和将高斯流迁移到反射感知残差空间来解决。该框架仅需2步即可达到传统多步扩散方法的性能，在4步或8步时实现新的SOTA结果。

【方法概述 / Method】
本文设计了反射感知轨迹精化（RATR）模块，利用图像的反射分量来精化教师轨迹；在此基础上构建了ReDDiT（Reflectance-aware Diffusion with Distilled Trajectory）蒸馏框架，通过知识蒸馏将多步扩散模型压缩为高效的少步推理模型。

【实验结果 / Results】
在10个基准数据集上的综合实验表明，ReDDiT在2步推理时即可媲美传统多步扩散方法的性能，在4步或8步时达到新的SOTA水平，显著优于现有最先进方法，同时大幅降低了计算开销。

【应用价值 / Applications】
该研究为实时低光照图像增强提供了高效解决方案，可广泛应用于夜间监控、自动驾驶视觉系统、移动设备摄影等需要快速高质量图像增强的场景，解决了扩散模型在实际部署中的效率瓶颈问题。
