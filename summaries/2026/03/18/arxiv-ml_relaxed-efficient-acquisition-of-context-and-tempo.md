---
title: "Relaxed Efficient Acquisition of Context and Temporal Features"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.11370"
published: "2026-03-18"
summarized: "2026-03-18T17:05:48.154422"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了REACT框架，首次将纵向主动特征获取（LAFA）中的初始 onboarding 上下文特征选择与时间自适应特征获取进行联合优化。针对生物医学场景中测量获取存在成本、时间和风险约束的问题，REACT通过端到端可微分优化，同时学习最优的静态上下文描述符选择和动态时间特征采集策略，在多个真实纵向健康与行为数据集上实现了更低成本下的更优预测性能。

【方法概述 / Method】

REACT采用Gumbel-Sigmoid松弛与直通估计（straight-through estimation）技术，将离散的特征获取掩码转化为可微分形式，从而支持基于梯度的端到端优化。该框架将预测损失与获取成本直接纳入联合目标函数，通过反向传播同时优化两个耦合的决策问题：初始 onboarding 阶段的上下文特征选择，以及后续时间步的自适应特征获取计划。

【实验结果 / Results】

在真实世界的纵向健康与行为数据集上，REACT相比现有的纵向获取基线方法，在降低获取成本的同时提升了预测性能。实验结果表明，将 onboarding 上下文选择与时间耦合的获取决策进行统一联合建模，能够带来显著的效益提升。

【应用价值 / Applications】

REACT适用于医疗资源受限的临床决策场景，如重症监护中的实验室检测优化、慢性病管理中的监测方案设计，以及数字健康中的传感器数据采集策略制定。该框架可帮助医疗机构在控制成本、减少患者负担的前提下，实现个性化的动态监测与精准预测，具有直接的临床转化价值。
