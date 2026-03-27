---
title: "The DMA Streaming Framework: Kernel-Level Buffer Orchestration for High-Performance AI Data Paths"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.10030"
published: "2026-03-27"
summarized: "2026-03-28T07:09:21.511645"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 **dmaplane**，一个 Linux 内核模块，用于解决 AI 数据传输库中缺失的缓冲区编排层问题。该框架通过 `/dev/dmaplane` 暴露稳定的内核 UAPI，集成了基于环的命令通道、DMA 缓冲区生命周期管理、跨设备共享的 dma-buf 导出、内核空间 RDMA 引擎、NUMA 感知分配、基于信用的流控制以及 GPU 内存集成等功能。实验评估了 NUMA 跨节点惩罚、RDMA 持续负载下的完成安全流控制、GPU BAR 映射层级与 cudaMemcpy 的对比，并展示了端到端分离式推理场景，通过 RDMA WRITE WITH IMMEDIATE 在两机之间传输 KV-cache 块并在接收端重建张量视图。

【方法概述 / Method】

dmaplane 采用内核级架构设计，将缓冲区编排功能下沉到 Linux 内核空间，避免用户态-内核态频繁切换的开销。核心机制包括：基于环形缓冲区的命令通道实现高效通信、dma-buf 子系统支持跨设备零拷贝共享、内核空间 RDMA 引擎直接操作 DMA 缓冲区、以及通过 PCIe BAR pinning 实现 GPU 内存的直接访问。框架还引入基于信用的流控制确保完成安全（completion-safe），并集成 NUMA 感知分配策略优化内存放置。

【实验结果 / Results】

实验测量了 NUMA 跨节点访问在 DRAM 规模下的性能惩罚，验证了 NUMA 感知分配的必要性；在持续 RDMA 负载下测试了完成安全的流控制机制；对比了 GPU BAR 映射层级与传统 cudaMemcpy 的性能差异。端到端演示成功实现了两台机器间的 KV-cache 分离式传输，使用 RDMA WRITE WITH IMMEDIATE 操作并在接收端重建张量视图。RDMA 测量基于 Soft-RoCE 完成，作者明确区分了实测结果与架构无关的通用属性。

【应用价值 / Applications】

该研究直接面向大规模 AI 推理系统的数据路径优化，特别适用于分离式内存架构（disaggregated memory）和分布式大模型推理场景，可显著降低 KV-cache 等大数据块的跨节点传输延迟。内核级缓冲区编排消除了传统用户态库在缓冲区管理上的假设限制，为需要严格延迟保证和高吞吐的 AI 工作负载提供了可移植、可观测的基础设施层，支持 GPU、RDMA NIC 等多种异构设备的统一数据移动。
