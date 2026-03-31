---
title: "ScoutAttention: Efficient KV Cache Offloading via Layer-Ahead CPU Pre-computation for LLM Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27138"
published: "2026-03-31"
summarized: "2026-04-01T07:22:05.516351"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出ScoutAttention，一种新型KV缓存卸载框架，通过GPU-CPU协同注意力计算加速大语言模型推理。该框架引入层间预计算算法，使CPU提前一层启动注意力计算，并结合异步周期性召回机制，显著降低CPU计算负载。实验表明，ScoutAttention在保持与基线模型精度差距2.4%以内的同时，相比现有卸载方法实现了2.1倍加速。

【方法概述 / Method】
ScoutAttention采用GPU-CPU协同的分块稀疏注意力机制，将KV缓存卸载至DRAM以缓解GPU内存瓶颈。核心创新在于"layer-ahead"预计算策略：CPU提前计算下一层的注意力，与GPU当前层计算流水线并行，避免CPU成为系统瓶颈。

【实验结果 / Results】
ScoutAttention在保持模型精度损失不超过2.4%的前提下，相比现有KV缓存卸载方法实现了2.1倍的推理加速。该结果表明该方法在内存效率与计算效率之间取得了有效平衡。

【应用价值 / Applications】
该研究适用于长上下文LLM推理场景，如文档分析、代码生成和多轮对话系统，能够在有限GPU内存条件下支持更大的批处理规模和更长的序列长度。对于资源受限的部署环境（如边缘设备或云服务器成本优化），ScoutAttention提供了一种实用的内存-计算协同优化方案。
