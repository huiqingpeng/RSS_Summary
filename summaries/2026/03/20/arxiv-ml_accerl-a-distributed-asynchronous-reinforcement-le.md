---
title: "AcceRL: A Distributed Asynchronous Reinforcement Learning and World Model Framework for Vision-Language-Action Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18464"
published: "2026-03-20"
summarized: "2026-03-20T12:12:12.878688"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了AcceRL，一个面向大规模视觉-语言-动作（VLA）模型的全异步解耦强化学习框架，通过物理隔离训练、推理和 rollout 消除同步屏障。该框架首次将可插拔、可训练的世界模型集成到分布式异步RL流程中以生成虚拟经验。在LIBERO基准上的实验表明，AcceRL在系统层面实现超线性吞吐量扩展和高效硬件利用，在算法层面则实现了前所未有的样本效率和复杂控制任务中的训练稳定性。

【方法概述 / Method】
AcceRL采用完全异步和物理解耦的架构设计，将模型训练、策略推理和环境交互三个核心组件分离到独立的计算单元中并行执行。框架创新性地引入了一个即插即用的世界模型模块，能够在分布式异步流水线中生成合成数据，从而减少对真实环境交互的依赖。

【实验结果 / Results】
在LIBERO机器人操作基准测试中，AcceRL达到了当前最优（SOTA）性能。系统评估显示其吞吐量随计算资源增加呈现超线性扩展特性，硬件利用率显著提升。算法评估表明，结合世界模型的变体在样本效率上取得突破性进展，并在复杂控制任务中展现出卓越的训练稳定性。

【应用价值 / Applications】
该研究为大规模VLA模型的实际部署提供了高效的分布式训练基础设施，可显著降低机器人强化学习的计算成本和时间开销。其异步架构和世界模型增强特别适用于需要大量交互数据的机器人操作、自动驾驶等真实世界控制任务，有望加速具身智能系统的规模化应用。
