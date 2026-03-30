---
title: "Knowledge Distillation for Efficient Transformer-Based Reinforcement Learning in Hardware-Constrained Energy Management Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26249"
published: "2026-03-30"
summarized: "2026-03-31T07:23:02.583277"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了知识蒸馏技术在Transformer强化学习模型中的应用，以解决住宅能源管理系统中硬件资源受限的问题。作者将高容量的Decision Transformer教师模型的决策行为迁移到紧凑的学生模型，在保持控制质量的同时显著降低模型复杂度。实验结果表明，该方法在参数数量减少96%、推理内存降低90%、推理时间缩短63%的情况下，仍能保持甚至略微提升（最高1%）控制性能，使Decision Transformer更适用于资源受限的嵌入式硬件部署。

【方法概述 / Method】
研究采用离线序列决策框架，首先基于Ausgrid数据集在多建筑异构数据上训练Decision Transformer教师模型，然后通过行为匹配（action matching）将教师模型的决策知识蒸馏到更小的学生模型中。该方法不仅探索了不同容量配置的师生模型组合，还验证了向同架构容量模型蒸馏的有效性。

【实验结果 / Results】
知识蒸馏在广泛的师生配置下基本保持了控制性能，部分配置甚至实现了最高1%的微小改进；模型压缩效果显著，参数数量最高减少96%，推理内存降低90%，推理时间缩短63%。值得注意的是，即使向相同架构容量的模型进行蒸馏，也能获得相当的成本改进效果。

【应用价值 / Applications】
该研究为住宅能源管理系统中的电池调度策略优化提供了实用的部署方案，使复杂的Transformer模型能够在内存和延迟受限的住宅控制器上高效运行。该方法可广泛应用于智能电网、分布式能源管理和边缘计算场景，推动高级强化学习算法在资源约束环境下的实际落地。
