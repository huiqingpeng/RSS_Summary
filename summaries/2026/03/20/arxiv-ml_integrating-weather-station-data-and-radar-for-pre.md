---
title: "Integrating Weather Station Data and Radar for Precipitation Nowcasting: SmaAt-fUsion and SmaAt-Krige-GNet"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2502.16116"
published: "2026-03-20"
summarized: "2026-03-20T14:05:47.206143"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究针对现有降水临近预报模型仅依赖雷达数据、未能充分利用大气信息的局限性，提出融合多变量气象站数据与雷达数据以提升预报能力。研究开发了两种互补架构——SmaAt-fUsion和SmaAt-Krige-GNet，并在荷兰2016-2019年气象站与雷达数据上进行评估。实验表明，SmaAt-Krige-GNet在低降水场景下优于基准模型，而SmaAt-fUsion在低、高降水场景下均表现更佳，验证了离散气象站数据对深度学习天气预报模型的增益价值。

【方法概述 / Method】
SmaAt-fUsion通过卷积层将气象站数据嵌入SmaAt-UNet网络瓶颈层实现数据融合；SmaAt-Krige-GNet则采用克里金（Kriging）地统计插值法将离散站点数据转化为变量专属空间分布图，再基于SmaAt-GNet构建双编码器架构进行多层级数据整合。两种方案分别从隐式特征融合与显式空间插值角度解决异构数据集成问题。

【实验结果 / Results】
在荷兰四年数据集上的评估显示：SmaAt-Krige-GNet在低降水条件下超越仅使用雷达数据的SmaAt-UNet基准模型；SmaAt-fUsion则在低、高降水双场景下均优于SmaAt-UNet。结果表明气象站数据的引入能有效提升降水临近预报精度，尤其在不同降水强度条件下展现出差异化优势。

【应用价值 / Applications】
该研究可直接应用于洪水预警、交通调度、能源系统运营及应急响应等需要精准短时降水预报的领域。通过低成本整合现有气象站网络数据与雷达系统，为运营决策提供更可靠的气象信息支撑，同时该方法框架可扩展至其他气象要素（如温度、风速）的多源数据融合预报场景。
