---
title: "Approximate Subgraph Matching with Neural Graph Representations and Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18314"
published: "2026-03-20"
summarized: "2026-03-20T12:10:19.685660"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对近似子图匹配（ASM）这一NP难问题，提出了基于强化学习的RL-ASM算法。该算法利用图Transformer提取完整的图结构信息，并采用模仿学习结合PPO强化学习训练策略，替代传统的启发式搜索方法。实验结果表明，RL-ASM在有效性和效率上均优于现有方法。

【方法概述 / Method】
论文采用分支限界框架，每次从两个输入图中选择一对节点进行潜在匹配。核心创新在于使用Graph Transformer架构提取编码完整图信息的特征表示，并通过两阶段训练策略——先利用监督信号进行模仿学习预训练，再用近端策略优化（PPO）进行微调优化长期累积奖励。

【实验结果 / Results】
RL-ASM在合成数据集和真实世界数据集上均展现出优越性能，相比现有基于启发式搜索的方法，在匹配效果和计算效率方面均有显著提升。具体性能指标虽未详述，但实验验证了该方法的有效性和可扩展性。

【应用价值 / Applications】
该研究可广泛应用于数据库系统查询优化、社交网络分析、生物化学分子结构比对以及隐私保护等领域，为需要在大规模图中进行模式发现的场景提供了更高效的算法工具，具有重要的理论和实际意义。
