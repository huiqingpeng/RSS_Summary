---
title: "Breaking Hard Isomorphism Benchmarks with DRESS"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18582"
published: "2026-03-20"
summarized: "2026-03-20T13:15:06.618411"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了DRESS框架的单删除变体Δ-DRESS，实证表明该算法在51,718个非同构强正则图（SRG）的16个参数族上实现了唯一指纹，并在包含Miyazaki、Chang、Paley等18个困难图族的34个基准测试族（共51,816个图实例）上达到100%的族内分离率。特别地，Δ-DRESS成功区分了3-WL算法无法区分的经典Rook L₂(4)与Shrikhande图对，证明其突破了3-WL的理论边界。

【方法概述 / Method】

Δ-DRESS采用单级顶点删除策略作用于DRESS图指纹，通过删除单个顶点生成子图多重集来构建图指纹；算法时间复杂度为多项式级别O(n·I·m·d_max)，流式实现仅需O(m+B+n)内存开销。

【实验结果 / Results】

实验覆盖51,718个SRG（16个参数族）和102个困难图（18个图族），实现100%族内分离率，隐式解决了超过5.76亿个族内非同构图对；成功分离3-WL无法区分的SRG(16,6,2,2)图对，突破了Weisfeiler-Leman算法的理论限制。

【应用价值 / Applications】

该研究为图同构问题提供了高效且强大的实用工具，可应用于计算化学、社交网络分析和组合设计验证等领域，特别适用于需要区分高度对称结构（如强正则图）的场景，同时其多项式时间复杂度保证了大规模图的可处理性。
