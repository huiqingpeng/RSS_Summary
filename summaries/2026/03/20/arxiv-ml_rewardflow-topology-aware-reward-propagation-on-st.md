---
title: "RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18859"
published: "2026-03-20"
summarized: "2026-03-20T13:17:06.502064"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出RewardFlow，一种轻量级状态级奖励估计方法，用于解决大语言模型智能体强化学习中终端奖励稀疏的问题。该方法通过构建状态图并利用其拓扑结构进行奖励传播，无需训练昂贵的奖励模型即可生成细粒度的状态级奖励。实验表明，RewardFlow在四个智能体推理基准上显著优于现有强化学习基线方法，展现出更优的性能、鲁棒性和训练效率。

【方法概述 / Method】
RewardFlow首先将推理轨迹中的状态构建为状态图，分析各状态对最终成功的贡献程度；随后采用拓扑感知的图传播算法量化这些贡献，生成客观的状态级密集奖励。该方法无需额外训练奖励模型，直接利用状态图的内在结构进行奖励估计。

【实验结果 / Results】
RewardFlow在四个智能体推理基准测试中均显著超越先前的强化学习基线方法，实现了更优的任务性能表现。同时，该方法展现出更强的训练鲁棒性和更高的计算效率，避免了传统过程奖励模型训练中的大规模计算开销。

【应用价值 / Applications】
RewardFlow可广泛应用于需要细粒度决策优化的LLM智能体场景，如代码生成、数学推理、工具调用和多步任务规划等。该方法为资源受限场景下的智能体强化学习提供了高效可行的解决方案，降低了部署过程奖励模型的门槛。
