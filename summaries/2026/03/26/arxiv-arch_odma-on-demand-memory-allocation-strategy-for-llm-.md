---
title: "ODMA: On-Demand Memory Allocation Strategy for LLM Serving on LPDDR-Class Accelerators"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2512.09427"
published: "2026-03-26"
summarized: "2026-03-27T07:13:23.440026"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ODMA，一种面向LPDDR类受限随机访问加速器的按需内存分配策略，以解决现有静态预分配和细粒度分页技术在低带宽内存系统上的低效问题。ODMA通过轻量级生成长度预测器、自适应桶分区机制和回退安全池，有效应对生产环境中的分布漂移和重尾请求模式。在Cambricon MLU370-X4上的部署表明，该方法将KV缓存利用率提升19.25%，吞吐量提高23-27%，验证了预测驱动的连续分配策略在LPDDR设备上的有效性。

【方法概述 / Method】
ODMA采用轻量级生成长度预测器，结合自适应桶分区与回退安全池的三层架构：在线直方图动态重新校准桶边界以最大化内存利用率，安全池则为预测误差提供鲁棒性保障。该方法专门针对LPDDR硬件的碎片化与带宽约束进行优化，避免传统分页机制带来的非顺序访问性能损失。

【实验结果 / Results】
在Alpaca和Google-NQ基准测试上，ODMA将S3预测准确率分别从98.60%提升至99.55%、从82.68%提升至93.36%。在Cambricon MLU370-X4加速器部署DeepSeek-R1-Distill-Qwen-7B的实测中，相比静态基线，KV缓存绝对利用率提升19.25%，系统吞吐量（TPS）提升23-27%。

【应用价值 / Applications】
ODMA适用于采用LPDDR等低成本、低功耗内存的AI加速器场景，如边缘计算设备、数据中心推理服务器中的寒武纪MLU系列芯片，可显著降低LLM服务部署的硬件成本与能耗。该策略为资源受限环境下的高效大模型推理提供了可扩展的内存管理方案，对推动LLM在更广泛硬件平台上的普及具有重要意义。
