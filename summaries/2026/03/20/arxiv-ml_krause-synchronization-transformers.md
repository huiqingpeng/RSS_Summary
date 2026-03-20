---
title: "Krause Synchronization Transformers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.11534"
published: "2026-03-20"
summarized: "2026-03-20T14:10:51.865475"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种名为 Krause Attention 的新型注意力机制，旨在解决标准 Transformer 中自注意力机制因全局归一化 softmax 权重导致的表示崩溃（representation collapse）和注意力汇聚（attention sink）问题。该机制受有限置信度共识动力学（bounded-confidence consensus dynamics）启发，用基于距离的局部化稀疏交互替代基于相似度的全局聚合，从而促进结构化局部同步而非全局混合。实验表明，该方法在视觉任务（ViT）、自回归生成（MNIST/CIFAR-10）和大语言模型（Llama/Qwen）上均取得一致性能提升，同时将计算复杂度从二次降至线性。

【方法概述 / Method】

Krause Attention 的核心思想源自 Krause 提出的有限置信度共识模型：每个 token 仅与距离足够近（置信度范围内）的邻居进行交互，而非与所有 token 计算注意力权重。具体实现中，作者用基于距离的阈值筛选机制替代传统的 softmax 归一化，使得注意力图天然稀疏且局部化，形成动态演化的局部邻域结构。该方法与近期将 Transformer 建模为相互作用粒子系统的理论相联系，通过有限置信度交互自然调节注意力集中度。

【实验结果 / Results】

在图像分类任务中，Krause ViT 在 CIFAR-10/100 和 ImageNet 上达到与标准 ViT 相当或更优的准确率，同时显著降低计算量；在自回归图像生成任务中，Krause Transformer 在 MNIST 和 CIFAR-10 上展现出更稳定的训练动态和更好的样本质量；在大语言模型微调实验中，基于 Llama 和 Qwen 的 Krause 变体在保持下游任务性能的同时，有效缓解了注意力汇聚现象，且推理速度因线性复杂度而获得实质性提升。

【应用价值 / Applications】

Krause Attention 为构建高效、可扩展的 Transformer 架构提供了新的归纳偏置，特别适用于长序列建模场景（如高分辨率图像处理、长文档理解、基因组序列分析等），可将计算成本从二次降至线性。其缓解注意力汇聚的特性也有助于提升大语言模型的训练稳定性和推理可靠性，为资源受限环境下的模型部署提供可行方案。此外，该方法与粒子系统理论的关联为理解深度网络动力学开辟了新的分析视角。
