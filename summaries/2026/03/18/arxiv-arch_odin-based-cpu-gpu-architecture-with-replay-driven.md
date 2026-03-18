---
title: "ODIN-Based CPU-GPU Architecture with Replay-Driven Simulation and Emulation"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.16812"
published: "2026-03-18"
summarized: "2026-03-18T15:31:56.075085"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对ODIN集成芯粒架构中的CPU-GPU子系统验证挑战，提出了一种基于确定性波形捕获与重放的验证方法。该方法通过单一设计数据库实现仿真与仿真的跨环境重放，能够在系统级别可靠地复现复杂GPU工作负载和协议序列。研究实现了端到端系统启动和工作负载执行，验证周期缩短至单个季度内，证明了重放验证方法在芯粒系统中的可扩展性和有效性。

【方法概述 / Method】
论文采用确定性波形捕获与重放（replay-driven）验证方法，在仿真和硬件仿真（emulation）环境中共享同一设计数据库。该方法通过记录和重放跨芯粒边界的协议交互波形，解决了非确定性执行带来的调试困难，支持CPU子系统、多Xe GPU核心与可配置片上网络（NoC）的协同验证。

【实验结果 / Results】
验证结果表明，该重放方法显著加速了调试过程并提升了集成可信度。研究团队成功在单个季度内完成了端到端系统启动和完整工作负载执行，大幅缩短了传统芯粒集成所需的验证周期。

【应用价值 / Applications】
该方法适用于大规模AI和图形工作负载所需的CPU-GPU集成芯片的预硅验证，特别是基于芯粒（chiplet）架构的异构系统。其可扩展的验证框架对半导体行业加速复杂SoC设计迭代、降低验证成本具有重要实践价值，为下一代高性能计算芯片的快速上市提供了方法论支撑。
