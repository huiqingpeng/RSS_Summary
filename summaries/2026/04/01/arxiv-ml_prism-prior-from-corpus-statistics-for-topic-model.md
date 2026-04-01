---
title: "PRISM: PRIor from corpus Statistics for topic Modeling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29406"
published: "2026-04-01"
summarized: "2026-04-02T07:18:00.307273"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出 PRISM（PRIor from corpus Statistics for topic Modeling），一种从语料库内部词共现统计中派生狄利克雷参数来初始化 LDA 的方法，无需修改 LDA 的生成过程或依赖外部知识。实验表明，PRISM 在文本和单细胞 RNA-seq 数据上均提升了主题一致性和可解释性，性能可与依赖外部知识的模型相媲美。该研究凸显了在资源受限场景下利用语料库驱动初始化的价值。

【方法概述 / Method】
PRISM 通过分析语料库内词的共现统计信息，计算得到一个数据驱动的狄利克雷先验参数，用于初始化传统 LDA 模型。该方法完全基于语料库内在特征，不引入预训练嵌入等外部知识，同时保持 LDA 原有的生成概率框架不变。

【实验结果 / Results】
PRISM 在标准文本数据集和单细胞 RNA-seq 生物数据上均取得显著效果，主题一致性指标得到明显改善。与依赖外部预训练知识的先进方法相比，PRISM 达到了可比拟甚至更优的性能，同时保持了更好的计算效率和领域适应性。

【应用价值 / Applications】
PRISM 特别适用于新兴领域或数据稀缺的低资源场景，如特定科学文献分析、罕见疾病研究、小众语言处理等难以获取大规模预训练资源的领域。该方法为无法依赖外部知识库的受限环境提供了高质量主题建模的实用解决方案。
