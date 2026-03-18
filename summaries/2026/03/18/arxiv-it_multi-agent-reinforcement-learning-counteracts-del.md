---
title: "Multi-Agent Reinforcement Learning Counteracts Delayed CSI in Multi-Satellite Systems"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2603.16470"
published: "2026-03-18"
summarized: "2026-03-18T19:08:32.663328"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了多卫星系统中下行链路传输的信道状态信息（CSI）延迟问题，提出了一种多智能体强化学习（MARL）算法来最大化用户总速率。该算法采用新颖的双层优化框架——双阶段近端策略优化（DS-PPO），分别处理单个卫星优化和多卫星协作优化两个阶段。数值结果表明DS-PPO对CSI不完美具有鲁棒性，并能显著提升系统总速率，同时论文还提供了算法的收敛性分析和计算复杂度分析。

【方法概述 / Method】
论文提出双阶段近端策略优化（DS-PPO）算法，通过双层优化结构解决MARL中的大规模连续动作空间和非独立同分布（non-IID）环境问题。第一阶段优化单个卫星的用户总速率，第二阶段优化多卫星协作形成分布式多天线基站时的总速率，实现从独立决策到协同决策的渐进式学习。

【实验结果 / Results】
实验验证了DS-PPO算法对CSI延迟和误差的鲁棒性，相比基准方法实现了显著的用户总速率提升。算法在不同CSI不完美条件下均能保持稳定性能，并提供了理论上的收敛性保证和计算复杂度分析。

【应用价值 / Applications】
该研究适用于下一代卫星通信网络与6G等技术的融合场景，为全球覆盖的移动通信提供高质量服务。DS-PPO算法可有效应对卫星-地面链路的高传播延迟问题，提升多卫星协作波束成形和资源分配的效率，对低轨卫星星座（如Starlink）的实时通信优化具有重要实践意义。
