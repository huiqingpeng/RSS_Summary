---
title: "Multimodal Forecasting for Commodity Prices Using Spectrogram-Based and Time Series Representations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27321"
published: "2026-03-31"
summarized: "2026-04-01T07:23:08.934521"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了**Spectrogram-Enhanced Multimodal Fusion (SEMF)**，一种用于多变量时间序列预测的新型多模态融合框架。SEMF 通过将目标时间序列转换为 Morlet 小波频谱图，并利用 Vision Transformer 提取局部频率感知特征，同时采用 Transformer 编码外生变量（如金融指标和宏观经济信号），最后通过双向交叉注意力模块实现模态融合。在多个商品价格预测任务中，SEMF 在七个竞争性基线模型上取得了持续改进，证明了频谱图编码和多模态融合在捕捉复杂金融时间序列多尺度模式方面的有效性。

【方法概述 / Method】
SEMF 采用**双分支架构**：第一分支将目标时间序列转换为 Morlet 小波频谱图，通过 Vision Transformer 提取频域特征；第二分支使用标准 Transformer 编码外生时间序列变量以捕捉时序依赖关系。两个分支通过**双向交叉注意力模块**进行深度融合，在保留各模态独特信号特征的同时建模跨模态相关性。

【实验结果 / Results】
SEMF 在多个商品价格预测数据集上进行了评估，在多个预测时间跨度（forecasting horizons）和评价指标上均** consistently 优于七个竞争性基线模型**，包括传统的统计方法和深度学习方法，展现了更强的准确性和鲁棒性。

【应用价值 / Applications】
该研究对**大宗商品价格预测、金融风险管理和宏观经济决策**具有重要价值，可应用于农产品、能源、金属等商品市场的价格走势预判，帮助投资者和 policymakers 更好地应对市场波动。此外，SEMF 的频谱图-时序融合思路可推广至其他具有复杂周期性和外部影响的预测场景，如能源负荷预测和供应链需求规划。
