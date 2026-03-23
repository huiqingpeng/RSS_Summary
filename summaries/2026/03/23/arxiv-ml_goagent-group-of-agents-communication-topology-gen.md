---
title: "GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19677"
published: "2026-03-23"
summarized: "2026-03-24T07:21:18.095396"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GoAgent（Group-of-Agents），一种面向大语言模型多智能体系统（MAS）的通信拓扑生成方法。该方法将协作组群作为构建MAS的原子单元，通过枚举任务相关的候选组群并自回归地选择与连接这些组群来构建最终通信图，同时引入条件信息瓶颈（CIB）目标来压缩组间通信、减少冗余噪声。在六个基准测试上的实验表明，GoAgent实现了93.84%的平均准确率，同时将token消耗降低了约17%，达到当前最优性能。

【方法概述 / Method】
GoAgent采用"组群优先"的拓扑生成范式：首先利用LLM枚举与任务相关的候选组群，然后以自回归方式将这些组群作为原子单元进行选择与连接，联合建模组内凝聚力与组间协调关系。为控制通信开销，该方法引入条件信息瓶颈目标，在保留任务相关信号的同时过滤冗余历史噪声。

【实验结果 / Results】
GoAgent在六个基准测试上达到93.84%的平均准确率，取得当前最优性能；同时相比现有方法减少了约17%的token消耗，在提升任务解决效果的同时显著降低了通信成本。

【应用价值 / Applications】
该研究适用于需要复杂协作的LLM多智能体场景，如软件开发、科学研究、商业决策等任务，能够自动生成高效的任务特定组群结构，减少人工设计拓扑的负担；其通信压缩机制对于API调用成本敏感的实际部署具有重要经济价值，可推动大规模多智能体系统在资源受限环境中的落地应用。
