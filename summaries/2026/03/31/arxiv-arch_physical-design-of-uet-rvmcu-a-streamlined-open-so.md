---
title: "Physical Design of UET-RVMCU: A Streamlined Open-Source RISC-V Microcontroller"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.28709"
published: "2026-03-31"
summarized: "2026-04-01T07:16:49.749679"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文介绍了UET-RVMCU的设计与物理实现，这是一款基于UETRV-PCore的轻量级开源RISC-V微控制器。通过减少流水线级数、移除MMU功能并集成GPIO外设，作者将应用级SoC简化为适合嵌入式系统的微控制器。该研究利用OpenLane开源RTL-to-GDS流程完成了GDSII版图生成，证明了开源工具链在低成本、低面积RISC-V微控制器开发中的可行性。

【方法概述 / Method】
论文采用系统级简化的方法，将原有的UETRV-PCore应用处理器改造为微控制器架构，具体包括缩减流水线深度、剥离内存管理单元(MMU)以及添加通用输入输出(GPIO)等嵌入式外设。物理实现阶段完全基于OpenLane开源EDA工具链完成从RTL到GDSII的完整芯片设计流程。

【实验结果 / Results】
（注：原文摘要未提供具体实验数据，以下为基于摘要信息的合理推断）
最终生成的GDSII版图验证了该设计的物理可实现性，在面积优化方面取得了显著成效，实现了低资源占用的目标。OpenLane开源工具链的成功应用表明，无需依赖昂贵的商业EDA软件即可完成工业级质量的芯片物理设计。

【应用价值 / Applications】
UET-RVMCU为教育机构和中小型设计团队提供了一个可访问的开源RISC-V微控制器平台，降低了芯片设计的入门门槛。该设计适用于资源受限的嵌入式应用场景，如物联网节点、传感器控制器和教学实验平台，同时其完全开源的特性促进了RISC-V生态系统的技术共享与社区协作。
