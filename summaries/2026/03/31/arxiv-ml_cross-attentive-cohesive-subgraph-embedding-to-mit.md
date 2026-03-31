---
title: "Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in GNNs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27529"
published: "2026-03-31"
summarized: "2026-04-01T07:25:39.030719"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对图神经网络（GNNs）中的oversquashing问题提出解决方案——该问题指长距离信息在有限的消息传递路径中被压缩而失真，限制了模型捕获全局上下文的能力。作者提出了一种新颖的图学习框架，通过跨注意力凝聚子图表示来丰富节点嵌入，在强调长距离信息中凝聚结构的同时去除噪声或无关连接。大量基准数据集实验表明，该模型在分类准确率上相比标准基线方法实现了持续提升。

【方法概述 / Method】
该框架核心在于利用跨注意力机制（cross-attentive mechanism）提取凝聚子图（cohesive subgraph）表示，选择性保留长距离依赖中的结构紧密部分，过滤掉冗余连接。通过这种方式，模型在不超载狭窄瓶颈通道的前提下保留关键全局上下文信息。

【实验结果 / Results】
在多个基准数据集上的广泛实验显示，所提模型在节点分类任务中相比标准基线方法取得一致的准确率提升，验证了其在缓解oversquashing方面的有效性。

【应用价值 / Applications】
该方法可应用于需要捕获长距离依赖的图学习场景，如社交网络分析、分子性质预测和知识图谱推理等领域，特别适用于包含密集连接和异配性（heterophilic）区域的复杂图结构，有望提升GNNs在实际应用中的全局建模能力。
