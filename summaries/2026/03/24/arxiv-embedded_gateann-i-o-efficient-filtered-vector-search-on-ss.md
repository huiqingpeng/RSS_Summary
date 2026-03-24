---
title: "GateANN: I/O-Efficient Filtered Vector Search on SSDs"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.21466"
published: "2026-03-24"
summarized: "2026-03-25T07:06:17.212790"
ai_provider: "openai"
---

【论文摘要 / Abstract】
GateANN 是一种 I/O 高效的 SSD 存储图索引近似最近邻搜索（ANNS）系统，支持在未修改的图索引上进行过滤向量搜索。现有系统要么因后过滤浪费 I/O，要么需要昂贵的过滤感知索引重建。GateANN 通过将图遍历与向量检索解耦，实现了无需重建索引的高效过滤搜索，最多可减少 10 倍 SSD 读取量并提升 7.6 倍吞吐量。

【方法概述 / Method】
GateANN 的核心技术是"图隧道（graph tunneling）"：利用遍历节点仅需邻居列表和近似距离、无需全精度向量的特性，在内存中预先检查每个节点的过滤谓词，对不匹配节点完全在内存中路由，保持图连通性而不产生 SSD 读取。该方法将图遍历与精确的向量距离计算分离，避免为过滤掉的节点发起 I/O 请求。

【实验结果 / Results】
实验表明，相比现有 SSD 存储的 ANNS 系统，GateANN 可将 SSD 读取量降低最高 10 倍，吞吐量提升最高 7.6 倍。该系统在不修改底层图索引结构的前提下，显著改善了过滤向量搜索的 I/O 效率和整体性能。

【应用价值 / Applications】
GateANN 适用于大规模向量数据库场景，如电商推荐（按价格/品牌过滤）、多媒体检索（按标签/时间过滤）和 RAG 系统（按权限/元数据过滤），能够在 SSD 存储约束下支持高效的属性条件向量搜索，降低存储成本的同时保证查询性能，特别适合云原生和边缘部署的向量检索服务。
