---
title: "Monodense Deep Neural Model for Determining Item Price Elasticity"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29261"
published: "2026-04-01"
summarized: "2026-04-02T07:17:01.625172"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种新颖的商品价格弹性估计框架，能够在缺乏对照实验设置的情况下估计商品级价格弹性。作者设计了一种名为Monodense-DL的混合深度神经网络架构，并在数百万笔交易的多类别零售数据上进行评估，实验结果表明该模型优于双机器学习（DML）和LightGBM等现有方法。

【方法概述 / Method】
论文提出了Monodense-DL网络，这是一种结合嵌入层（embedding）、全连接密集层（dense）和Monodense层的混合神经网络架构。该方法能够在无处理-对照实验设计的条件下，利用大规模交易数据估计价格弹性，并与双机器学习（DML）和LightGBM两种基线方法进行对比。

【实验结果 / Results】
研究在涵盖数百万笔交易的多类别零售数据集上，使用回溯测试框架对模型进行评估。实验结果表明，所提出的Monodense-DL神经网络模型在该弹性估计框架中的表现优于其他主流机器学习方法（DML和LGBM）。

【应用价值 / Applications】
该研究可直接应用于实体零售、电子商务和消费品等行业的定价策略制定与收益管理优化，帮助企业理解不同商品的购买行为、消费者对折扣的敏感度以及需求弹性部门。对于竞争激烈的市场和资源受限的企业，该技术能够支持其最大化盈利能力和市场份额的决策制定，同时揭示消费者响应度的历史变化趋势。
