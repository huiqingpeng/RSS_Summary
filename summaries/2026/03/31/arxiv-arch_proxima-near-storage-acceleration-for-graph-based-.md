---
title: "Proxima: Near-storage Acceleration for Graph-based Approximate Nearest Neighbor Search in 3D NAND"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2312.04257"
published: "2026-03-31"
summarized: "2026-04-01T07:17:14.311706"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Proxima，一种基于近存储处理（NSP）的图近似最近邻搜索（ANNS）加速方案，通过在3D NAND闪存中进行算法-硬件协同设计来解决图基ANNS的高内存占用和昂贵距离计算问题。Proxima利用距离近似和早期终止技术显著降低图搜索复杂度，并通过异构集成技术在3D NAND中实现。评估结果表明，与CPU/GPU上的图ANNS相比，Proxima在吞吐量或能效方面实现了数量级提升，比现有ASIC设计快7-13倍，同时在准确性、效率和存储密度之间取得了良好平衡。

【方法概述 / Method】
Proxima采用算法-硬件协同设计方法，在算法层面引入距离近似和早期终止机制以降低搜索复杂度；在硬件层面，利用异构集成技术将搜索算法直接实现在3D NAND闪存中，并设计了定制化的数据流和优化的数据分配方案以最大化3D NAND的带宽利用率。

【实验结果 / Results】
与CPU和GPU上的图ANNS相比，Proxima在吞吐量或能效方面实现了数量级（magnitude）的改进；与现有ASIC设计相比，Proxima实现了7倍到13倍的加速；与先前的近存储处理加速器相比，Proxima在准确性、效率和存储密度之间取得了更好的平衡。

【应用价值 / Applications】
Proxima可广泛应用于推荐系统、信息检索和语义搜索等依赖大规模近似最近邻搜索的数据密集型应用场景，特别适合需要高存储密度、高能效和高吞吐量的边缘或数据中心部署环境。
