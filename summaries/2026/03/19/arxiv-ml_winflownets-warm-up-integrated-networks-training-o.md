---
title: "WINFlowNets: Warm-up Integrated Networks Training of Generative Flow Networks for Robotics and Machine Fault Adaptation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17301"
published: "2026-03-19"
summarized: "2026-03-19T12:09:59.322721"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了WINFlowNets，一种新型的连续生成流网络（CFlowNets）框架，解决了传统CFlowNets依赖预训练检索网络的问题。该方法通过引入预热阶段和共享训练架构，实现了流网络与检索网络的协同训练。实验表明，WINFlowNets在平均奖励和训练稳定性方面优于传统CFlowNets和最先进的强化学习算法，并在故障环境中展现出强大的快速适应能力，适用于动态且易发生故障的机器人系统。

【方法概述 / Method】

WINFlowNets采用三阶段训练策略：首先对检索网络进行预热训练以初始化策略，随后建立共享训练架构和共享回放缓冲区，实现流网络与检索网络的同步联合训练。这种设计消除了对预训练数据的依赖，使网络能够在动态环境中自适应学习。

【实验结果 / Results】

在模拟机器人环境中的实验显示，WINFlowNets在平均奖励指标上超越了标准CFlowNets和最先进的强化学习算法，同时表现出更优的训练稳定性。关键的是，该方法在故障环境中展现出强大的自适应能力，能够在样本数据有限的情况下实现快速适应，显著提升了在动态变化环境中的实用性。

【应用价值 / Applications】

WINFlowNets特别适用于动态且易发生故障的机器人系统，如工业制造中的自适应机械臂控制和设备故障自适应调整等场景。该研究解决了传统方法中预训练数据难以获取或无法代表当前环境的问题，为实际部署中面临数据收集困难或样本效率要求高的机器人任务提供了可行的解决方案。
