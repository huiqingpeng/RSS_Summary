---
title: "Breaking the $O(\sqrt{T})$ Cumulative Constraint Violation Barrier while Achieving $O(\sqrt{T})$ Static Regret in Constrained Online Convex Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20671"
published: "2026-03-24"
summarized: "2026-03-25T07:13:11.806064"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了带约束的在线凸优化问题，其中学习者在每轮选择动作后，会依次揭示凸损失函数和凸约束函数。研究目标是同时最小化静态遗憾（static regret）和累积约束违反（CCV）。此前工作普遍认为，对于任意维度 $d \ge 2$，任何保证 $O(\sqrt{T})$ 遗憾的算法其CCV下界为 $\Omega(\sqrt{T})$。本文反驳了这一观点，证明当 $d=2$ 时，Vaze和Sinha [2025] 的算法能够同时实现 $O(\sqrt{T})$ 的遗憾和 $O(T^{1/3})$ 的CCV，突破了长期存在的理论屏障。

【方法概述 / Method】

本文基于Vaze和Sinha [2025] 提出的算法框架，通过理论分析而非设计新算法来取得突破。核心方法是重新审视现有算法的理论保证，利用二维空间（$d=2$）的几何特性，建立更紧致的CCV上界分析，从而证明该算法在二维情况下可以获得优于此前认知的约束违反界。

【实验结果 / Results】

理论结果表明，在二维决策空间（$d=2$）中，该算法同时满足：静态遗憾为 $O(\sqrt{T})$，累积约束违反为 $O(T^{1/3})$。这一结果打破了此前认为 $O(\sqrt{T})$ 遗憾与 $O(\sqrt{T})$ CCV不可同时改进的普遍信念，首次在一般凸约束设置下实现了CCV的次平方根收敛。

【应用价值 / Applications】

该研究对资源分配、网络流量控制、在线广告竞价等具有时变约束的实时决策问题具有重要理论指导意义。特别是当决策变量可简化为二维（如价格-数量联合优化、双资源分配）时，该算法可在保证最优性差距可控的同时，显著降低长期约束违反，为设计更高效的安全在线学习系统提供了新的理论可能性。
