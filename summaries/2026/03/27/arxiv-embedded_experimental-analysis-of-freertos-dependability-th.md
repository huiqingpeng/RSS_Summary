---
title: "Experimental Analysis of FreeRTOS Dependability through Targeted Fault Injection Campaigns"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.25666"
published: "2026-03-27"
summarized: "2026-03-28T07:06:09.222098"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了实时操作系统（RTOS）在电离辐射环境下的可靠性问题，提出了KRONOS——一种基于软件的非侵入式故障注入框架，用于在FreeRTOS内核数据结构中注入瞬态和永久性故障。通过大规模故障注入实验，作者系统评估了内核级数据损坏对功能正确性、时序行为和系统可用性的影响，发现指针和调度器相关变量的损坏极易导致系统崩溃，而任务控制块（TCB）中许多字段对系统可用性的影响相对有限。

【方法概述 / Method】

KRONOS采用后传播（post-propagation）故障注入技术，无需专用硬件或调试接口即可向操作系统可见的内核数据结构注入故障。该框架针对FreeRTOS核心组件（包括调度器变量和任务控制块TCB）实施定向故障注入，能够模拟电离辐射引起的瞬态和永久性硬件故障在软件层面的传播效应。

【实验结果 / Results】

实验结果表明，指针类型变量和关键调度器相关数据的损坏最频繁地引发系统崩溃；相比之下，TCB中大量字段的损坏对系统整体可用性影响较小。该研究首次系统量化了不同内核数据结构损坏对FreeRTOS功能正确性、时序行为和可用性的差异化影响。

【应用价值 / Applications】

该研究为安全关键领域（如航空航天、核能、医疗设备）中FreeRTOS的可靠性评估和加固设计提供了实证依据和数据支持。KRONOS框架可作为RTOS容错机制验证和故障响应策略优化的测试工具，帮助开发者在不依赖昂贵辐射测试设施的情况下评估系统鲁棒性。
