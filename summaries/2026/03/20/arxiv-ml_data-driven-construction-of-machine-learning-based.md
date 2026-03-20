---
title: "Data-driven construction of machine-learning-based interatomic potentials for gas-surface scattering dynamics: the case of NO on graphite"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18864"
published: "2026-03-20"
summarized: "2026-03-20T13:17:14.857241"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文开发了一种数据驱动的工作流程，用于构建专门针对气-表面散射动力学的机器学习原子间势（MLIP），以NO在高度定向热解石墨（HOPG）上的散射为基准系统。该研究结合SOAP描述符、主成分分析和最远点采样构建紧凑训练集，并通过委员会查询主动学习策略优化Deep Potential模型。最终得到的MLIP能够以远低于从头算分子动力学（AIMD）的计算成本，高精度复现参考能量和力，并实现大规模分子动力学模拟，成功再现了实验的主要趋势。

【方法概述 / Method】
该研究采用SOAP（平滑重叠原子位置）描述符表征局部原子环境，并通过主成分分析进行降维；利用最远点采样构建代表性训练集，结合Deep Potential框架和委员会查询主动学习策略迭代优化模型。该方法通过从扩展入射能量和表面温度范围的分子动力学模拟中提取额外构型，逐步扩展训练数据覆盖范围。

【实验结果 / Results】
最终MLIP在能量和力的预测上展现出高保真度，计算成本显著低于AIMD；大规模模拟揭示了吸附能学、捕获与直接散射概率、平动能损失、角分布和转动激发等详细动力学信息。模拟结果成功复现了实验观测的主要趋势，验证了描述符引导采样结合主动学习策略的有效性和可迁移性。

【应用价值 / Applications】
该研究为气-表面相互作用体系的高效MLIP构建提供了通用框架，可广泛应用于催化、表面科学和大气化学等领域中的气体-表面散射问题。该方法能够显著降低复杂体系原子模拟的计算成本，同时保持量子力学精度，为理解界面能量转移和反应动力学机制提供有力工具。
