---
title: "Rolling-Origin Validation Reverses Model Rankings in Multi-Step PM10 Forecasting: XGBoost, SARIMA, and Persistence"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20315"
published: "2026-03-24"
summarized: "2026-03-25T07:07:33.459009"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究揭示了传统静态时间序列划分方法在空气质量预测评估中的局限性，发现滚动原点验证（rolling-origin validation）会显著改变模型排名。研究表明，在PM10多步预测中，静态评估显示XGBoost表现优异，但滚动原点评估发现其短期和中期预测甚至不如持续性基准（persistence），而SARIMA则在全预测范围内保持稳定的正技能得分。

【方法概述 / Method】

研究采用2017-2024年间南欧某城市背景监测站的2,350条日PM10观测数据，对比了XGBoost、SARIMA和持续性基准三种方法。实验设计了两种评估协议：静态时间序列划分和带月度更新的滚动原点验证，并定义"可预测性范围"为相对于持续性基准仍具有正技能的最大预测步长。

【实验结果 / Results】

静态评估显示XGBoost在1-7天预测范围内表现良好，但滚动原点验证完全逆转了模型排名：XGBoost在短期和中期预测中并不稳定优于持续性基准，而SARIMA在整个预测范围内始终保持正技能。这一发现表明静态划分可能高估机器学习方法在实际运营环境中的效用。

【应用价值 / Applications】

该研究为空气质量预测领域提供了更严谨的模型评估框架，强调在实际运营中需采用滚动原点验证和持续性基准参考。对实践者而言，滚动原点验证下的技能轮廓图可明确显示各方法在不同预测时效上的可靠性，帮助选择最适合特定预测需求的模型。
