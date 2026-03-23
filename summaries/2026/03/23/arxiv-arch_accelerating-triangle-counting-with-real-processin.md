---
title: "Accelerating Triangle Counting with Real Processing-in-Memory Systems"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2505.04269"
published: "2026-03-23"
summarized: "2026-03-24T07:14:51.670157"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了首个针对UPMEM商用存内计算（PIM）架构的三角形计数（TC）算法，通过顶点着色、水库采样、Misra-Gries摘要和边均匀采样等技术，解决了PIM核心间通信开销和DRAM容量受限等挑战。该实现在处理动态图的坐标列表格式数据时，性能超越了最先进的CPU方案，证明了PIM架构在缓解TC内存瓶颈方面的有效性。

【方法概述 / Method】
论文采用顶点着色技术消除PIM核心间的昂贵通信，利用水库采样应对PIM核心DRAM容量限制，结合Misra-Gries摘要加速高度数节点的三角形计数，并通过边均匀采样实现快速近似结果。这些技术协同适配UPMEM PIM系统的硬件约束。

【实验结果 / Results】
PIM实现在处理动态图的坐标列表（Coordinate List）格式时，性能超过最先进的CPU三角形计数实现。实验表明该方案有效克服了TC工作负载的内存瓶颈问题，在真实PIM硬件上展现了显著加速效果。

【应用价值 / Applications】
该研究可广泛应用于社交网络分析、生物网络分析和网络安全等领域的大规模图计算场景，为内存密集型图算法在新兴PIM硬件上的高效部署提供了实践范例，推动存内计算技术从理论走向实际应用。
