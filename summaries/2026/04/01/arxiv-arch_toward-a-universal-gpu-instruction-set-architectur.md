---
title: "Toward a Universal GPU Instruction Set Architecture: A Cross-Vendor Analysis of Hardware-Invariant Computational Primitives in Parallel Processors"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.28793"
published: "2026-04-01"
summarized: "2026-04-02T07:11:33.467707"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究首次系统性地分析了四大主流GPU厂商（NVIDIA、AMD、Intel、Apple）的指令集架构，涵盖16种不同微架构和超过5000页的一手资料。研究识别出10个跨厂商的硬件不变计算原语、6个可参数化的方言差异以及6个真正的架构分歧，并基于此提出了一个与厂商无关的GPU ISA抽象执行模型。该模型在NVIDIA T4和Apple M1两种架构差异最大的平台上进行了验证，在六组基准测试中的五组达到或超越了原生厂商优化性能。

【方法概述 / Method】
研究团队综合分析了官方ISA参考手册、架构白皮书、专利文件以及社区逆向工程成果，采用跨架构比较的方法识别计算原语的共性与差异。通过构建基于并行计算物理约束的抽象执行模型，将硬件特性映射到统一的中间表示层，并在异构硬件平台上实现该模型进行性能验证。

【实验结果 / Results】
在NVIDIA T4和Apple M1平台上，抽象模型在五组基准测试-平台配对中达到或超过原生优化性能。唯一例外是NVIDIA平台上的并行归约操作，性能为原生实现的62.5%，该结果揭示了intra-wave shuffle必须作为强制原语，从而完善了所提出的模型。

【应用价值 / Applications】
该研究为跨厂商GPU编程提供了统一的抽象基础，有望降低异构并行编程的复杂度，促进可移植高性能计算库的开发。所提出的通用ISA框架可应用于编译器中间表示设计、跨平台性能优化工具以及未来开放GPU标准的制定，对打破当前GPU生态的厂商锁定具有重要意义。
