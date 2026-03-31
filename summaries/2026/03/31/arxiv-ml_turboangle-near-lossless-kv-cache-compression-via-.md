---
title: "TurboAngle: Near-Lossless KV Cache Compression via Uniform Angle Quantization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27467"
published: "2026-03-31"
summarized: "2026-04-01T07:24:38.631346"
ai_provider: "openai"
---

【论文摘要 / Abstract】

TurboAngle提出了一种近乎无损的KV缓存压缩方法，通过在Fast Walsh-Hadamard域中对角度进行均匀量化实现压缩。该方法结合逐层"early-boost"技术，为关键层独立配置K和V的码本大小以分配更高精度。在7个模型（1B至7B参数）上的实验表明，该方法在4个模型上实现了无损压缩，在6个模型上达到近无损质量，仅需3.28-3.67角度比特/元素；在Mistral-7B上配合非对称范数量化可达到6.56总比特/元素，困惑度仅增加0.0014且无需校准数据。

【方法概述 / Method】

TurboAngle的核心技术是在Fast Walsh-Hadamard变换域中进行角度量化，利用随机对角旋转使连续元素对在单位圆上近似均匀分布。该方法进一步扩展了逐层early-boost机制，允许独立配置每层K和V的码本大小，将更高精度分配给模型特定的关键层。此外，采用非对称范数量化策略：keys使用8-bit，values使用4-bit对数空间量化。

【实验结果 / Results】

在7个规模从1B到7B参数的模型上，per-layer early-boost在4个模型上实现无损压缩，在6个模型上达到近无损质量，压缩率为3.28-3.67角度比特/元素。在Mistral-7B上的完整方案（含非对称范数量化）达到6.56总比特/元素，困惑度仅增加0.0014，且无需任何校准数据。层组敏感性分析揭示了模型特定的瓶颈模式，包括K主导层、V主导层以及增加精度反而会降低质量的负迁移层。

【应用价值 / Applications】

该研究为大语言模型的KV缓存压缩提供了高效实用的解决方案，可显著降低推理时的内存占用，特别适用于长上下文场景和边缘设备部署。无需校准数据的特性使其便于实际部署，而逐层自适应配置能力为不同模型架构的优化提供了灵活框架。发现的负迁移层等现象也为后续模型架构设计和压缩策略研究提供了重要洞察。
