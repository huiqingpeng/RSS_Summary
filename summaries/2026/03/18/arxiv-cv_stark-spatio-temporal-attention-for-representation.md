---
title: "STARK: Spatio-Temporal Attention for Representation of Keypoints for Continuous Sign Language Recognition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16163"
published: "2026-03-18"
summarized: "2026-03-18T18:07:27.980041"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对连续手语识别（CSLR）任务，提出了一种统一的空间-时间注意力网络STARK。该网络通过同时计算关键点之间的空间注意力和局部窗口内的时间注意力，生成具有局部上下文感知的空间-时间表示。与现有基于关键点的最先进方法相比，所提出的编码器参数量减少了约70-80%，同时在Phoenix-14T数据集上达到了可比的性能。

【方法概述 / Method】
STARK采用统一的注意力机制，将空间交互（跨关键点）和时间动态（局部时间窗口）整合到单一框架中，替代了传统的图卷积网络与1D卷积分割编码的设计。该网络通过聚合空间和时间维度的注意力分数，直接生成局部上下文感知的空间-时间特征表示。

【实验结果 / Results】
在Phoenix-14T数据集上的实验表明，STARK在大幅压缩模型参数（减少70-80%）的同时，保持了与现有基于关键点的最先进方法相当的识别性能，验证了轻量化设计与有效特征提取之间的良好平衡。

【应用价值 / Applications】
该研究为手语识别系统提供了高效轻量的解决方案，特别适用于资源受限的实时应用场景，如移动设备上的手语翻译工具和辅助听障人士交流的智能系统，有助于推动手语技术的普及和可及性。
