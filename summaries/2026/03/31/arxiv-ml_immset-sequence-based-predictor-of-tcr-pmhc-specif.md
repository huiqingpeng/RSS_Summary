---
title: "ImmSET: Sequence-Based Predictor of TCR-pMHC Specificity at Scale"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26994"
published: "2026-03-31"
summarized: "2026-04-01T07:21:00.528635"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究提出 ImmSET（Immune Synapse Encoding Transformer），一种用于预测 T 细胞受体（TCR）与肽-MHC 复合物（pMHC）特异性结合的新型序列架构。该模型能够处理可变长度生物序列集合的交互建模，并在严格评估下克服了先前方法存在的性能虚高问题。研究系统验证了 ImmSET 在多种数据类型上的规模扩展性，证明其在充足训练数据条件下可优于 AlphaFold2/3 的预测流程，为免疫治疗开发建立了可扩展的计算范式。

【方法概述 / Method】

ImmSET 采用基于 Transformer 的序列编码架构，专门设计用于建模多组可变长度生物序列（TCR α链、β链及 pMHC）之间的相互作用关系。该方法通过序列驱动的方式进行高通量推理，区别于传统的结构预测方法，并可针对不同数据集规模和组成进行训练优化。

【实验结果 / Results】

研究表明 ImmSET 的性能随训练数据量增长而持续提升，在多个数据类型上表现一致；在与预训练蛋白质语言模型 ESM2 的对比中，ImmSET 在相同数据集上展现出更优的微调效果。当提供充足训练数据时，ImmSET 在 TCR-pMHC 特异性预测任务上超越了基于 AlphaFold2 和 AlphaFold3 的预测流程。

【应用价值 / Applications】

ImmSET 为理解适应性免疫机制和开发个性化免疫疗法（如肿瘤免疫治疗、自身免疫疾病干预）提供了可扩展的计算工具。该建模范式不仅适用于 TCR-pMHC 相互作用预测，还可推广至其他需要高通量序列交互推理的生物学领域，与结构预测和实验验证形成互补。
