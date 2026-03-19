---
title: "Tokenization vs. Augmentation: A Systematic Study of Writer Variance in IMU-Based Online Handwriting Recognition"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16883"
published: "2026-03-19"
summarized: "2026-03-19T12:19:17.417983"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究系统探讨了两种解决IMU在线手写识别中字符分布不均和书写者差异问题的策略：子词分词（tokenization）和基于拼接的数据增强。研究发现，分词和增强策略在处理书写者间差异（inter-writer）和书写者内差异（intra-writer）方面存在明显二分效应：Bigram分词显著改善了对未知书写风格的泛化能力，而拼接增强则有效补偿了书写者内部的数据分布稀疏问题。

【方法概述 / Method】
论文对比研究了两种技术方案：（1）子词分词策略，通过Bigram等结构抽象方法将字符序列分解为更短的低层级token；（2）基于拼接的数据增强方法，通过连接多个样本生成更长的训练序列。实验在OnHW-Words500数据集上进行，分别评估了书写者无关（writer-independent）和书写者相关（writer-dependent）两种划分设置。

【实验结果 / Results】
在书写者无关划分上，Bigram分词将词错误率（WER）从15.40%降至12.99%，显著提升了对新书写风格的识别能力；然而在书写者相关划分上，分词因训练集与验证集词汇分布偏移而导致性能下降。相反，拼接增强在该设置下表现优异，字符错误率降低34.5%，词错误率降低25.4%，且其性能增益超过了单纯按比例扩展训练数据的效果。

【应用价值 / Applications】
该研究为IMU-based在线手写识别系统的设计提供了重要指导：当部署于多用户场景（如公共设备）时，应采用分词策略以增强对新用户的泛化能力；当针对特定用户优化时（如个人设备），则应采用拼接增强来充分利用有限的用户数据。这些发现对智能笔、数字手写板等设备的算法优化具有直接应用价值。
