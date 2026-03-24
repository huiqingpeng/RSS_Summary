---
title: "Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20616"
published: "2026-03-24"
summarized: "2026-03-25T07:12:29.019416"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MixedDimKV，一种细粒度的混合维度KV缓存压缩方法，突破了传统token驱逐方法只能将token维度设为0或全维的粗粒度限制。该方法通过为不同token分配不同维度的表示，实现了更高效的内存压缩。实验表明，该方法仅需6.25%的KV缓存即可在LongBench上达到与全注意力相当的性能，在Needle-in-a-Haystack测试中仅用0.26%缓存即可在50K上下文长度下保持100%准确率。

【方法概述 / Method】
MixedDimKV采用混合维度预算分配策略，根据token重要性为其分配不同维度的KV表示，而非简单地保留或丢弃整个token。在此基础上，MixedDimKV-H进一步整合head-level重要性信息，实现更精细的维度分配决策。

【实验结果 / Results】
在不依赖head-level重要性分析的方法中，MixedDimKV优于现有KV缓存压缩方法；在同等head-level信息条件下，MixedDimKV-H持续优于HeadKV。该方法在LongBench长上下文基准上仅用6.25%缓存达到全注意力性能，在50K长度的Needle-in-a-Haystack测试中仅用0.26%缓存保持100%准确率。

【应用价值 / Applications】
该研究显著降低了大语言模型长上下文推理的内存瓶颈，使超长序列处理在资源受限设备上成为可能。可广泛应用于需要处理长文档、代码库、多轮对话等场景的高效推理系统，为边缘设备部署和降低推理成本提供了可行方案。
