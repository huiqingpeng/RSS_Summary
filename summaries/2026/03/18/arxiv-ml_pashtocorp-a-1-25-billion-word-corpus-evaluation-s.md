---
title: "PashtoCorp: A 1.25-Billion-Word Corpus, Evaluation Suite, and Reproducible Pipeline for Low-Resource Language Development"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16354"
published: "2026-03-18"
summarized: "2026-03-18T16:12:40.521467"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文介绍了PashtoCorp，一个包含12.5亿词的普什图语语料库。普什图语是6000万人使用的语言，但在NLP领域严重缺乏资源。该语料库整合了39个来源的数据，规模是此前最大专用普什图语语料库的83倍。基于该语料库的持续预训练显著提升了模型性能：困惑度降低25.1%，命名实体识别F1分数相对提升10%，并在Belebele阅读理解基准上首次建立了大语言模型的基线结果。

【方法概述 / Method】

研究者构建了一个可复现的数据处理流程，包括阿拉伯文字分词、SHA-256去重和质量过滤。语料库数据来自7个HuggingFace数据集和32个专门开发的网络爬虫。采用掩码语言模型（MLM）持续预训练策略，在XLM-R-base基础上进行领域自适应。通过留一法消融实验评估不同数据源对下游任务的贡献度。

【实验结果 / Results】

在WikiANN命名实体识别任务上，预训练模型将实体F1从19.0%提升至21.0%，训练方差降低近7倍；在仅有50条训练样本的低资源设置下提升幅度达27%。Gemma-3n在Belebele普什图语阅读理解上达到64.6%准确率。消融实验发现，仅占0.7%文档量的Wikipedia是NER任务最关键的数据源，移除后F1下降47%。

【应用价值 / Applications】

该研究为低资源语言NLP开发提供了可复现的完整范式，包括大规模语料构建、评估套件和训练流程。PashtoCorp可支持普什图语的机器翻译、信息抽取、阅读理解等应用，对阿富汗及巴基斯坦地区的数字资源建设具有重要社会价值。方法论可迁移至其他低资源语言，推动全球语言技术公平发展。
