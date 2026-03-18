---
title: "A Scalable Approach to Solving Simulation-Based Network Security Games"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.16564"
published: "2026-03-18"
summarized: "2026-03-18T17:04:35.137227"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MetaDOAR，一种轻量级元控制器，通过引入可学习的分区感知过滤层和Q值缓存机制来增强Double Oracle/PSRO范式，实现了在超大规模网络环境中的可扩展多智能体强化学习。该方法学习从节点结构嵌入到紧凑状态投影的映射，以快速筛选关键设备子集进行聚焦搜索，并通过LRU缓存和保守的k跳缓存失效策略大幅减少冗余计算。实验表明，MetaDOAR在大型网络拓扑上获得了比SOTA基线更高的玩家收益，且内存使用和训练时间无明显扩展问题。

【方法概述 / Method】
MetaDOAR采用分层策略架构：上层元控制器学习紧凑状态投影，将网络节点嵌入映射为分区评分，筛选出top-k关键设备子集；下层传统actor在该子集上进行聚焦式束搜索，利用critic智能体评估候选动作。系统通过量化状态投影和局部动作标识符建立LRU缓存，以批量critic前向传播评估动作，并采用k跳缓存失效机制保证决策质量。

【实验结果 / Results】
MetaDOAR在大型网络拓扑上的玩家收益显著优于现有SOTA基线方法；该方法在内存占用和训练时间方面表现出良好的可扩展性，未出现明显的性能瓶颈；缓存机制有效降低了冗余critic计算，同时通过保守失效策略保持了决策质量。

【应用价值 / Applications】
该研究为大规模网络安全博弈提供了实用的分层策略学习方案，可应用于企业级网络防御决策、关键基础设施保护等场景；其可扩展架构适用于节点数量庞大的复杂网络环境，为实时安全策略优化提供了计算高效的解决路径；理论上 motivated 的设计也为其他大规模网络化决策问题提供了可借鉴的方法论框架。
