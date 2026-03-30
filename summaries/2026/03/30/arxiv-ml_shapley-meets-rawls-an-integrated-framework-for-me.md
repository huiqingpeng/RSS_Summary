---
title: "Shapley meets Rawls: an integrated framework for measuring and explaining unfairness"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26476"
published: "2026-03-30"
summarized: "2026-03-31T07:24:44.937578"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一个将可解释性与公平性统一整合的框架，证明Shapley值可同时用于定义和解释机器学习模型中的不公平性。该框架基于标准群体公平性准则，能够对不公平性进行估计、统计推断，并识别导致不公平的特征。研究还将框架扩展至Efficient-Symmetric-Linear (ESL)值族，其中部分变体提供了更稳健的定义和更短的计算时间。在UCI人口普查收入数据集上的实证表明，"年龄"、"工作时长"和"婚姻状况"是导致性别不公平的主要因素。

【方法概述 / Method】
论文核心方法是将Shapley值从合作博弈论引入公平性分析，通过量化各特征对群体间预测差异的贡献来同时度量和解释不公平性。该方法可推广至ESL值族（包括Shapley值及其变体），在保持效率性、对称性和线性性的同时，提供更灵活的计算效率与稳健性权衡。

【实验结果 / Results】
在UCI人口普查收入数据集上，该方法识别出年龄、每周工作时长和婚姻状况是导致性别不公平的主要驱动特征。与传统Bootstrap检验相比，ESL值变体显著缩短了计算时间，同时保持了可比的统计推断能力。

【应用价值 / Applications】
该框架适用于需要同时审计模型公平性并解释不公平来源的场景，如信贷审批、招聘系统和公共政策评估等高风险决策领域。通过提供特征层面的不公平归因，帮助从业者针对性地改进数据收集或模型设计，实现更透明、可操作的算法公平性治理。
