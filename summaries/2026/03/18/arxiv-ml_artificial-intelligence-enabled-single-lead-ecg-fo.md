---
title: "Artificial intelligence-enabled single-lead ECG for non-invasive hyperkalemia detection: development, multicenter validation, and proof-of-concept deployment"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14177"
published: "2026-03-18"
summarized: "2026-03-18T17:06:46.145215"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究开发并验证了一种名为Pocket-K的单导联AI-ECG系统，用于非侵入性高钾血症筛查。该系统基于ECGFounder基础模型初始化，利用34,439例患者的62,290对ECG-血钾数据进行训练和验证。Pocket-K在内部测试、时间验证和外部验证中分别达到0.936、0.858和0.808的AUROC，对中重度高钾血症（≥6.0 mmol/L）的检测性能更优，且外部阴性预测值超过99.3%。研究团队还开发了手持原型设备，支持近实时推理，为院外监测提供了可行性。

【方法概述 / Method】
研究采用多中心观察性设计，使用常规收集的临床ECG和实验室数据，以I导联ECG数据对基于ECGFounder的模型进行微调。数据来自北京大学人民医院（用于模型开发和时间验证）和天津医科大学第二医院（独立外部验证），高钾血症定义为静脉血清钾>5.5 mmol/L。

【实验结果 / Results】
Pocket-K在内部测试中AUROC达0.936，时间验证为0.858，外部验证为0.808；针对KDIGO定义的中重度高钾血症（≥6.0 mmol/L），时间验证和外部验证AUROC分别提升至0.940和0.861。外部验证阴性预测值超过99.3%，模型预测的高风险在低血钾阈值以下患者中更常见于慢性肾病和心力衰竭患者。

【应用价值 / Applications】
该研究为慢性肾病和心力衰竭患者的高钾血症院外监测提供了非侵入性解决方案，手持原型设备可实现近实时检测，有望部署于家庭、社区等原生手持和可穿戴场景，改善高危人群的早期筛查和长期管理。
