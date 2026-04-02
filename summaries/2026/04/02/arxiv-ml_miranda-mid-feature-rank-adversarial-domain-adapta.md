---
title: "MIRANDA: MId-feature RANk-adversarial Domain Adaptation toward climate change-robust ecological forecasting with deep learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00800"
published: "2026-04-02"
summarized: "2026-04-03T07:25:06.357606"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对气候变化导致的生态预测可靠性问题，提出了一种名为MIRANDA（中特征秩对抗域适应）的新方法。传统深度学习模型在气候变化引起的数据分布偏移时表现不佳，而MIRANDA通过对中间特征施加对抗正则化，并采用基于秩的目标函数强制学习年份不变的气象表征，有效应对了气候域的连续变化和协变量/标签偏移。在涵盖70年、67,800条观测记录的国家级数据集上，MIRANDA显著提升了模型对气候分布偏移的鲁棒性，缩小了与机理模型的性能差距。

【方法概述 / Method】
MIRANDA采用两阶段域适应策略：首先，不同于传统对抗方法仅在最终潜在表征上强制域不变性，该方法在中间特征层施加对抗正则化以显式处理标签偏移；其次，使用基于排序的目标函数替代二元域分类目标，通过学习年份无关的气象表征来适应气候变化的连续时间域特性。

【实验结果 / Results】
在包含5个树种、跨越70年的大规模物候数据集上，MIRANDA相比传统域适应方法展现出更优的气候变化鲁棒性；该方法成功缩小了深度学习模型与机理模型在分布偏移场景下的性能差距，证明了其在生态预测任务中的有效性。

【应用价值 / Applications】
MIRANDA可广泛应用于气候变化背景下的生态系统响应预测，如植被物候期预报、农业产量预估和生物多样性保护规划；该方法为深度学习模型在动态非平稳环境中的可靠部署提供了技术支撑，对生态学和气候科学领域的决策支持系统具有重要实践意义。
