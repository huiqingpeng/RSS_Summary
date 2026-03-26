---
title: "HillInfer: Efficient Long-Context LLM Inference on the Edge with Hierarchical KV Eviction using SmartSSD"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2602.18750"
published: "2026-03-26"
summarized: "2026-03-27T07:13:33.218729"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出HillInfer，一种面向边缘AI个人计算机（AIPC）的计算存储驱动器（CSD）辅助KV缓存驱逐框架，通过将轻量级token重要性评估任务卸载到SmartSSD等CSD设备，突破了长上下文LLM推理中的内存瓶颈。该框架采用分层KV缓存管理器（HKM）利用时间局部性和动态token命中率进行物理分区，消除跨设备I/O抖动；并设计自适应预取流水线（APP）平衡CPU与SmartSSD间的评估负载。实验表明，HillInfer在商用AIPC上实现了最高8.56倍的加速，在保持模型精度的同时实现了低延迟、I/O高效的长上下文推理。

【方法概述 / Method】

HillInfer采用"轻量级卸载"范式，将token重要性评估而非计算密集型的精确注意力计算卸载到单个SmartSSD的FPGA上，通过CSD-based Evaluation Configuration（CEC）实现资源高效的近数据处理。核心组件包括：分层KV缓存管理器（HKM）根据时间局部性和动态命中率将KV缓存物理分区为热池和冷池；自适应预取流水线（APP）动态调度CPU与CSD间的评估任务，掩盖异构计算中的拖尾效应。

【实验结果 / Results】

在商用AIPC平台上的广泛实验表明，HillInfer相比最先进的基线方法实现了最高8.56倍的加速，显著优于传统SSD卸载方案（受限于PCIe I/O瓶颈）和单CSD精确注意力方案（面临FPGA资源耗尽问题）。该框架在实现低延迟、I/O高效的长上下文推理的同时，未牺牲模型精度，有效解决了边缘设备上的内存墙问题。

【应用价值 / Applications】

HillInfer可直接部署于内存受限的AI个人计算机（AIPC），支持本地化的低延迟、隐私保护型长上下文LLM推理，适用于智能文档分析、长对话系统、代码生成等需要处理超长序列的边缘AI场景。该研究为在资源受限的边缘设备上高效部署大语言模型提供了可行的系统级解决方案，推动了端侧AI的实用化进程。
