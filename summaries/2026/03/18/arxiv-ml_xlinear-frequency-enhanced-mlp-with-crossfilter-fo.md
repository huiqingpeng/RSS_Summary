---
title: "XLinear: Frequency-Enhanced MLP with CrossFilter for Robust Long-Range Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15645"
published: "2026-03-18"
summarized: "2026-03-18T15:32:32.001370"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出XLinear，一种基于MLP的长程时间序列预测模型，通过将时间序列分解为趋势和季节成分，分别设计增强频率注意力（EFA）和CrossFilter模块来捕获长期依赖关系并保持抗噪鲁棒性。实验表明，XLinear在保持MLP轻量架构和高鲁棒性的同时，实现了最先进的预测性能，有效解决了传统MLP难以捕获复杂长程特征的问题。

【方法概述 / Method】

XLinear采用时间序列分解策略，将输入序列分离为趋势分量和季节分量。对于趋势分量，设计增强频率注意力（EFA）机制，利用频域操作捕获长程依赖；对于季节分量，提出CrossFilter模块替代传统注意力机制，在提取局部特征的同时避免注意力机制带来的噪声敏感性问题。

【实验结果 / Results】

XLinear在多个标准测试数据集上达到最先进的预测性能，相比其他MLP-based预测器，在长程依赖捕获能力方面表现更优，同时保持了MLP模型固有的轻量架构特性和对噪声的高鲁棒性。

【应用价值 / Applications】

该研究适用于需要长程预测且数据含噪的实际场景，如能源负荷预测、金融时序分析、交通流量预测等，为工业界提供了一种兼具高精度、高效率和高稳定性的时间序列预测解决方案。
