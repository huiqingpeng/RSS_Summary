---
title: "SISA: A Scale-In Systolic Array for GEMM Acceleration"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.29913"
published: "2026-04-01"
summarized: "2026-04-02T07:11:25.231963"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对大语言模型（LLMs）中输入相关且高度倾斜的矩阵形状导致传统方形脉动阵列（SA）资源利用率低下的问题，提出了SISA（Scale-In Systolic Array）架构。该架构将传统方形阵列划分为水平矩形条带，以最小开销实现对小规模或倾斜矩阵的并行独立调度，同时保留全阵列操作能力以处理大型GEMM运算。实验表明，SISA在代表性LLM工作负载上相比同等PE数量的最先进单片式SA可实现最高8.52倍加速和93%的能量延迟积（EDP）降低。

【方法概述 / Method】
SISA采用创新的水平矩形条带划分策略，将传统方形脉动阵列重构为可独立调度的多个子阵列。该设计通过灵活的调度机制，使不同条带能够同时处理多个小规模GEMM或协同执行大型GEMM，从而在硬件层面实现动态资源分配与负载均衡。

【实验结果 / Results】
在代表性大语言模型工作负载评估中，SISA相比同等规模的传统单片式脉动阵列实现了最高8.52倍的性能加速，同时获得93%的能量延迟积（EDP）降低。这些结果表明SISA在处理现代LLM中常见的倾斜矩阵形状时具有显著的效率优势。

【应用价值 / Applications】
SISA架构可直接应用于AI/ML加速器芯片设计，特别适用于需要高效处理多样化矩阵形状的大语言模型推理与训练场景。该研究为下一代神经网络加速器提供了可扩展的硬件架构方案，有助于提升数据中心和边缘设备上LLM部署的能效比和吞吐量。
