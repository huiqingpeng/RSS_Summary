---
title: "FlashSampling: Fast and Memory-Efficient Exact Sampling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15854"
published: "2026-03-18"
summarized: "2026-03-18T15:36:21.855424"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了FlashSampling，一种快速且内存高效的精确采样方法，用于解决大词汇量解码中分类分布采样带来的额外内存带宽开销和内核调用问题。该方法通过将采样融合到LM-head矩阵乘法中，避免在HBM中实例化logits张量，实现了精确采样而无需近似。在H100、H200、B200和B300 GPU上的实验表明，该方法在端到端vLLM实验中可将每输出token时间降低最多19%。

【方法概述 / Method】
FlashSampling采用分块（tile-by-tile）计算策略：在芯片上逐块计算logits，添加Gumbel噪声，每行和每词汇块仅保留一个最大值，最后通过小块归约完成采样。该方法利用argmax在分区上的可分解性保证精确性，并通过分层分解分类分布实现了在线和tensor-并行设置下的分组变体。

【实验结果 / Results】
在多种NVIDIA GPU（H100、H200、B200、B300）上，FlashSampling在核级解码工作负载中实现了加速；在端到端vLLM实验中，测试模型上的每输出token时间减少高达19%。该方法将原本受带宽限制的后处理步骤转变为轻量级epilogue，同时保持精确采样无近似。

【应用价值 / Applications】
FlashSampling可直接集成到现代LLM推理框架（如vLLM）中，显著降低大词汇量解码的延迟和内存开销，特别适用于需要高频采样的生成式AI应用。该方法使精确采样成为矩阵乘法的原生组成部分，为高效、可扩展的大语言模型推理提供了新的优化范式。
