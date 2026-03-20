---
title: "Combining T-learning and DR-learning: a framework for oracle-efficient estimation of causal contrasts"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2402.01972"
published: "2026-03-20"
summarized: "2026-03-20T14:14:08.374154"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了高效插件学习（EP-learning）框架，用于估计异质性因果对比（如条件平均处理效应和条件相对风险）。EP学习框架兼具Neyman正交学习策略（如DR学习和R学习）的oracle效率，同时克服了它们的主要缺陷：非凸损失函数导致的实际应用困难，以及逆概率加权和违反边界的伪结果带来的性能不佳和不稳定性。EP学习器利用因果对比总体风险函数的高效插件估计量，继承了T学习等插件策略的稳定性，同时提高了效率。

【方法概述 / Method】

EP学习框架通过构建因果对比总体风险函数的高效插件估计量来实现估计，基于经验风险最小化的EP学习器在合理条件下具有oracle效率，与oracle高效的一步去偏总体风险函数估计量的最小化器渐近等价。该方法结合了T学习的插件稳定性和DR/R学习的效率优势，避免了复杂的非凸优化问题和不稳定的逆概率加权。

【实验结果 / Results】

模拟实验表明，EP学习器在估计条件平均处理效应和条件相对风险方面优于最先进的竞争方法，包括T学习器、R学习器和DR学习器。作者提供了开源R包hte3实现所提出的方法。

【应用价值 / Applications】

该研究在因果推断和精准医疗领域具有重要应用价值，可用于更稳定、高效地估计个体层面的处理效应异质性，支持个性化决策制定。EP学习框架的oracle效率和稳定性使其适用于高维复杂数据场景，为观察性研究中的因果效应估计提供了实用的工具。
