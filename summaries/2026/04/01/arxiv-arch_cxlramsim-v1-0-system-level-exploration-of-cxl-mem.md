---
title: "CXLRAMSim v1.0: System-Level Exploration of CXL Memory Expander Cards"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.29483"
published: "2026-04-01"
summarized: "2026-04-02T07:11:05.116403"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CXLRAMSim，首个与gem5集成的全系统CXL内存模拟器，能够准确建模CXL设备在I/O总线上的真实位置，支持使用未修改的Linux内核和软件栈。该工具实现了高保真度的CXL内存特性表征，可捕捉真实延迟带宽行为和与系统DRAM的真正交错访问，同时能够识别缓存污染等关键挑战。

【方法概述 / Method】
CXLRAMSim基于gem5全系统模拟器构建，将CXL内存扩展卡建模为位于I/O总线上的真实设备，而非采用简化或非合规的架构模型。该方法支持完整的软件栈运行，包括未修改的Linux内核，从而确保模拟结果与实际系统行为的高度一致性。

【实验结果 / Results】
论文展示了CXLRAMSim能够准确捕捉CXL内存的真实延迟-带宽特性，并实现与系统DRAM的真正内存交错（true interleaving）。该工具成功识别了访问CXL内存时的缓存污染等关键系统级挑战，为CXL内存架构研究提供了高保真度的评估平台。

【应用价值 / Applications】
该研究为大语言模型训练和推理所需的扩展内存系统提供了精确的评估工具，支持系统架构师在硬件设计阶段探索CXL内存扩展卡的性能特征。CXLRAMSim可广泛应用于数据中心内存扩展方案的设计优化、CXL技术标准化研究以及下一代AI基础设施的架构决策。
