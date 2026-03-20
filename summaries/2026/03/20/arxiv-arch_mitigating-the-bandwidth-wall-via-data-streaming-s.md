---
title: "Mitigating the Bandwidth Wall via Data-Streaming System-Accelerator Co-Design"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.19057"
published: "2026-03-20"
summarized: "2026-03-20T12:04:39.696802"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对Transformer推理中的"带宽墙"问题，提出了一种系统-加速器协同设计方法，通过分页流式数据流和计算与传输的显式重叠来优化矩阵加速器及其系统集成。研究开发的MatrixFlow加速器采用4KB分块和约20KB片上缓存，配合Gem5-AcceSys仿真平台评估表明，该方法在标准PCIe互联下可达到近80%的HBM性能，相比CPU基线实现最高22倍端到端加速，较现有先进加速器提升5-8倍。

【方法概述 / Method】

硬件方面设计了MatrixFlow加速器，采用16×16松散耦合脉动阵列架构，基于4KB页对齐分块矩阵乘法，配合DMA-计算-DMA输出流水线调度；系统方面开发了Gem5-AcceSys仿真框架，扩展gem5以支持PCIe等标准互联和多种内存层级模式（直接内存、直接缓存、设备内存）及SMMU/TLB效应建模。

【实验结果 / Results】

在BERT和ViT等代表性Transformer模型上的gem5仿真显示，该方法实现最高22倍于CPU基线的端到端加速，相比最先进的松散耦合和紧密耦合加速器分别有5倍和8倍性能提升；关键发现是标准PCIe主机内存设计可达到片上HBM约80%的性能，且分页流式传输与流水线重叠比大容量本地SRAM更能有效提升实际系统约束下的推理效率。

【应用价值 / Applications】

该研究为数据中心和边缘设备中的Transformer推理提供了高性价比的硬件加速方案，证明通过系统-架构协同优化而非依赖昂贵的高带宽内存（HBM）即可突破带宽瓶颈，对降低AI加速器成本、提升基于标准互联（如PCIe）的部署灵活性具有重要实践意义，特别适用于需要平衡性能与成本的大规模AI推理场景。
