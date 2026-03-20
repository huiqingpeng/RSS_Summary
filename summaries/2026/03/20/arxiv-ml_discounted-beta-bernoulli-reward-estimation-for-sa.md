---
title: "Discounted Beta--Bernoulli Reward Estimation for Sample-Efficient Reinforcement Learning with Verifiable Rewards"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18444"
published: "2026-03-20"
summarized: "2026-03-20T12:11:51.513782"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对可验证奖励强化学习（RLVR）中的样本效率问题，提出了一种新的统计估计视角。现有基于组采样的RLVR方法因依赖少量rollout的点估计而面临高方差、方差崩溃和生成响应利用不足等问题。作者提出Discounted Beta-Bernoulli（DBB）奖励估计方法，利用历史奖励统计信息建模非平稳分布，虽然存在偏差但实现了更低且稳定的方差，理论上避免了估计方差崩溃，并获得了比标准点估计更低的均方误差。

【方法概述 / Method】

作者将RLVR重新表述为统计估计问题，将奖励视为策略诱导分布的样本，将优势计算转化为从有限数据中估计奖励分布的问题。DBB方法采用Beta-Bernoulli框架，通过折扣因子整合历史奖励统计信息，构建对非平稳奖励分布的估计器，替代传统的点估计方式。

【实验结果 / Results】

在六个分布内和三个分布外推理基准上的实验表明，结合DBB的GRPO持续优于朴素GRPO。在1.7B和8B模型上，分布内平均Acc@8分别提升3.22和2.42个点，分布外分别提升12.49和6.92个点，且无需额外计算成本或内存开销。

【应用价值 / Applications】

该方法可直接应用于大语言模型的推理能力后训练优化，特别适用于数学推理、代码生成等需要可验证奖励的场景。DBB方法在不增加计算资源消耗的前提下显著提升样本效率和模型泛化能力，为实际部署中的RLVR训练提供了更高效的解决方案。
