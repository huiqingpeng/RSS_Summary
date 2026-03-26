---
title: "TsetlinWiSARD: On-Chip Training of Weightless Neural Networks using Tsetlin Automata on FPGAs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24186"
published: "2026-03-26"
summarized: "2026-03-27T07:21:40.727139"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了TsetlinWiSARD，一种基于Tsetlin自动机的权重less神经网络（WNN）训练方法，通过概率反馈驱动学习克服了传统WiSARD一次性训练的过拟合问题。该方法实现了FPGA上的片上训练架构，在保持硬件高效性的同时达到最先进的精度。相比传统WiSARD实现，训练速度提升超过1000倍；与其他ML算法的FPGA训练加速器相比，资源使用减少22%，延迟降低93.3%，功耗降低64.2%。

【方法概述 / Method】
TsetlinWiSARD采用Tsetlin自动机替代传统WNN的记忆式训练，通过迭代优化和简单的连续二进制反馈机制实现概率性学习。该方法设计了专门的FPGA硬件架构，支持高效的片上训练与推理，避免了传统深度神经网络中复杂的乘累加运算。

【实验结果 / Results】
实验表明，TsetlinWiSARD在精度上达到SOTA水平的同时，实现了显著的硬件效率提升：训练速度较传统WiSARD提升1000倍以上，资源利用率优化22%，训练延迟大幅降低93.3%，功耗减少64.2%。这些指标证明了该方法在边缘计算场景下的优越性能。

【应用价值 / Applications】
该研究适用于对适应性、隐私性和安全性要求极高的边缘智能场景，如物联网设备、嵌入式系统和实时决策应用。其低延迟、低功耗的片上训练能力使其特别适合需要持续学习、数据不出本地的敏感任务，如工业监控、智能传感器和边缘AI安全系统。
