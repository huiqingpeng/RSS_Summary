---
title: "EmbedPart: Embedding-Driven Graph Partitioning for Scalable Graph Neural Network Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.01000"
published: "2026-04-02"
summarized: "2026-04-03T07:26:43.163033"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出EmbedPart，一种基于嵌入驱动的图分区方法，用于解决大规模图神经网络（GNN）训练中的可扩展性挑战。该方法利用GNN训练过程中产生的节点嵌入，通过对密集嵌入进行聚类来实现图分区，避免了直接在不规则图结构上操作。EmbedPart在保持与Metis相当分区质量的同时实现了100倍以上的加速，并天然支持图动态更新和快速重分区。

【方法概述 / Method】
EmbedPart的核心思想是将分区操作从稀疏的图结构转移到GNN训练过程中已产生的密集节点嵌入上，通过聚类这些嵌入来推导分区方案。该方法无需额外的图遍历或特征工程，直接复用训练时的中间结果，实现了分区过程与GNN训练工作流的深度耦合。

【实验结果 / Results】
实验表明，EmbedPart相比Metis实现了超过100倍的速度提升，同时保持了具有竞争力的分区质量。该方法显著加速了分布式GNN训练，并且能够有效支持图数据的动态更新和快速重分区需求。

【应用价值 / Applications】
EmbedPart可广泛应用于大规模图数据的分布式GNN训练场景，如社交网络分析、知识图谱推理和推荐系统等。此外，该方法还可用于图重排序以提升数据局部性，从而加速单机GNN训练，为图数据优化提供了一种可扩展且高质量的通用解决方案。
