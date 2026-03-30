---
title: "VolTune: A Fine-Grained Runtime Voltage Control Architecture for FPGA Systems"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.26147"
published: "2026-03-30"
summarized: "2026-03-31T07:16:39.889725"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了VolTune，一种开源的细粒度运行时电压控制架构，用于解决FPGA系统中固定供电电压导致的能效受限问题。该架构通过FPGA集成的控制逻辑抽象底层PMBus操作，实现了运行时电压调节，并提供硬件和软件两种控制路径以平衡确定性与可编程性。在Kintex-7平台的GTX收发器供电轨案例研究中，VolTune在允许误码率达10e-6的条件下，实现了最高约29.3%的供电轨功耗降低，同时保持低于2%的静态功耗开销和FPGA资源开销。

【方法概述 / Method】
VolTune采用FPGA集成的控制逻辑直接操作电源管理总线（PMBus），通过硬件路径实现确定性低延迟控制，同时提供软件路径以增强灵活性。该架构将低层电源管理操作抽象为高层接口，使设计者无需深入了解PMBus协议细节即可实现运行时电压调节。

【实验结果 / Results】
硬件控制路径的端到端电压转换延迟实测为2.3毫秒，控制器增加的静态功耗开销和FPGA资源开销均低于2%。在10.0 Gbps传输速率下，运行时电压调节揭示了能效与可靠性之间的明确权衡关系，当允许误码率提升至10e-6时，可实现约29.3%的供电轨功耗节省。

【应用价值 / Applications】
VolTune适用于边缘计算平台和大规模数据中心等对功耗敏感的场景，特别适合数据密集型和AI驱动的工作负载。该架构为FPGA系统提供了实用的能效优化手段，使设计者能够在保证可靠性的前提下动态调整功耗，且低集成开销特性便于在现有FPGA平台中部署应用。
