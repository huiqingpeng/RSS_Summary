---
title: "Attention Sinks Induce Gradient Sinks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17771"
published: "2026-03-19"
summarized: "2026-03-19T12:16:28.339219"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文揭示了Transformer模型中两个重要现象——注意力汇聚（attention sinks）和巨大激活（massive activations）——之间的深层联系。研究表明，在因果掩码条件下，注意力汇聚会导致梯度在特定位置高度集中，形成"梯度汇聚"（gradient sinks）；而在采用RMSNorm的pre-norm架构中，巨大激活可理解为模型对局部梯度压力的自适应响应。作者通过引入V-scale方法验证了这一假设，发现预训练后的V-scale模型保留了注意力汇聚但抑制了巨大激活，证明梯度汇聚是连接这两个现象的关键训练时中介机制。

【方法概述 / Method】
本文从反向传播视角出发，结合理论分析和实证研究，系统考察注意力汇聚与梯度汇聚的因果关系。作者设计了V-scale改进方法，通过调整value路径反向传播梯度的缩放机制，来干预梯度汇聚效应，从而检验巨大激活是否是对梯度压力的响应。

【实验结果 / Results】
V-scale实验表明，在预训练模型中，注意力汇聚现象得以保留，而巨大激活被显著抑制，支持了梯度汇聚作为中介机制的理论假设。理论分析和实验结果一致表明，因果掩码下的注意力汇聚确实会诱导明显的梯度集中现象。

【应用价值 / Applications】
本研究为理解和优化Transformer训练动态提供了新视角，有助于设计更稳定的训练策略和架构改进。V-scale方法可直接应用于大型语言模型的训练优化，减少巨大激活带来的数值稳定性问题，同时保持注意力机制的有效性，对提升模型训练效率和可解释性具有实际意义。
