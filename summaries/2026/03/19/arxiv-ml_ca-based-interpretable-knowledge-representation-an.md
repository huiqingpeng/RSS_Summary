---
title: "CA-Based Interpretable Knowledge Representation and Analysis of Geometric Design Parameters"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17535"
published: "2026-03-19"
summarized: "2026-03-19T12:13:21.598150"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究针对CAD应用中复杂几何体由高维设计参数定义、导致下游工程任务困难的问题，聚焦于从PCA表示中估计原始设计参数的挑战。作者分析了一种针对该领域的PCA改进方法，发现其结果与标准PCA实质相同，并揭示了该方法的局限性。研究提出了获得准确且可解释参数估计的合理条件，并通过专门实验深入分析了PCA各阶段及几何体在过程中的可能变化。

【方法概述 / Method】

论文采用理论分析与实验验证相结合的方法，对比分析了标准PCA与一种针对CAD领域的改进PCA变体（CA, Component Analysis），证明两者在数学上的等价性。研究建立了从PCA潜变量反推原始设计参数的理论框架，并设计了多组专门实验来系统检验PCA各处理阶段对几何表示的影响。

【实验结果 / Results】

实验表明，在特定条件下（如设计参数与几何变化存在明确映射关系时），可以从PCA表示中准确恢复原始设计参数。研究详细展示了PCA编码（参数→几何→潜变量）和解码（潜变量→几何→参数）过程中几何信息的保持与损失情况，验证了所提条件对于获得可解释参数估计的必要性。

【应用价值 / Applications】

该研究对CAD/CAE集成、生成式设计及工程优化具有重要价值，使工程师能够在降维后的紧凑表示中仍理解原始设计参数的意义。成果可支持更高效的仿真驱动设计、智能优化算法的可解释性提升，以及复杂几何模型的交互式编辑与探索任务。
