---
title: "A Tight Expressivity Hierarchy for GNN-Based Entity Resolution in Master Data Management"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27154"
published: "2026-03-31"
summarized: "2026-04-01T07:22:20.814123"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了基于图神经网络（GNN）的实体解析（Entity Resolution）任务的表达能力层次结构。作者发现，不同的实体解析任务具有根本不同的复杂度，使用完整扩展的消息传递神经网络（MPNN）会造成不必要的开销。论文建立了四个定理的分离理论，针对共引用谓词（Dup_r，表示两个同类型实体共享至少r个属性值）和ℓ-环谓词（Cyc_ℓ），证明了每种谓词所需的最小MPNN架构的紧确下界和上界。核心发现是：检测任意共享属性（纯局部任务）仅需两层反向消息传递，而检测多个共享属性（需要跨属性身份关联）则必须使用ego IDs和四层网络，即使在无环二分图上也是如此。

【方法概述 / Method】
论文采用理论分离（separation）方法，针对类型化的实体-属性图建立表达能力层次。对于每个目标谓词，作者构造出特定的图对（graph pairs），证明任何缺少必要扩展的MPNN都无法区分这些图对；同时构造显式的最小深度MPNN，证明该架构足以在所有输入上计算目标谓词。所考虑的MPNN扩展包括反向消息传递（reverse message passing）、端口编号（port numbering）和ego IDs。

【实验结果 / Results】
理论结果揭示了尖锐的复杂度鸿沟：Dup_1（检测任意共享属性）仅需反向消息传递和两层；而Dup_r（r≥2，检测多个共享属性）和Cyc_ℓ则需要ego IDs和四层，即使图是无环的。计算验证确认了所有理论预测。这些结果为每种谓词提供了最小充分架构的精确刻画，并证明不存在更简单的替代方案。

【应用价值 / Applications】
该研究为实体解析实践者提供了"最小架构原则"：可根据具体匹配准则选择最便宜的充分MPNN架构，并保证不存在更简单的有效方案。这有助于避免在简单任务上过度设计GNN架构，降低主数据管理（Master Data Management）中实体解析系统的计算开销，同时确保复杂任务获得必要的表达能力。
