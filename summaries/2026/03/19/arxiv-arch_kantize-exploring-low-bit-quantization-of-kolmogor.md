---
title: "KANtize: Exploring Low-bit Quantization of Kolmogorov-Arnold Networks for Efficient Inference"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.17230"
published: "2026-03-19"
summarized: "2026-03-19T12:03:19.049847"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文首次系统研究了低比特量化对Kolmogorov-Arnold网络（KANs）的影响，发现B-spline系数可量化至2-3比特而精度损失可忽略。研究提出用低比特量化预计算表替代递归B-spline算法，在保持精度的同时显著降低计算复杂度。ResKAN18实现了50倍的BitOps缩减，且在GPU、FPGA和ASIC平台上均获得显著的推理加速与资源效率提升。

【方法概述 / Method】
论文采用标准量化技术对KANs中的B-spline系数进行低比特（2-8比特）量化，并探索用预计算查找表替代实时递归B-spline计算。该方法通过离线计算和存储量化后的B-spline基函数值，将复杂的 spline 求值转化为高效的表查询操作。

【实验结果 / Results】
实验表明B-spline系数量化至2-3比特时精度损失可忽略，ResKAN18实现50倍BitOps降低而无精度损失。8比特预计算查找表在GPU上带来最高2.9倍推理加速；在FPGA脉动阵列加速器上，将表精度从8比特降至3比特可减少36%资源占用、提升50%时钟频率和1.24倍加速；28nm FD-SOI ASIC上，16比特降至3比特实现72%面积缩减和50%最高频率提升。

【应用价值 / Applications】
该研究为KANs在边缘计算、移动设备和嵌入式系统等资源受限场景的高效部署提供了可行路径，使KANs在保持MLP替代优势的同时获得媲美甚至超越传统量化神经网络的硬件效率。预计算查找表方法特别适合定制化硬件加速，有望推动KANs从研究原型向实际AI芯片应用转化。
