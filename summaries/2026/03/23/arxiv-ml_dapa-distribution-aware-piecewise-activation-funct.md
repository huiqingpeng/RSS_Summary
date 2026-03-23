---
title: "DAPA: Distribution Aware Piecewise Activation Functions for On-Device Transformer Inference and Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19338"
published: "2026-03-23"
summarized: "2026-03-24T07:17:37.778054"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了分布感知分段激活函数（DAPA），一种针对Transformer架构的可微分且硬件友好的激活函数。DAPA通过利用预激活数据的分布特性，采用非均匀分段近似方法，在高概率区域分配更精细的线段，从而提升泛化能力。该近似结果进一步通过分布加权均方误差进行量化，以降低硬件部署的延迟和资源消耗。

【方法概述 / Method】
DAPA的核心方法包括两个关键步骤：首先，基于预激活数据的实际分布构建非均匀分段线性近似，在数据密集区域使用更细的粒度以保证精度，在稀疏区域使用较粗的粒度以节省计算；其次，采用分布加权均方误差（DWMSE）作为量化损失函数，使量化过程更关注高频出现的数值区域。

【实验结果 / Results】
在HLS（高层次综合）硬件实现中，DAPA将GELU计算速度提升了16倍，DSP（数字信号处理器）利用率降低了16倍。在视觉Transformer和GPT-2模型上的实验表明，DAPA在显著加速推理的同时，保持了与原始模型相当甚至更优的性能表现。

【应用价值 / Applications】
DAPA特别适用于资源受限的边缘设备上的Transformer推理与训练场景，如智能手机、物联网设备和嵌入式AI系统。该研究为在能耗和算力受限的硬件上部署大规模Transformer模型提供了高效的激活函数替代方案，有望推动端侧AI的普及和能效优化。
