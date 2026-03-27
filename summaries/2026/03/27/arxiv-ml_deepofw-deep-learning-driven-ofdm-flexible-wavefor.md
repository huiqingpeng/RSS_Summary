---
title: "DeepOFW: Deep Learning-Driven OFDM-Flexible Waveform Modulation for Peak-to-Average Power Ratio Reduction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23544"
published: "2026-03-27"
summarized: "2026-03-28T07:13:31.198333"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出DeepOFW，一种深度学习驱动的OFDM灵活波形调制框架，通过数据驱动方式设计波形以降低峰均功率比（PAPR），同时保持传统收发器的低复杂度硬件结构。该框架采用全可微架构，支持端到端优化波形生成和接收处理，并将学习阶段限制在离线或中央单元，无需在收发两端部署深度学习推理。实验表明，所学习的波形相比经典OFDM显著降低PAPR，同时比特误码率（BER）性能优于现有先进传输方案。

【方法概述 / Method】

DeepOFW采用完全可微的神经网络架构，实现波形表示与检测参数的联合优化，并在训练过程中显式引入PAPR约束。与传统神经收发器不同，该方法将深度学习推理集中在离线训练阶段，部署时仅需标准硬件执行查表或简单运算，避免实时推理的计算开销。

【实验结果 / Results】

在3GPP多径信道上的大量仿真表明，DeepOFW学习的波形在显著降低PAPR的同时，BER性能优于现有先进传输方案。该框架成功实现了PAPR降低与误码性能改善的双重优化目标，验证了数据驱动波形设计的有效性。

【应用价值 / Applications】

DeepOFW适用于5G/6G移动通信、卫星通信等对功放效率和发射功率受限的多载波系统，可在不更换现有硬件基础设施的前提下提升系统性能。其开源实现有助于推动可重复研究和实际工程部署，为下一代无线通信的波形设计提供灵活高效的解决方案。
