---
title: "Graph Signal Processing Meets Mamba2: Adaptive Filter Bank via Delta Modulation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22333"
published: "2026-03-25"
summarized: "2026-03-26T07:12:35.920253"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了HADES（Hierarchical ADaptive filter bank for Efficient SSMs），一种受图信号处理（GSP）启发的框架，将Mamba2重新解释为线图上的自适应滤波器组。该分层架构通过结构化偏置参数Δ引入共享滤波器（全局低通）和专家滤波器（局部高通），在语言建模、常识推理和长上下文检索等基准测试中达到与Mamba2相当的性能，但仅使用58.9%的原始参数，实现了高效、分层且可解释的SSM滤波。

【方法概述 / Method】
HADES将Mamba2的多头递推结构重新建模为线图上的自适应滤波器组，通过分层设计实现：底层使用共享滤波器捕获全局低频信息，上层使用专家滤波器处理局部高频细节。核心创新在于对Mamba2的关键参数Δ施加结构化偏置，实现频率选择性的自适应调制，从而替代传统的多头独立递推机制。

【实验结果 / Results】
HADES在多个基准测试上取得与Mamba2基线相当的表现，同时显著减少参数量至原模型的58.9%。实验覆盖语言建模、常识推理和长上下文检索任务，验证了该方法在保持模型容量的同时实现高效压缩，证明了GSP启发的滤波器组设计在序列建模中的有效性。

【应用价值 / Applications】
该研究为状态空间模型提供了新的理论视角和实用优化路径，适用于需要高效长序列建模的场景，如大规模语言模型、文档分析和实时流数据处理。HADES的参数量削减特性使其特别适合资源受限环境下的部署，同时其可解释的滤波结构有助于理解SSM的内部工作机制。
