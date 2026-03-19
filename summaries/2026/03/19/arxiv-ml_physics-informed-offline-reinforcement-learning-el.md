---
title: "Physics-informed offline reinforcement learning eliminates catastrophic fuel waste in maritime routing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17319"
published: "2026-03-19"
summarized: "2026-03-19T13:11:31.902560"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了PIER（Physics-Informed, Energy-efficient, Risk-aware routing），一种离线强化学习框架，用于解决国际航运中航线规划依赖启发式方法导致的高碳排放问题。该框架基于物理校准的环境和历史船舶追踪数据学习燃料高效、安全感知的航线策略，无需在线模拟器。在墨西哥湾7条航线2023年全年AIS数据的验证中，PIER相比大圆航线平均减少10%的CO₂排放，并将灾难性燃料浪费（>1.5倍中位数消耗）从4.8%降至0.5%，实现9倍降低；同时单次航行燃料方差降低3.5倍。关键优势在于PIER仅依赖局部观测即可保持恒定性能，不受预报不确定性影响。

【方法概述 / Method】
PIER采用离线强化学习架构，核心创新包括三方面：一是物理信息状态构建，将海洋再分析产品（如海浪、洋流）编码为状态表示；二是演示增强的离线数据集，结合历史最优轨迹与物理模拟生成的数据；三是解耦的事后安全护盾（post-hoc safety shield），在策略输出后验证安全性。该方法完全脱离在线环境交互，通过预训练的物理校准模型实现策略学习。

【实验结果 / Results】
在840个测试episode的年度验证中，PIER实现平均CO₂减排10%（bootstrap 95%置信区间[2.9%, 15.7%]），且单次航行燃料消耗方差降低3.5倍（p<0.001）。灾难性燃料浪费事件发生率从4.8%骤降至0.5%。与真实AIS观测数据的部分验证显示，PIER与最快实际航行时间一致，但方差低23.1倍。对比实验表明，A*路径优化在真实预报不确定性下波浪防护性能衰减4.5倍，而PIER性能恒定。

【应用价值 / Applications】
PIER的架构具有广泛迁移性，可扩展至野火疏散、飞行器轨迹优化及未测绘地形自主导航等场景。对航运业而言，该方法在不依赖昂贵实时预报系统的前提下实现显著减排与风险控制，为国际海事组织（IMO）脱碳目标提供可部署的技术路径，同时降低航运公司燃料成本与运营风险。
