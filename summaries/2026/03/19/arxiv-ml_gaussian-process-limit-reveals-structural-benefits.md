---
title: "Gaussian Process Limit Reveals Structural Benefits of Graph Transformers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17569"
published: "2026-03-19"
summarized: "2026-03-19T13:13:50.554986"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究通过高斯过程极限理论揭示了图Transformer相比图卷积网络的结构优势。作者证明了在无限宽度和无限头数条件下，图Transformer（包括GAT、Graphormer和Specformer）能够在深层网络中保持社区信息并维持判别性节点表示，从而有效避免过平滑问题。该理论分析为图Transformer在实际任务中的优异表现提供了数学解释，并通过合成图和真实图数据进行了验证。

【方法概述 / Method】

作者采用神经网络的无限宽度极限分析方法，推导了图Transformer在无限宽度和无限头数条件下的高斯过程极限，并建立了节点级和边级的核函数表达式。通过分析这些核函数在层间的传播特性，刻画了节点特征与图结构在注意力层中的演化规律。

【实验结果 / Results】

理论分析表明图Transformer能够结构性保持社区信息，即使在深层网络中也不会出现过平滑现象；实验验证了整合信息性先验和位置编码可以显著提升深层图Transformer的性能，在合成图和真实图数据集上均支持了理论发现。

【应用价值 / Applications】

该研究为图Transformer的设计和优化提供了理论指导，特别是在构建深层图神经网络时可通过合理的位置编码和先验信息整合来提升性能。研究成果可应用于社交网络分析、分子性质预测、知识图谱推理等需要深层图表示学习的领域。
