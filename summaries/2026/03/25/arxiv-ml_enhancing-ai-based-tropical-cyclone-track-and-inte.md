---
title: "Enhancing AI-Based Tropical Cyclone Track and Intensity Forecasting via Systematic Bias Correction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22314"
published: "2026-03-25"
summarized: "2026-03-26T07:09:59.241749"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了BaguanCyclone，一个用于热带气旋路径和强度预报的统一AI框架，通过概率中心精化模块和区域感知强度预报模块，解决了现有AI气象预报系统因粗分辨率再分析数据训练导致的离散化误差和强度平滑问题。该模型在全球IBTrACS数据集和六大热带气旋洋区的评估中，持续优于业务数值天气预报模式和多数AI基线方法，尤其在再增强、急转、双台风和迂回等复杂气象情景下表现卓越。

【方法概述 / Method】

BaguanCyclone框架包含两个核心创新：（1）概率中心精化模块，对热带气旋中心的连续空间分布进行建模，突破固定网格约束以实现更精细的路径定位；（2）区域感知强度预报模块，在热带气旋核心周围动态定义的子网格区域内利用高分辨率内部表征，以更好地捕捉局部极端强度。

【实验结果 / Results】

该模型在全球IBTrACS数据集六大热带气旋洋区的评估中，在路径和强度预报精度上均显著优于业务数值天气预报（NWP）模型及大多数AI基线方法；特别地，系统在处理再增强、急转、双台风和迂回等复杂气象事件时展现出稳定的准确预报能力。

【应用价值 / Applications】

本研究可提升热带和亚热带地区热带气旋预警的时效性与准确性，为防灾减灾决策提供更可靠的预报支撑，适用于气象业务预报、应急管理部门的风险评估与应急响应规划，以及保险和能源等行业的气象风险管理工作。
