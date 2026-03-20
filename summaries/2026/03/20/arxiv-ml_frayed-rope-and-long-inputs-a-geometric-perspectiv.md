---
title: "Frayed RoPE and Long Inputs: A Geometric Perspective"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18017"
published: "2026-03-20"
summarized: "2026-03-20T12:05:00.718742"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文从几何视角揭示了旋转位置编码（RoPE）在长输入场景下性能崩溃的根本原因：RoPE 导致键/查询向量聚类分离被破坏，从而抑制了"汇聚token"（sink tokens）的正常功能。基于此发现，作者提出了 RoPE-ID（In Distribution）方法，通过对部分通道应用高频 RoPE，使模型无需额外训练即可泛化到更长输入。实验表明，该方法在 1B 和 3B 参数的 Transformer 上显著提升了 LongBench 和 RULER 长文本基准测试的性能。

【方法概述 / Method】
论文通过实证与理论分析，建立了 RoPE 注意力机制的统一几何理解框架，发现注意力会诱导分离的键/查询潜在点云产生紧密聚类。基于此，提出 RoPE-ID 改进方案：选择部分通道应用高频 RoPE，其余通道保持低频或固定编码，以维持键/查询聚类的分离性。

【实验结果 / Results】
在 1B 和 3B 参数规模的 Transformer 模型上，RoPE-ID 在 LongBench 和 RULER 信息检索基准测试中展现出有效性，实现了开箱即用（out of the box）的长输入泛化能力，无需针对长文本进行额外微调或训练。

【应用价值 / Applications】
该研究为大型语言模型处理长上下文任务（如长文档理解、多轮对话、代码生成）提供了即插即用的位置编码解决方案，降低了长文本推理的计算成本与部署门槛，对提升现有预训练模型的长序列能力具有重要实践意义。
