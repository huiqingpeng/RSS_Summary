---
title: "Learnability with Partial Labels and Adaptive Nearest Neighbors"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15781"
published: "2026-03-18"
summarized: "2026-03-18T16:08:00.039892"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了偏标签学习（Partial Labels Learning, PLL）的理论基础与算法设计。首先，作者从数学上刻画了PLL可行的必要条件，填补了该领域理论空白。其次，提出了PL A-$k$NN算法——一种自适应最近邻方法，能够在一般PLL场景下提供性能保证。实验表明，该算法在多种PLL设定下优于现有最先进方法。

【方法概述 / Method】

PL A-$k$NN采用自适应最近邻策略，根据偏标签袋的信息动态调整邻居选择与权重分配。该算法通过理论分析确保在一般PLL场景下的学习可行性，无需依赖特定数据分布假设。

【实验结果 / Results】

实验验证了PL A-$k$NN在多种PLL场景下的优越性，能够稳定超越现有SOTA方法。结果支持了理论分析，表明该算法具有良好的泛化性能。

【应用价值 / Applications】

该研究适用于标注成本高昂或存在标注歧义的场景，如医学影像诊断（多位专家意见不一致）、众包标注、隐私敏感数据标注等。理论成果为设计更鲁棒的PLL算法提供了指导原则，算法本身可直接集成到实际标注系统中以降低标注成本。
