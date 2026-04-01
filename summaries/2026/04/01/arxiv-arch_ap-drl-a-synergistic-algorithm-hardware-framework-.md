---
title: "AP-DRL: A Synergistic Algorithm-Hardware Framework for Automatic Task Partitioning of Deep Reinforcement Learning on Versal ACAP"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.29369"
published: "2026-04-01"
summarized: "2026-04-02T07:10:57.102786"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了AP-DRL，一个面向AMD Versal ACAP异构架构的自动任务划分框架，用于加速深度强化学习（DRL）训练。该框架解决了DRL训练中的两大核心挑战：不同DRL算法及操作间计算强度的显著差异导致的硬件平台选择困难，以及DRL宽动态范围在传统FP16+FP32混合精度量化下产生的严重奖励误差问题。AP-DRL通过设计空间探索分析和整数线性规划（ILP）模型实现智能的任务划分，并协调CPU（FP32）、FPGA（FP16）和AI引擎（BF16）的混合精度计算。实验表明，该框架相比可编程逻辑基线最高可实现4.17倍加速，相比AI引擎基线最高可实现3.82倍加速，同时保持训练收敛性。

【方法概述 / Method】

AP-DRL采用软硬件协同设计方法，首先对CPU、FPGA和AI引擎（AIE）在不同DRL工作负载下的性能瓶颈进行系统分析，以指导组件间任务划分和量化优化的设计原则。框架核心包含基于设计空间探索的性能分析模块和基于ILP的自动划分模型，后者根据计算特性将DRL操作匹配到最优计算单元；同时利用Versal ACAP原生支持的多种精度格式，实现FP32/FP16/BF16的硬件感知算法级协调。

【实验结果 / Results】

综合实验表明，AP-DRL在多种DRL工作负载上取得了显著的性能提升：相比纯FPGA（可编程逻辑）实现最高获得4.17倍加速，相比纯AI引擎实现最高获得3.82倍加速。关键的是，该框架在实现大幅加速的同时，成功保持了DRL训练的收敛性，避免了因混合精度引入的奖励误差问题。

【应用价值 / Applications】

AP-DRL可广泛应用于需要高效DRL训练的边缘计算和嵌入式智能系统，如机器人控制、自动驾驶决策和实时游戏AI等场景。该框架的自动任务划分能力降低了开发者在异构硬件上部署DRL的门槛，而其硬件感知的混合精度优化为资源受限环境下的大规模DRL训练提供了可行的加速方案，对推动DRL在工业界的实际部署具有重要价值。
