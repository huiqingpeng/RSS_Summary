---
title: "Per-Domain Generalizing Policies: On Learning Efficient and Robust Q-Value Functions (Extended Version with Technical Appendix)"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17544"
published: "2026-03-19"
summarized: "2026-03-19T13:13:18.559260"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对规划学习中的领域泛化策略问题，提出学习Q值函数而非传统的状态值函数。作者发现朴素的监督学习Q值函数效果不佳，因其无法区分教师规划器采取的动作与未采取的动作；通过引入正则化项解决这一问题后，Q值策略在10个测试领域上持续优于状态值策略，且能与LAMA-first规划器竞争。

【方法概述 / Method】
论文采用图神经网络表示Q值函数，以监督学习方式从教师规划器生成的最优计划中学习；核心创新是设计正则化项，显式强化被采纳动作与未被采纳动作之间的Q值差异，从而改进标准监督学习的缺陷。

【实验结果 / Results】
在10个不同领域的广泛实验表明，Q值策略在评估效率上显著优于状态值策略（仅需处理当前状态而非所有后继状态），同时保持或提升了规划性能，整体表现与经典规划器LAMA-first具有竞争力。

【应用价值 / Applications】
该研究为自动化规划领域提供了更高效的策略学习方法，适用于需要快速决策的实时规划场景（如机器人任务规划、物流调度等），其轻量化的Q值评估机制可降低计算开销，支持大规模状态空间中的高效推理。
