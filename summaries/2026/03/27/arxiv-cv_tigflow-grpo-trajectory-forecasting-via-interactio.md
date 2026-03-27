---
title: "TIGFlow-GRPO: Trajectory Forecasting via Interaction-Aware Flow Matching and Reward-Driven Optimization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24936"
published: "2026-03-27"
summarized: "2026-03-28T07:18:35.135117"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出TIGFlow-GRPO，一种用于人体轨迹预测的两阶段生成框架，通过将基于流的轨迹生成与行为规则对齐来解决现有监督学习方法难以充分反映社会规范和场景约束的问题。第一阶段构建基于条件流匹配（CFM）的预测器，引入轨迹交互图（TIG）模块建模细粒度视觉空间交互；第二阶段采用Flow-GRPO后训练，将确定性流展开重构为随机ODE-to-SDE采样以支持轨迹探索，并通过复合奖励函数引导多模态预测向行为合理的未来演化。在ETH/UCY和SDD数据集上的实验表明，该方法在预测精度、长程稳定性、社会合规性和物理可行性方面均有提升。

【方法概述 / Method】
该方法采用两阶段训练策略：第一阶段使用TIG增强的CFM预测器，通过图神经网络显式建模智能体间及智能体与场景间的交互关系，生成信息丰富的条件特征；第二阶段引入Flow-GRPO后训练，将流匹配的确定性ODE采样转化为随机SDE采样以实现轨迹探索，结合视角感知的社会合规奖励与地图感知的物理可行奖励，通过GRPO算法优化策略。

【实验结果 / Results】
在标准轨迹预测基准ETH/UCY和SDD上的实验表明，TIGFlow-GRPO相比现有方法显著提升了预测准确性和长时程稳定性，同时生成的轨迹在社会规范遵守程度和物理场景约束满足度方面表现更优，验证了流模型与强化学习对齐机制结合的有效性。

【应用价值 / Applications】
该研究可直接应用于自动驾驶系统中的行人意图预测与路径规划，以及智能监控场景中的异常行为检测与人群流动分析，为动态多媒体环境下的智能决策系统提供了兼具分布建模能力与行为约束意识的轨迹预测解决方案，有助于提升人机交互的安全性与自然性。
