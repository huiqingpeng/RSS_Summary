---
title: "Transit Network Design with Two-Level Demand Uncertainties: A Machine Learning and Contextual Stochastic Optimization Framework"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.00010"
published: "2026-03-18"
summarized: "2026-03-18T17:04:51.295387"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了双层乘客选择公交网络设计框架（2LRC-TND），首次将两层需求不确定性纳入公交网络设计过程：第一层识别依赖公共交通的核心需求，第二层捕捉潜在需求者的条件性采用行为。该框架结合机器学习与情境随机优化，通过约束规划求解，在亚特兰大都会区的案例研究中验证了其在处理需求不确定性和情境信息方面的有效性，为固定需求模型提供了更现实的替代方案。

【方法概述 / Method】
2LRC-TND采用两个出行方式选择模型分别刻画核心需求和潜在需求，这些模型基于多种机器学习算法构建；随后将选择模型嵌入情境随机优化（CSO）框架，并利用CP-SAT求解器进行网络优化设计。

【实验结果 / Results】
该研究在包含6,600多条出行弧段和超过38,000次出行的亚特兰大都会区案例中进行评估，计算结果表明2LRC-TND能够有效设计考虑需求不确定性和情境信息的公交网络，显著优于传统固定需求模型。

【应用价值 / Applications】
该框架适用于大城市公交系统规划与优化，帮助交通规划者在不确定需求环境下做出更鲁棒的决策；其实际价值在于提升公共交通服务质量和覆盖率，促进潜在用户向实际用户的转化，从而支持可持续城市交通发展。
