---
title: "Epileptic Seizure Prediction Using Patient-Adaptive Transformer Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26821"
published: "2026-03-31"
summarized: "2026-04-01T07:19:12.140548"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种患者自适应的Transformer框架，用于癫痫发作的短期预测，以解决脑电信号中患者间差异大和时间结构复杂的问题。该方法采用两阶段训练策略：首先通过自监督预训练学习通用的脑电时间表征，然后进行患者特异性微调以实现30秒内发作 onset 的二分类预测。在TUH EEG数据集上的实验表明，该方法验证准确率超过90%、F1分数超过0.80，证明了自监督表征学习与患者自适应结合的有效性。

【方法概述 / Method】
论文采用基于Transformer的序列建模方法，首先通过噪声感知预处理将多通道脑电信号离散化为token化的时间序列，然后以自回归序列建模进行自监督预训练，最后针对个体患者进行二分类任务的微调。核心创新在于将自然语言处理中的tokenization和自监督预训练范式迁移到脑电信号分析领域。

【实验结果 / Results】
在TUH EEG数据集的多名受试者上，所提方法实现了90%以上的验证准确率和0.80以上的F1分数，表明该患者自适应Transformer网络在个体化癫痫发作预测任务上具有稳定且优异的性能表现。

【应用价值 / Applications】
该研究为临床癫痫监测和预警系统提供了新的技术路径，可集成于可穿戴脑电设备或医院监护系统中，实现发作前的实时预警，从而为患者争取宝贵的干预时间窗口，改善癫痫患者的生活质量和安全管理。
