---
title: "Improving Instruction Fetch Efficiency via High-Level Program Map Traversal"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2406.06738"
published: "2026-04-02"
summarized: "2026-04-03T07:15:43.295177"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了"指令预发送"(instruction presending)技术，通过遍历高级程序映射来识别并将指令缓存块、分支目标缓冲区和指令TLB条目从二级结构"即时"迁移到一级结构。实验表明，该技术相比最先进的指令预取方案，可将指令获取等待周期减少一个数量级，尤其适用于高基础MPKI(每千条指令缺失数)的基准测试程序。

【方法概述 / Method】
该方案通过分析高级程序控制流图来预测即将执行的代码区域，并提前将所需的指令缓存块、BTB条目和iTLB条目从二级存储预迁移至一级结构。这种"即时"迁移机制避免了传统预取策略的盲目性，实现了更精准的指令供应。

【实验结果 / Results】
在小尺寸一级BTB配置下，预发送技术将指令获取等待周期降低了约10倍；对于高基础MPKI的基准测试，性能提升尤为显著，因为这些场景中二级到一级结构的频繁迁移成为关键瓶颈。整体性能改进与指令获取效率的重要性呈正相关。

【应用价值 / Applications】
该技术可应用于现代处理器设计，特别是在嵌入式系统和移动设备等受面积/功耗限制、无法配置大容量一级BTB的场景。通过提升指令获取效率，有助于在资源受限环境下实现更高的指令级并行度和整体性能。
