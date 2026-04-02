---
title: "Event Embedding of Protein Networks : Compositional Learning of Biological Function"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00911"
published: "2026-04-02"
summarized: "2026-04-03T07:25:58.738565"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究探索了在蛋白质-蛋白质相互作用网络中强制施加严格组合结构是否能产生有意义的嵌入几何组织。作者使用基于加性序列嵌入模型Event2Vec，在人类STRING互作组上训练64维表示，并与基于Word2Vec的DeepWalk基线进行比较。研究发现，组合结构显著提升了通路一致性（较随机基线提升30.2倍 vs 2.9倍）和功能类比准确性（平均相似度0.966 vs 0.650），同时改善了层次化通路组织，而非组合基线则在某些几何特性上表现相当或更优。

【方法概述 / Method】
研究采用Event2Vec模型——一种具有显式组合结构的加性序列嵌入方法，在人类STRING蛋白质互作网络上进行随机游走采样并训练64维嵌入向量。作为对照，使用相同随机游走数据训练基于Word2Vec的DeepWalk基线模型，以隔离组合性对嵌入质量的影响。

【实验结果 / Results】
Event2Vec在通路一致性指标上达到30.2倍于随机水平的提升，远超DeepWalk的2.9倍；功能类比任务的平均相似度达0.966，显著优于DeepWalk的0.650。此外，组合嵌入展现出更优的层次化通路组织结构，而范数-度反相关等几何特性则与基线相当或由基线超越。

【应用价值 / Applications】
该研究为生物网络分析提供了更具组合推理能力的嵌入方法，可应用于蛋白质功能预测、信号通路分析和药物靶点发现等场景。强制组合性的嵌入框架有助于揭示生物系统的模块化功能组织，为理解复杂疾病机制和开发精准医疗策略提供计算工具支持。
