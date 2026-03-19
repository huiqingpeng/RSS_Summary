---
title: "Baguan-TS: A Sequence-Native In-Context Learning Model for Time Series Forecasting with Covariates"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17439"
published: "2026-03-19"
summarized: "2026-03-19T12:12:09.444580"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Baguan-TS，一个统一的时序预测框架，将原始序列表示学习与上下文学习（ICL）相结合，通过3D Transformer同时对时间、变量和上下文三个维度进行联合注意力建模。该模型解决了高容量ICL模型的两个关键挑战：通过目标空间检索式局部校准提升训练稳定性，以及通过上下文过拟合策略缓解输出过度平滑问题。在含协变量的公开基准测试和真实能源数据集上，Baguan-TS均显著优于现有基线方法，在点预测和概率预测指标上均取得最佳表现。

【方法概述 / Method】
Baguan-TS采用3D Transformer架构，将时序数据视为三维张量（时间步×变量×上下文样本），实现跨时间、跨变量和跨上下文样本的联合注意力计算。为支持端到端的原始序列学习，模型设计了特征无关的目标空间检索机制进行局部校准，并引入上下文过拟合训练策略来增强输出多样性。

【实验结果 / Results】
在含协变量的公开基准测试中，Baguan-TS取得了最高的胜率，同时在点预测和概率预测指标上均实现显著降低。在多样化的真实世界能源数据集上的进一步评估表明，该模型具有强大的鲁棒性，并带来了实质性的性能提升。

【应用价值 / Applications】
Baguan-TS适用于需要快速适应新场景且无需梯度更新的时序预测任务，特别是在能源负荷预测、智能电网管理等存在丰富协变量信息的工业场景中具有重要价值。其序列原生的ICL能力使其能够便捷地部署到需要零样本或少样本快速适应的实际业务环境中。
