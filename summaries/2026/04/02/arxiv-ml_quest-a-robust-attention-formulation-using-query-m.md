---
title: "QUEST: A robust attention formulation using query-modulated spherical attention"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00199"
published: "2026-04-02"
summarized: "2026-04-03T07:18:11.918296"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为 QUEST（QUEry-modulated Spherical aTtention）的新型注意力机制，用于解决标准 Transformer 中因查询和键向量范数任意增长导致的训练不稳定问题。该方法将键约束到超球面潜在空间，同时允许单个 token 灵活控制注意力分布的锐度。实验表明，QUEST 可作为标准注意力的即插即用替代方案，在视觉及其他领域实现更稳定的训练、更优的性能，并对数据损坏和对抗攻击具有更强的鲁棒性。

【方法概述 / Method】
QUEST 通过将键向量归一化到单位超球面上，同时利用查询向量的范数来调制注意力分布的锐度，从而在保持表达能力的同时消除训练不稳定性。这种设计既约束了键的几何结构，又保留了查询对注意力集中程度的灵活控制。

【实验结果 / Results】
研究表明 QUEST 能够在存在虚假数据模式的简单 Transformer 模型中避免训练不稳定；在视觉任务及其他领域，QUEST 训练稳定且性能优于标准注意力机制；此外，采用 QUEST 的模型对数据损坏和对抗攻击表现出更强的鲁棒性。

【应用价值 / Applications】
QUEST 可直接替换现有 Transformer 模型中的标准注意力模块，无需修改整体架构，适用于计算机视觉及其他需要稳定训练和高鲁棒性的深度学习应用场景。该方法为构建更可靠、更安全的注意力机制提供了通用解决方案，特别适合对模型鲁棒性要求较高的实际部署环境。
