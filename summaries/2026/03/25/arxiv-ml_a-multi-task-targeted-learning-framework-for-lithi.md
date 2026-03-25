---
title: "A Multi-Task Targeted Learning Framework for Lithium-Ion Battery State-of-Health and Remaining Useful Life"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22323"
published: "2026-03-25"
summarized: "2026-03-26T07:11:16.729864"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种面向锂离子电池健康状态（SOH）和剩余使用寿命（RUL）预测的多任务靶向学习框架。该框架整合了多尺度CNN特征提取模块、改进型扩展LSTM网络以及双流注意力模块，分别用于捕获局部退化模式、增强长期时序建模能力，并实现对SOH和RUL关键信息的 selective focus。实验表明，该方法相比传统和现有最优方法，SOH和RUL预测的平均RMSE分别降低了111.3%和33.0%。

【方法概述 / Method】
论文采用多任务学习架构，首先利用多尺度CNN提取电池衰退的局部细节特征；其次引入改进的扩展LSTM以增强长期时间依赖的建模能力；最后通过双流注意力模块（极化注意力用于SOH、稀疏注意力用于RUL）实现任务特定的关键信息聚焦，并采用Hyperopt算法自动优化超参数。

【实验结果 / Results】
在电池老化数据集上的大量对比实验显示，所提方法在SOH预测任务上将平均RMSE降低了111.3%，在RUL预测任务上降低了33.0%，显著优于传统方法及当前最先进的深度学习方法，验证了多任务框架与针对性特征提取的有效性。

【应用价值 / Applications】
该研究可广泛应用于电动汽车电池管理系统的健康监测与寿命预测，有助于提升电池运行的安全性和效率，降低热失控等风险；同时，自动化的超参数优化机制减少了人工调参成本，便于在实际工业场景中部署应用。
