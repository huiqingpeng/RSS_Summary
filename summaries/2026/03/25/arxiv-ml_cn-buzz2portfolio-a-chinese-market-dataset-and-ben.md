---
title: "CN-Buzz2Portfolio: A Chinese-Market Dataset and Benchmark for LLM-Based Macro and Sector Asset Allocation from Daily Trending Financial News"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22305"
published: "2026-03-25"
summarized: "2026-03-26T07:09:31.690731"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CN-Buzz2Portfolio，一个基于中国市场的可复现基准数据集，用于评估大型语言模型（LLMs）从每日热门金融新闻中进行宏观和行业资产配置的能力。该数据集覆盖2024年至2025年中期的滚动时间窗口，模拟真实的公众注意力流，要求智能体从高曝光叙事中提炼投资逻辑而非依赖预过滤的实体新闻。研究通过9个LLM的广泛实验发现，不同模型在将宏观叙事转化为投资组合权重方面存在显著差异，为通用推理与金融决策之间的对齐提供了新见解。

【方法概述 / Method】
论文提出了三阶段CPA智能体工作流（Compression-Perception-Allocation），包括新闻信息压缩、市场感知理解和资产配置决策三个阶段。该框架评估LLM在交易所交易基金（ETF）等广泛资产类别上的配置能力，而非个股选择，以降低特质性波动的影响。

【实验结果 / Results】
对9个LLM的实验揭示了模型在将宏观层面叙事转化为投资组合权重时存在显著性能差异。研究表明不同LLM在通用推理能力与金融决策制定之间的对齐程度各不相同，为理解LLM作为金融智能体的能力边界提供了实证依据。

【应用价值 / Applications】
该基准为LLM向自主金融智能体的演进提供了严格的评估框架，可应用于智能投顾、量化策略开发和风险管理等场景。通过开源数据、代码和实验，研究促进了可持续的金融智能体研究，帮助从业者和研究者更好地理解和部署基于新闻驱动的资产配置系统。
