---
title: "CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Attention"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17946"
published: "2026-03-19"
summarized: "2026-03-19T12:18:29.312004"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出CARE方法，解决将预训练注意力模块（如GQA）转换为多头潜在注意力（MLA）时的关键问题。现有转换方法仅关注权重矩阵的低秩近似，忽视输入激活的协方差结构并采用均匀秩分配，导致激活漂移和注意力保真度下降。CARE通过激活感知分解、自适应秩分配和KV奇偶映射三个核心步骤，在固定KV缓存预算下显著提升转换质量，在Qwen3和Llama-3.1系列模型上实现困惑度最高215倍降低和平均准确率最高1.70倍提升，经简短微调后可完全恢复原始模型性能。

【方法概述 / Method】

CARE提出三项关键技术：（i）激活保持分解，通过考虑输入激活的协方差结构，使低秩近似对齐实际激活而非仅权重矩阵；（ii）自适应秩分配，根据各层需求将固定KV预算非均匀分配，优先保障关键层的表达能力；（iii）KV奇偶映射，重新参数化转换后的K和V矩阵以适配MLA格式，同时保持KV缓存大小不变。

【实验结果 / Results】

在Qwen3-4B/30B-A3B-Instruct-2507和Llama-3.1-8B/70B-Instruct模型上的实验表明，相比均匀秩SVD基线，CARE在匹配KV预算下将一次性困惑度降低高达215倍，平均准确率提升高达1.70倍。经过简短的SVD后修复微调（healing fine-tune），模型可完全恢复原始准确率。

【应用价值 / Applications】

CARE为大规模语言模型的高效推理部署提供实用解决方案，使现有GQA预训练模型能够在不增加KV缓存成本的前提下转换为更具表达力的MLA架构。该方法特别适用于资源受限的推理场景，可显著提升模型在边缘设备和长上下文处理中的效率，为模型压缩与架构迁移提供了新的技术路径。
