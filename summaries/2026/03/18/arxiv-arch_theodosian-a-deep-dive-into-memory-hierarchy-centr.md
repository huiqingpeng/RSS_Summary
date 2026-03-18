---
title: "Theodosian: A Deep Dive into Memory-Hierarchy-Centric FHE Acceleration"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2512.18345"
published: "2026-03-18"
summarized: "2026-03-18T15:32:12.721152"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文对现代GPU上的CKKS全同态加密方案进行了微架构分析，发现其主要计算内核受限于L2缓存带宽而非传统DRAM瓶颈，并揭示了低硬件利用率源于内核内并行度不足。基于此，作者提出Theodosian优化框架，通过内存感知优化提升缓存效率，在RTX 5090上将32,768个复数的自举延迟从22.1ms降至12.8ms，创下GPU加速FHE的新性能纪录。

【方法概述 / Method】

研究采用微架构剖析方法定位CKKS在GPU上的性能瓶颈，重点分析内存层次结构（特别是L2缓存）和内核级并行特征。Theodosian框架包含一系列互补的内存感知优化技术，包括缓存效率优化和运行时开销削减，并辅以算法级优化进一步提升性能。

【实验结果 / Results】

Theodosian在代表性CKKS工作负载上相比高度优化的基线Cheddar实现1.45–1.83倍加速；在NVIDIA RTX 5090上，基础优化将自举延迟从22.1ms降至15.2ms，结合额外算法优化后进一步降至12.8ms，达到当前最优GPU性能水平。

【应用价值 / Applications】

该研究为云和边缘环境中的隐私保护计算提供了高性能FHE加速方案，可支持加密机器学习、安全多方计算等应用场景；其内存层次优化方法对GPU加速其他内存密集型密码学工作负载具有借鉴意义，有助于推动全同态加密在隐私计算领域的实用化部署。
