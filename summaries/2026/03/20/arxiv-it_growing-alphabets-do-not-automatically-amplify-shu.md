---
title: "Growing Alphabets Do Not Automatically Amplify Shuffle Privacy: Obstruction, Estimation Bounds, and Optimal Mechanism Design"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2603.18080"
published: "2026-03-20"
summarized: "2026-03-20T17:05:19.673736"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了在字母表规模 d → ∞ 增长情况下的洗牌差分隐私（shuffle privacy）机制设计问题。核心发现包括：证明了洗牌直方图实验的精确压缩定理，建立了普适的 χ² 上界 (e^{ε₀}-1)²/e^{ε₀}，并构造了隐私曲线恒等于二元随机响应的显式阻碍族；在估计理论方面，证明了阶为 (d-1)/(n χ*(W)) 的普适下界；在机制设计方面，发现校准的广义随机响应（GRR）并非最优，最优机制是"增强型GRR"——部分用户采用激进GRR，其余发送空符号，这一稀疏化原理为洗牌模型所特有。

【方法概述 / Method】

论文采用信息论与统计决策理论相结合的方法，运用 Cramér-Rao 不等式和 Assouad 引理建立估计下界，通过分析成对似然比的推前律（pushforward law）来刻画洗牌隐私的压缩结构，并利用对称化论证说明等变通道的不失一般性（WLOG）。

【实验结果 / Results】

研究建立了洗牌隐私的精确理论界限：χ² 预算满足普适上界 χ² ≤ (e^{ε₀}-1)²/e^{ε₀}；对于频率估计问题，证明了对称化到等变通道的最优性，并发现增强型GRR（以比例 p 采用激进参数 λ* = √(d-1) 的GRR，其余发送空符号）在低预算 0 < C ≤ C*(d) 范围内是所有置换等变通道中的最优机制，而标准GRR在子集选择族内是唯一优化器。

【应用价值 / Applications】

该研究为大规模字母表（如高维类别数据、大规模推荐系统）下的隐私保护频率估计提供了理论基础和最优机制设计指南，特别适用于联邦学习、人口统计调查等需要兼顾隐私性与统计效率的场景；所提出的"稀疏化"设计原则——部分用户主动不贡献信息——为实际分布式隐私系统提供了新的优化策略。
