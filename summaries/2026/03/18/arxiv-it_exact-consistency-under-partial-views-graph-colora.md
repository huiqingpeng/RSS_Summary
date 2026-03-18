---
title: "Exact Consistency Under Partial Views: Graph Colorability, Capacity, and Equality in Multi-Location Encodings"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2602.23520"
published: "2026-03-18"
summarized: "2026-03-18T19:10:28.030534"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文构建了多位置编码(multi-location encodings)失效的结构理论。作者证明：可容许的部分视图会在潜在元组上诱导出混淆图(confusability graph)；在精确坐标视图模型中，该图类可由坐标一致集的向上闭族精确刻画，而使用T进制标签的精确恢复等价于T-可着色性。重复组合产生强幂次，归一化块速率序列收敛于渐近香农容量，其上界为Lovász-ϑ函数。当混淆关系具有传递性时，该上界理论是紧的；meet-witnessing和fiber coherence提供了可验证的充分条件。

【方法概述 / Method】

论文采用图论与信息论相结合的方法，将多位置编码的一致性问题转化为图着色问题。核心工具包括：利用向上闭族(upward-closed families)对混淆图进行组合刻画，通过Lovász ϑ函数建立容量上界，以及引入仿射限制下的可表示拟阵(representable matroid)来约束混淆性。作者还发展了meet-witnessing和fiber coherence等代数条件来判定传递性。

【实验结果 / Results】

理论结果表明：(1) 渐近香农容量存在且被Lovász-ϑ函数上界约束；(2) 当混淆关系传递时，该上界是紧的（达到容量）；(3) 在仿射结构下，拟阵秩给出了混淆性的组合上界。这些结果为编码设计提供了可计算的复杂度界限和可验证的正确性条件。

【应用价值 / Applications】

该理论统一适用于编程语言运行时、数据库和依赖管理器等系统。核心应用价值在于：建立了因果传播(causal propagation)与来源可观测性(provenance observability)作为可验证结构完整性的充要条件，为分布式系统、版本控制和软件供应链安全中的数据一致性验证提供了理论基础。
