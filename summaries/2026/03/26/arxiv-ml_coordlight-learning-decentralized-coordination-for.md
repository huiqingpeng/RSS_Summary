---
title: "CoordLight: Learning Decentralized Coordination for Network-Wide Traffic Signal Control"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24366"
published: "2026-03-26"
summarized: "2026-03-27T07:23:05.328410"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CoordLight，一种基于多智能体强化学习（MARL）的交通信号控制框架，旨在解决部分可观测性和去中心化协调的关键挑战。该框架通过引入队列动态状态编码（QDSE）和邻居感知策略优化（NAPO）算法，实现了单个路口决策优化与邻里协调的有机结合，从而扩展到网络级交通优化。在包含多达196个路口的三个真实世界数据集上的评估表明，CoordLight在多样化交通网络中 consistently 优于现有最先进方法。

【方法概述 / Method】
CoordLight的核心方法包括两个创新组件：一是队列动态状态编码（QDSE），基于车辆排队模型的新型状态表示，增强智能体分析、预测和响应本地交通动态的能力；二是邻居感知策略优化（NAPO）算法，通过注意力机制识别相邻智能体间的状态和动作依赖关系，实现更协调的决策制定，并通过鲁棒的优势计算改进策略学习更新。

【实验结果 / Results】
CoordLight在三个真实世界交通数据集上进行了全面评估，网络规模涵盖多达196个路口。实验结果表明，该方法在不同交通流量的多样化交通网络中 consistently 展现出优越性能，显著优于现有的最先进交通信号控制方法。

【应用价值 / Applications】
该研究对缓解城市拥堵、最大化通行能力和促进可持续出行具有重要实际价值，特别适用于不断扩张的大型城市中的自适应交通信号控制系统。CoordLight的可扩展性使其能够部署于大规模真实交通网络，为智能交通系统提供高效的去中心化协调解决方案。
