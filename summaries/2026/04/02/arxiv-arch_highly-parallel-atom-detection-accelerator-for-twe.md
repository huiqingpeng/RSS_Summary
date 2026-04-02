---
title: "Highly-Parallel Atom-Detection Accelerator for Tweezer-Based Neutral Atom Quantum Computers"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.00816"
published: "2026-04-02"
summarized: "2026-04-03T07:15:17.765307"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对中性原子量子计算机（NAQCs）中耗时最长的原子检测与状态测量问题，提出了一种高度并行的原子检测加速器。该设计基于现有的状态重建方法，结合算法级优化与FPGA实现，最大化并行性以缩短图像分析时间。在Xilinx UltraScale+ FPGA上的测试表明，该加速器可在115微秒内分析256×256像素的荧光图像，相比原始CPU基线实现34.9倍加速，相比优化后的CPU基线仍有6.3倍提升，且能在不同原子阵列规模下保持稳定的资源利用率。

【方法概述 / Method】
论文采用算法-硬件协同设计方法，将状态重建算法映射至FPGA架构以实现大规模并行计算。为克服FPGA实现中的可扩展性挑战，引入了预取机制（prefetching）并定制总线传输以支持高带宽需求，从而优化数据流和内存访问效率。

【实验结果 / Results】
在Xilinx UltraScale+ FPGA平台上，该加速器处理256×256像素图像仅需115微秒，达到34.9倍于原始CPU实现、6.3倍于优化CPU实现的加速比。关键优势在于资源利用率不随原子阵列尺寸变化而显著波动，展现出良好的可扩展性。

【应用价值 / Applications】
该加速器可直接集成至中性原子量子计算机的控制系统，显著缩短量子计算周期中的测量瓶颈时间，推动大规模、全集成FPGA控制系统的实用化。其低延迟特性对需要快速反馈的量子纠错和动态重配置等实时量子控制任务具有重要价值。
