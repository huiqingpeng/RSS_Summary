---
title: "Lagrangian Relaxation Score-based Generation for Mixed Integer linear Programming"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24033"
published: "2026-03-26"
summarized: "2026-03-27T07:19:57.890251"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出SRG（Score-based Relaxation Generation），一种基于拉格朗日松弛引导随机微分方程（SDE）的生成式框架，用于加速混合整数线性规划（MILP）求解。该框架通过卷积核捕获变量间依赖关系，并利用拉格朗日松弛引导采样过程趋向可行且近最优区域，从而生成多样化的高质量解候选。实验表明，SRG在多个公开基准上优于现有机器学习方法，并在跨规模/跨问题的零样本迁移场景下达到与最先进精确求解器相当的优化性能，同时显著降低计算开销。

【方法概述 / Method】
SRG采用基于分数的生成模型，通过随机微分方程进行概率采样，突破传统"预测-搜索"方法中变量独立假设和单点确定性预测的局限。核心创新包括：使用卷积神经网络建模变量间的空间依赖关系，以及将拉格朗日松弛理论融入SDE的漂移项设计，为采样过程提供理论保证的最优性引导。

【实验结果 / Results】
SRG在多个公开MILP基准数据集上 consistently 超越现有机器学习基线方法，获得更优的解质量。在零样本迁移实验中，SRG在未见过的跨规模和跨问题实例上实现了与Gurobi等最先进精确求解器相当的优化间隙（optimality gap），同时通过生成紧凑有效的信赖域子问题，显著减少了下游搜索的计算时间。

【应用价值 / Applications】
该研究可广泛应用于运筹优化领域，包括供应链调度、生产计划、网络设计、组合优化等需要求解大规模MILP问题的工业场景。SRG的生成式范式和高迁移能力使其特别适合快速求解新类型或动态变化的优化问题，为将机器学习与数学规划求解器深度结合提供了新思路。
