---
title: "Time-Aware Prior Fitted Networks for Zero-Shot Forecasting with Exogenous Variables"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15802"
published: "2026-03-18"
summarized: "2026-03-18T15:35:12.615207"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ApolloPFN，首个能够原生融合外生变量的时间感知先验拟合网络（PFN），解决了现有时间序列基础模型（如Chronos、TimesFM等）忽略外生协变量的问题。该模型通过定制化的合成数据生成流程和时间感知架构改进，有效克服了传统表格型PFN应用于时间序列时的失效模式。在M5零售需求和电价预测等包含外生信息的基准测试中，ApolloPFN取得了最先进的零样本预测性能。

【方法概述 / Method】
ApolloPFN采用先验拟合网络（PFN）框架，但针对时间序列特性进行了两项关键改进：一是设计了专门的合成数据生成程序，模拟外生变量驱动目标序列出现尖峰、间断和状态转换等复杂模式；二是引入时间感知架构修改，嵌入利用时间序列上下文所需的归纳偏置，使模型能够捕捉时序依赖关系。

【实验结果 / Results】
ApolloPFN在M5竞赛数据集（包含促销、价格等外生变量）和电价预测任务（包含电网负荷、燃料成本等外生信息）上均达到 state-of-the-art 性能。实验表明，忽略外生协变量会显著降低预测准确性，而ApolloPFN通过有效利用这些信号，在零样本设置下超越了现有时间序列基础模型。

【应用价值 / Applications】
该研究适用于零售需求预测（整合促销和定价策略）、能源负荷预测（结合气象数据）、交通流量预测（利用日历和节假日信息）以及电力市场定价（纳入电网状态和燃料成本）等场景。ApolloPFN的零样本能力使其能够快速部署到新领域，无需针对特定数据集重新训练，降低了企业级时序预测系统的开发成本。
