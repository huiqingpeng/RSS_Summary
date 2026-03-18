---
title: "Integrating Weather Foundation Model and Satellite to Enable Fine-Grained Solar Irradiance Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14845"
published: "2026-03-18"
summarized: "2026-03-18T17:07:27.611643"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Baguan-solar，一种两阶段多模态框架，用于实现公里级分辨率的24小时太阳辐照度预报。该方法融合了全球天气基础模型Baguan的预报结果与高分辨率地球静止卫星图像，克服了现有方法在精细尺度分辨率或长时效预报方面的局限。在东亚地区的评估中，Baguan-solar相比强基线模型（包括ECMWF IFS、原始Baguan和SolarSeer）RMSE降低16.08%，并能更好地解析云引起的瞬态变化。该模型自2025年7月起已在中国东部某省投入太阳能发电预报的实际运营部署。

【方法概述 / Method】
Baguan-solar采用解耦的两阶段设计：第一阶段预报昼夜连续中间变量（如云量），第二阶段推断太阳辐照度；其多模态融合机制联合保留卫星图像中的精细尺度云结构信息和Baguan预报的大尺度约束条件。

【实验结果 / Results】
以CLDAS数据为真值在东亚地区进行评估，Baguan-solar相比强基线模型RMSE降低16.08%，显著优于ECMWF IFS、原始Baguan和SolarSeer等方法，尤其在解析云引起的辐照度瞬态变化方面表现更佳。

【应用价值 / Applications】
该研究可直接应用于电网太阳能功率预测与调度优化，提升可再生能源并网稳定性；自2025年7月起已在中国东部某省实现运营部署，为电力系统实际运行提供决策支持，具有明确的商业化和规模化推广价值。
