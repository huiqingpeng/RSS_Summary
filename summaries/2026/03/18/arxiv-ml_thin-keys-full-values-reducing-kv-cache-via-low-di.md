---
title: "Thin Keys, Full Values: Reducing KV Cache via Low-Dimensional Attention Selection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.04427"
published: "2026-03-18"
summarized: "2026-03-18T17:05:18.190410"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文揭示了Transformer注意力机制中查询/键（用于选择）与值（用于表征传递）的功能不对称性：仅需O(log N)维度即可区分N个相关token类别，远低于值传递所需维度。基于此，作者提出"分解键"方法，通过截断SVD将键投影分解为低维形式，可在无需从头预训练的情况下压缩任意预训练模型的KV缓存。该方法在7B规模模型上实现75%键缓存节省（约2%质量损失），并可与GQA和量化技术结合实现16倍综合压缩。

【方法概述 / Method】

核心方法是对键投影矩阵进行低秩分解：将W_K ≈ A_{d×r}B_{r×d}通过截断SVD分解，其中r = d_select为选择维度；将A作为新的键投影生成紧凑的r维键用于缓存，同时将B^T吸收到查询投影W_Q' = W_Q B^T中（查询无需缓存）。对于现有模型，采用SVD初始化后仅微调QK投影（3轮epoch，<1%预训练数据）即可适配。

【实验结果 / Results】

从头训练7B模型时，r = d_model/4的配置在20B token后达到9.2 PPL（对比完整注意力9.3 PPL），同时减少12%参数并加速8%训练。在GPT-2和Mistral-7B上的迁移实验显示，75%键缓存压缩仅带来约2%质量下降。与GQA和量化结合后，可实现16倍键缓存综合压缩；对于128K上下文的7B模型服务场景，每用户可节省25GB KV缓存，使相同硬件支持并发用户数提升约60%。

【应用价值 / Applications】

该方法可直接应用于已部署的大语言模型服务系统，无需昂贵的重新预训练即可显著降低推理内存瓶颈，特别适合长上下文场景（如128K token）。其与现有压缩技术（GQA、量化）的正交组合特性，为边缘设备部署和规模化云服务提供了灵活的内存-质量权衡方案，在保持模型架构兼容性的同时提升硬件利用率。
