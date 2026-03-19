---
title: "Time Tracker: Mixture-of-Experts-Enhanced Foundation Time Series Forecasting Model with Decoupled Training Pipelines"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.15151"
published: "2026-03-19"
summarized: "2026-03-19T13:20:49.530554"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了Time Tracker，一种基于混合专家（MoE）增强的时间序列基础预测模型，旨在解决真实世界时间序列在跨时间跨度和领域上的显著多样性问题。该模型创新性地设计了Any-variate Attention机制，支持统一架构处理单变量和多变量时间序列，并实现了预训练阶段的通道独立建模与微调阶段的通道混合建模。此外，模型还引入了基于频域特征的图学习模块来精确捕捉序列间依赖关系，最终在预测精度、泛化能力和适应性方面达到最先进的性能。

【方法概述 / Method】

Time Tracker采用稀疏混合专家（MoE）集成于Transformer架构中，以处理多样化的时间序列模式，缓解单一模型的学习困难并提升泛化能力。核心创新包括Any-variate Attention机制，允许同一模型结构灵活支持通道独立和通道混合两种建模方式；以及基于频域特征构建序列关系的图学习模块，为通道混合建模提供更精确的序列间依赖指导。

【实验结果 / Results】

论文表明Time Tracker在预测准确性、模型泛化性和适应性方面达到了最先进的性能水平，但摘要中未提供具体的数值指标或基准对比细节。模型通过解耦训练流程（预训练阶段通道独立、微调阶段通道混合）有效利用了大规模预训练数据的优势，同时保留了捕捉变量间复杂相关性的能力。

【应用价值 / Applications】

Time Tracker可广泛应用于需要处理多变量时间序列预测的实际场景，如能源负荷预测、金融时序分析、交通流量预测和工业设备监测等领域。其统一架构设计降低了部署成本，能够适应不同领域和数据特性的时间序列任务，为构建通用时间序列基础模型提供了可行路径，具有显著的工程实用价值和研究推广意义。
