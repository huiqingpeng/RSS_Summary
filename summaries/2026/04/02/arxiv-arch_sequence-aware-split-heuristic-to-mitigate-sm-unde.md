---
title: "Sequence-Aware Split Heuristic to Mitigate SM Underutilization in FlashAttention-3 Low-Head-Count Decoding"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.00028"
published: "2026-04-02"
summarized: "2026-04-03T07:14:44.400504"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对FlashAttention-3在低头数（low-head-count）解码配置下出现的GPU占用率瓶颈问题，提出了一种序列感知分割启发式策略。标准FlashAttention-3仅基于序列长度禁用序列分割，导致Hopper GPU的流式多处理器（SM）利用不足。该研究通过允许低头数场景下的序列级并行性，显著提升了硬件利用率，在元数据启用的推理路径上实现了约21-24%的解码器内核效率提升，且未观察到性能回退。

【方法概述 / Method】
作者提出了一种序列感知分割策略（sequence-aware split policy），替代原有的仅基于序列长度的分割启发式。该方法在低头数解码配置中启用序列级并行性，以更充分地利用Hopper GPU的流式多处理器资源，从而缓解SM利用率不足的问题。

【实验结果 / Results】
实验表明，所提出的序列感知分割启发式策略在元数据启用的推理路径上，可将解码器内核效率提升约21-24%。重要的是，该优化在实现显著性能增益的同时，未引入任何性能回退（no observed regressions）。

【应用价值 / Applications】
该研究对大规模Transformer模型的推理优化具有重要价值，尤其适用于需要低头数配置的场景（如特定模型架构或内存受限部署）。通过提升FlashAttention-3在Hopper GPU上的硬件利用率，该工作可加速LLM推理服务，降低推理成本，并为高效的大模型部署提供支持。
