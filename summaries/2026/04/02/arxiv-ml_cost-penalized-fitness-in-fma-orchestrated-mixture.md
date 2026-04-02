---
title: "Cost-Penalized Fitness in FMA-Orchestrated Mixture of Experts: Experimental Evidence for Molecular Memory in Domain Adaptation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00812"
published: "2026-04-02"
summarized: "2026-04-03T07:25:18.145902"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了nanoFMT系统的七组对照实验结果，这是一种由自由市场算法（FMA） orchestrated 的Transformer架构，具备动态专家混合（MoE）管理能力。研究核心发现是：成本惩罚适应度指标结合新生专家的线性宽限期，能使系统通过专家多样化而非替换来积累领域知识。关键的"往返领域迁移"实验显示，系统返回先前学习领域时的恢复速度提升9-11倍，且无需任何专家新生或替换，这种"分子记忆"效应在现有MoE管理方法中尚无对应机制。

【方法概述 / Method】
论文采用自由市场算法（FMA）作为MoE系统的中央协调机制，引入成本惩罚适应度指标来评估专家价值，并为新创建的专家设置线性宽限期以避免过早淘汰。该方法使专家池在满容量运行时能够动态适应变化的数据分布，同时保留对历史领域的记忆能力。

【实验结果 / Results】
七组对照实验证实，该方案在往返领域迁移任务中实现9-11倍的恢复速度提升，且重返历史领域时零专家更替。初步成本分析表明，对于OpenAI规模的服务提供商，在中等场景下可实现年均3910万美元成本节约和27.1 GWh能耗降低。

【应用价值 / Applications】
该研究为大规模语言模型服务提供商提供了显著降低运营成本与能耗的潜在方案，特别适用于需要持续处理多领域动态数据流的云AI基础设施。分子记忆机制使系统能够高效服务具有周期性或回归性特征的客户需求，无需重复训练开销。
