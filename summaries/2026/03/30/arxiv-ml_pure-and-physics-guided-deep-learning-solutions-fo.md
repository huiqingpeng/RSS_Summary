---
title: "Pure and Physics-Guided Deep Learning Solutions for Spatio-Temporal Groundwater Level Prediction at Arbitrary Locations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25779"
published: "2026-03-30"
summarized: "2026-03-31T07:17:53.794108"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究提出了一种名为STAINet的注意力机制纯深度学习模型，用于在任意位置预测周尺度地下水位，同时融合空间稀疏的地下水测量数据和空间密集的气象信息。为提升模型的可信度和泛化能力，研究进一步开发了三种物理引导策略（STAINet-IB、STAINet-ILB和STAINet-ILRB），将地下水流动方程嵌入模型中。其中STAINet-ILB表现最优，在滚动预测设置中实现了中位数MAPE 0.16%和KGE 0.58的优异性能，并能预测合理的物理方程组件，为开发新一代混合深度学习地球系统模型奠定了基础。

【方法概述 / Method】

研究采用注意力机制的深度学习架构STAINet处理时空地下水预测问题，并设计了三种物理引导变体：STAINet-IB通过归纳偏置估计控制方程组件；STAINet-ILB采用学习偏置策略，通过附加损失项对方程组件估计进行监督训练；STAINet-ILRB则利用领域专家估计的地下水补给区信息。这些方法将物理先验知识以不同方式融入纯数据驱动模型，实现物理一致性与数据驱动灵活性的结合。

【实验结果 / Results】

STAINet-ILB在测试集上表现最优，在滚动预测场景（rollout setting）中取得中位数MAPE仅0.16%、KGE达0.58的压倒性性能优势。该模型不仅能准确预测地下水位，还能输出具有物理合理性的方程组件估计，验证了模型的物理可靠性。物理引导策略显著提升了模型的泛化能力和可信度，相比纯深度学习方案展现出明显优势。

【应用价值 / Applications】

该研究为水资源管理和地下水监测提供了高精度、可解释的预测工具，特别适用于观测井分布稀疏但需要任意位置预测的场景。物理引导的混合建模方法为地球系统科学中的其他时空预测问题（如土壤水分、地表径流模拟）提供了可迁移的技术框架，有望推动新一代可信、泛化性强的地球系统混合智能模型的发展，支持气候变化背景下的可持续水资源决策。
