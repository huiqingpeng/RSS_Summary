---
title: "LogicXGNN: Grounded Logical Rules for Explaining Graph Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2503.19476"
published: "2026-03-18"
summarized: "2026-03-18T16:17:29.037830"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了LogicXGNN，一种用于解释图神经网络（GNN）的后置式框架。该框架通过构建基于可靠谓词的逻辑规则，显式捕捉GNN的消息传递结构，从而确保解释的有效落地（grounding）。作者还引入了数据落地保真度（Fid_D）这一现实评估指标，直接在最终子图形式上评估解释质量。实验表明，LogicXGNN相比最先进方法平均提升Fid_D超过20%，同时速度快10-100倍。

【方法概述 / Method】
LogicXGNN设计了一套专门捕捉GNN消息传递机制的可靠谓词系统，并在此基础上构建逻辑规则；该方法通过显式建模GNN的聚合与更新操作，确保生成的规则能够可靠地映射到可观察的数据子图上，避免了传统方法在中间概念空间优化而导致的落地失效问题。

【实验结果 / Results】
LogicXGNN在多个数据集上的广泛实验显示，其数据落地保真度（Fid_D）相比现有最优方法平均提升超过20%；同时计算效率显著提升，运行速度达到现有方法的10-100倍；此外，该方法在覆盖率和有效性等补充效用指标上也表现出色，具有良好的可扩展性。

【应用价值 / Applications】
LogicXGNN适用于需要高可信度解释的GNN应用场景，如药物发现中的分子性质预测、金融风控中的交易网络分析、以及社交网络中的推荐系统决策解释；其生成的逻辑规则既忠实于模型内部机制，又可直接对应到具体数据子结构，便于领域专家审验和监管合规。
