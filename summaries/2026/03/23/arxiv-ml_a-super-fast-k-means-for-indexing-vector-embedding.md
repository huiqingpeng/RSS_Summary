---
title: "A Super Fast K-means for Indexing Vector Embeddings"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20009"
published: "2026-03-23"
summarized: "2026-03-24T07:23:59.468982"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SuperKMeans，一种专为高维向量嵌入聚类设计的k-means变体算法。该算法在现代CPU上比FAISS和Scikit-Learn快达7倍，在GPU上比cuVS快达4倍，同时保持向量相似性搜索任务中质心的质量。加速来源于通过可靠高效地剪枝无需维度来减少数据访问和计算开销，并引入了"按召回率早停"的新机制，在质心质量停止提升时提前终止迭代，进一步缩短运行时间。

【方法概述 / Method】
SuperKMeans通过智能剪枝技术，识别并跳过对向量分配到质心无关紧要的维度，显著降低数据访问和计算开销。同时提出"按召回率早停"（Early Termination by Recall）机制，监控质心在检索任务中的质量变化，当迭代不再带来质量提升时自动终止算法。

【实验结果 / Results】
SuperKMeans在现代CPU上实现相比FAISS和Scikit-Learn最高7倍的加速，在GPU上相比cuVS最高4倍的加速，同时保持与标准k-means相当的质心质量。早停机制在实际应用中进一步减少了运行时间，且未对检索质量造成负面影响。

【应用价值 / Applications】
该研究可广泛应用于大规模向量数据库的索引构建，如语义搜索、推荐系统和RAG（检索增强生成）等需要高效相似性搜索的场景。SuperKMeans显著降低了高维嵌入聚类的时间和计算成本，使实时或大规模向量索引变得更加可行和经济。
