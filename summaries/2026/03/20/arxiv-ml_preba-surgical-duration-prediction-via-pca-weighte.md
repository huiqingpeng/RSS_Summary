---
title: "PREBA: Surgical Duration Prediction via PCA-Weighted Retrieval-Augmented LLMs and Bayesian Averaging Aggregation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.13275"
published: "2026-03-20"
summarized: "2026-03-20T14:13:17.379445"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了PREBA框架，通过PCA加权检索增强和贝叶斯平均聚合技术，将大语言模型（LLM）的预测锚定在机构特定的临床证据和统计先验上，解决了零样本LLM推理缺乏本地临床上下文的问题。该框架在真实临床数据集上显著提升了手术时长预测性能，MAE降低高达40%，R²从-0.13提升至0.62，且精度可与监督学习方法相媲美。

【方法概述 / Method】
PREBA首先将异构临床特征编码到统一表示空间，然后采用PCA加权检索识别最相关的历史病例作为证据上下文，最后通过贝叶斯平均将多轮LLM预测与群体级统计先验融合，生成经过校准的预测结果。

【实验结果 / Results】
在真实世界临床数据集上使用Qwen3、DeepSeek-R1和HuatuoGPT-o1三种先进LLM进行评估，PREBA相比零样本推理将MAE降低40%，R²从-0.13提升至0.62，达到与监督式机器学习方法相当的预测精度。

【应用价值 / Applications】
PREBA为医院手术排程和资源管理提供了无需大量标注数据、计算成本低的实用解决方案，特别适用于不同医疗机构快速部署个性化的手术时长预测系统，提升手术室利用率和运营效率。
