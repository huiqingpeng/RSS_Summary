---
title: "DeepStage: Learning Autonomous Defense Policies Against Multi-Stage APT Campaigns"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16969"
published: "2026-03-19"
summarized: "2026-03-19T13:07:20.233336"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出 DeepStage，一种基于深度强化学习（DRL）的自适应、阶段感知防御框架，用于应对高级持续性威胁（APT）。该方法将企业环境建模为部分可观测马尔可夫决策过程（POMDP），融合主机溯源与网络遥测数据构建统一溯源图，利用图神经网络编码器和LSTM阶段估计器推断与MITRE ATT&CK框架对齐的攻击阶段概率，并通过分层近端策略优化（PPO）智能体选择监控、访问控制、遏制和修复等防御动作。在真实企业测试平台上，DeepStage 实现了 0.89 的阶段加权 F1 分数，较风险感知 DRL 基线提升 21.9%，证明了其在阶段感知和成本效益方面的有效性。

【方法概述 / Method】

论文采用 POMDP 对企业网络环境进行建模，整合主机溯源与网络遥测数据生成统一溯源图；基于 StageFinder 构建图神经网络编码器和 LSTM 阶段估计器，以推断攻击者在 MITRE ATT&CK 框架下的概率阶段；最终通过分层 PPO 智能体结合阶段信念与图嵌入，实现跨监控、访问控制、遏制和修复的多层次防御动作决策。

【实验结果 / Results】

在基于 CALDERA 驱动 APT 剧本的真实企业测试平台上，DeepStage 达到 0.89 的阶段加权 F1 分数，较风险感知 DRL 基线方法性能提升 21.9%，展现出优异的 APT 阶段识别准确率和成本效益。

【应用价值 / Applications】

DeepStage 可部署于企业级网络安全运营中心（SOC），实现针对多阶段 APT 攻击的自主、自适应防御决策，降低人工分析负担和响应延迟；其阶段感知机制有助于安全团队精准定位攻击所处战术阶段，优化资源分配与威胁狩猎策略，提升整体网络韧性。
