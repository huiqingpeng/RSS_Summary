---
title: "Transfer Learning for Contextual Joint Assortment-Pricing under Cross-Market Heterogeneity"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18114"
published: "2026-03-20"
summarized: "2026-03-20T13:09:21.914563"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了在多项Logit选择模型下，具有bandit反馈的情境联合品类定价问题的迁移学习。作者提出了TJAP（Transfer Joint Assortment-Pricing）框架，通过结构化效用偏移建模跨市场异质性，实现了偏差感知的迁移学习。理论分析揭示了方差-偏差权衡机制：迁移加速共享偏好方向的学习，而异质成分产生不可约的适应成本，并建立了匹配极小极大遗憾界。

【方法概述 / Method】

作者采用"聚合-去偏"（aggregate-then-debias）估计与UCB风格策略相结合的方法。具体而言，TJAP构建双半径置信界，分别刻画统计不确定性和迁移引入的偏差，且该置信界在连续价格空间上均匀成立。模型假设市场共享共同的上下文效用结构，但在稀疏的潜在偏好坐标上存在差异。

【实验结果 / Results】

理论分析建立了极小极大遗憾界 $\tilde{O}\!\left(d\sqrt{\frac{T}{1+H}} + s_0\sqrt{T}\right)$，其中$H$为源市场数量，$d$为特征维度，$s_0$为稀疏异质维度。数值实验验证了TJAP优于仅目标市场学习和朴素聚合两种基准方法，且对跨市场差异具有稳健性。

【应用价值 / Applications】

该研究适用于多市场运营的零售商（如跨国电商平台），能够在保护用户隐私（仅观察价格与购买结果）的前提下，利用历史市场数据加速新市场学习。方法对连续价格空间的处理能力使其可直接应用于实际定价决策，为数据稀缺的新市场进入策略提供了理论指导。
