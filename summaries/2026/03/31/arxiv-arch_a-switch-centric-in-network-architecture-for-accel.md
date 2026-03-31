---
title: "A Switch-Centric In-Network Architecture for Accelerating LLM Inference in Shared-Memory Network"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.28239"
published: "2026-03-31"
summarized: "2026-04-01T07:16:28.581777"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SCIN（Switch-Centric In-Network Architecture），首个面向AI加速器共享内存网络的交换机中心式网络内计算架构，旨在解决NVLink Sharp（NVLS）在LLM推理中存在的通信瓶颈问题。SCIN通过引入能够主动发起内存语义操作的交换机内加速器（ISA）和协同设计的低开销通信架构，消除了冗余数据传输，并支持网络内量化（INQ）将All-Reduce精度降至8位。实验表明，该设计可将All-Reduce加速最高8.7倍（小消息）和3.8倍（大消息），在LLaMA-2模型上实现1.74倍的TTFT提升和1.34倍的TPOT提升。

【方法概述 / Method】
SCIN的核心创新在于将架构范式从"加速器中心"转变为"交换机中心"，使交换机内的ISA能够主动发起内存读写操作，而非被动等待GPU加载指令触发。该架构包含三个关键组件：支持主动内存语义的ISA、集成于ISA的量化模块以实现INQ，以及专为低协议开销设计的协同通信协议栈。

【实验结果 / Results】
在多FPGA原型系统上的评估显示，相比NVLS，SCIN将All-Reduce延迟降低：小消息（≤1KB）场景下最高达8.7倍，大消息场景下达3.8倍；端到端LLM推理性能方面，首token生成时间（TTFT）提升1.74倍，每token生成时间（TPOT）提升1.34倍。INQ机制在几乎不损失精度的情况下将All-Reduce位宽从FP16/BF16压缩至8位，有效带宽接近翻倍。

【应用价值 / Applications】
SCIN适用于大规模分布式LLM推理部署，特别是在多GPU共享内存网络环境中可显著缓解通信瓶颈，降低推理延迟并提升吞吐量。该技术对需要低延迟响应的交互式AI应用（如实时对话系统）以及追求成本效益的云AI服务具有重要价值，同时其网络内量化能力有助于在带宽受限场景下实现更高效的模型部署。
