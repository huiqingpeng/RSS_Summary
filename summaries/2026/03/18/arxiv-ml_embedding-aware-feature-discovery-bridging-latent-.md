---
title: "Embedding-Aware Feature Discovery: Bridging Latent Representations and Interpretable Features in Event Sequences"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15713"
published: "2026-03-18"
summarized: "2026-03-18T15:34:41.842963"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Embedding-Aware Feature Discovery (EAFD)框架，旨在弥合事件序列中预训练嵌入表示与可解释手工特征之间的鸿沟。EAFD通过自反思的LLM驱动特征生成智能体，结合"对齐性"（解释嵌入已编码信息）和"互补性"（发现嵌入缺失的预测信号）双重标准，从原始事件序列中迭代发现、评估和优化特征。在开源和工业交易基准测试中，EAFD相比最先进的预训练嵌入方法实现了最高+5.8%的相对提升，创造了事件序列数据集的新SOTA性能。

【方法概述 / Method】
EAFD采用统一的框架架构，将预训练事件序列嵌入与自反思的大语言模型驱动特征生成智能体相结合。该方法通过双重评估标准——对齐性（alignment）和互补性（complementarity）——迭代地从原始事件序列中发现、评估和精炼特征，实现嵌入表示与可解释特征的有机融合。

【实验结果 / Results】
在多个开源和工业交易基准数据集上，EAFD一致性地超越了纯嵌入方法和基于特征的基线方法。相比最先进的预训练嵌入方法，EAFD取得了最高达+5.8%的相对性能提升，并在事件序列数据集上达到了新的最优性能（state-of-the-art）。

【应用价值 / Applications】
该研究对工业金融系统具有重要价值，特别是在交易欺诈检测、用户行为分析和系统日志监控等需要同时满足高预测性能、模型可解释性和严格延迟约束的场景。EAFD为生产环境中平衡深度学习表示与传统特征工程提供了实用解决方案，有助于推动 learned embeddings 在实际业务系统中的落地应用。
