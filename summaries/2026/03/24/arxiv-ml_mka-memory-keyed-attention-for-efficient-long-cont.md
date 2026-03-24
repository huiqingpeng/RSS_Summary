---
title: "MKA: Memory-Keyed Attention for Efficient Long-Context Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20586"
published: "2026-03-24"
summarized: "2026-03-25T07:11:54.336064"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Memory-Keyed Attention (MKA)，一种用于高效长上下文推理的分层注意力机制。MKA通过整合多级KV缓存（本地、会话和长期）并动态路由注意力，解决了大KV缓存带来的内存瓶颈问题。作者进一步提出了Route-Fused MKA (FastMKA)变体，在注意力计算前融合记忆源以提升效率。实验表明，FastMKA在保持与MLA相当困惑度的同时，实现了最高5倍的训练吞吐量和1.8倍的评估延迟降低。

【方法概述 / Method】
MKA采用分层架构管理多级KV缓存，使模型能够根据上下文动态选择不同时间尺度的记忆源进行注意力计算。FastMKA通过广播路由机制预先融合记忆源，避免了动态路由的运行时开销，在保证表示质量的同时显著提升了计算效率。

【实验结果 / Results】
在不同序列长度上的实验显示，FastMKA实现了精度与效率的优异平衡：困惑度与MLA相当，训练吞吐量提升最高达5倍，评估延迟降低1.8倍。这些结果表明MKA框架在长上下文注意力任务中具有实用性和可扩展性。

【应用价值 / Applications】
MKA特别适用于需要处理超长上下文的场景，如多轮对话系统、长文档理解与生成、代码辅助工具等。该机制显著降低了长序列训练和推理的计算成本，使大规模语言模型在实际部署中更加高效经济，为构建可扩展的长上下文AI应用提供了实用解决方案。
