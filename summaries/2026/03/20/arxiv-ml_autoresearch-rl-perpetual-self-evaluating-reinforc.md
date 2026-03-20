---
title: "AutoResearch-RL: Perpetual Self-Evaluating Reinforcement Learning Agents for Autonomous Neural Architecture Discovery"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.07300"
published: "2026-03-20"
summarized: "2026-03-20T14:12:17.710974"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出 AutoResearch-RL，一种无需人工监督的开放式神经网络架构与超参数自动搜索框架。该强化学习智能体通过持续提出代码修改、在固定时间预算内执行实验、基于验证集 bits-per-byte 指标获取奖励，并使用 PPO 算法更新策略，实现永久自主运行。研究将该过程形式化为马尔可夫决策过程，在理论上给出收敛保证，并在单 GPU nanochat 预训练基准上验证：经过约 300 次夜间迭代后，智能体发现的配置达到或超越人工调优基线。

【方法概述 / Method】

论文采用三模块分离设计：冻结环境（数据流水线、评估协议与常量）确保跨实验公平比较；可变目标文件作为智能体可编辑状态；元学习器（RL 智能体）累积实验轨迹并指导后续提案。智能体使用近端策略优化（PPO）算法，以验证集 bits-per-byte（val-bpb）作为标量奖励信号进行策略更新。

【实验结果 / Results】

在单 GPU nanochat 预训练任务上，AutoResearch-RL 经过约 300 次夜间迭代后，自动发现的神经网络架构与超参数配置能够匹配或超过人工精心调优的基线性能，全程无需人类介入。

【应用价值 / Applications】

该框架可显著降低神经网络架构搜索（NAS）和超参数优化中的人工成本，实现真正的自动化机器学习（AutoML）。其"永久运行"特性适用于需要持续优化的场景，如大规模语言模型预训练、云端自动化实验平台，以及算力受限环境下的高效架构探索。
