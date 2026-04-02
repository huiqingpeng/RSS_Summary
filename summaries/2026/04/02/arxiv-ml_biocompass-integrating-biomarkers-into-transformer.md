---
title: "BioCOMPASS: Integrating Biomarkers into Transformer-Based Immunotherapy Response Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00739"
published: "2026-04-02"
summarized: "2026-04-03T07:24:21.734041"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了BioCOMPASS，一种基于Transformer的免疫治疗反应预测模型，通过整合生物标志物和治疗信息来提升模型的泛化能力。该研究创新性地将生物标志物信息以损失函数组件的形式（而非直接输入）与模型中间表示对齐，并引入治疗门控和通路一致性损失等机制。实验表明，该方法在多种跨队列、跨癌种和跨治疗方案的泛化性评估策略中均表现优异，证明了利用互补临床信息和领域知识构建模型组件是提升免疫治疗预测泛化性的有效方向。

【方法概述 / Method】
BioCOMPASS基于现有的COMPASS Transformer架构进行扩展，核心创新在于不直接将生物标志物作为模型输入，而是设计专门的损失组件（包括治疗门控机制和通路一致性损失）来约束模型的中间表示与已知的生物标志物及治疗信息保持一致。这种对齐策略使模型能够隐式地学习并利用领域知识，同时保持端到端的训练流程。

【实验结果 / Results】
研究采用Leave-one-cohort-out（留一队列）、Leave-one-cancer-type-out（留一癌种）和Leave-one-treatment-out（留一治疗方案）三种严格的泛化性评估策略，结果显示BioCOMPASS相比仅依赖自监督学习的基线Transformer模型以及传统的阈值型生物标志物方法均有显著提升。特别是治疗门控和通路一致性损失组件被验证对泛化性能改善起到关键作用。

【应用价值 / Applications】
该研究为免疫治疗反应预测提供了更具临床实用价值的建模框架，能够适应不同癌症类型、测序平台和用药方案的异质性临床场景，有助于解决当前模型在新患者队列上性能骤降的问题。BioCOMPASS的方法论可推广至其他小样本、高异质性的生物医学预测任务，为整合多源先验知识提升深度学习模型泛化性提供了可借鉴的技术路径。
