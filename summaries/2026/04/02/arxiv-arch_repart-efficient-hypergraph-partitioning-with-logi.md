---
title: "RePart: Efficient Hypergraph Partitioning with Logic Replication Optimization for Multi-FPGA System"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.00780"
published: "2026-04-02"
summarized: "2026-04-03T07:14:49.665319"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了RePart，一种面向多FPGA系统（MFS）的定制化多级超图划分框架，通过集成逻辑复制与拓扑感知优化来解决现有方法忽视网络拓扑结构和FPGA资源利用率不足的问题。RePart在Titan23和EDA精英挑战赛基准测试上，相比最先进超图划分器平均减少52.3%的总跳距离，同时实现11.1倍加速，并超越EDA精英挑战赛优胜方案。

【方法概述 / Method】
RePart采用多级超图划分流程，包含三个协同创新组件：FPGA感知动态粗化（根据FPGA资源动态调整粗化策略）、热值引导分配（利用网络拓扑热值指导初始划分）、以及支持复制-删除的精化（允许逻辑复制并在后续优化中选择性删除）。该方法将逻辑复制决策与拓扑信息深度融合到划分的各个阶段。

【实验结果 / Results】
在Titan23和EDA精英挑战赛基准测试上的大量实验表明，RePart相比现有最优超图划分器平均减少52.3%的总跳距离，同时获得11.1倍的运行速度提升；此外，RePart的性能也优于EDA精英挑战赛的获奖方案，验证了其在实际竞赛场景中的优越性。

【应用价值 / Applications】
该研究可直接应用于VLSI仿真和快速原型设计中的多FPGA系统划分，显著降低片间通信延迟并提升FPGA资源利用率；对于需要大规模逻辑划分的电子设计自动化（EDA）工具链具有重要价值，可加速复杂数字系统的硬件验证与原型开发流程。
