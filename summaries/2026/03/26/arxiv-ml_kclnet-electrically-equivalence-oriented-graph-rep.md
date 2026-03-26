---
title: "KCLNet: Electrically Equivalence-Oriented Graph Representation Learning for Analog Circuits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24101"
published: "2026-03-26"
summarized: "2026-03-27T07:20:23.564342"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了KCLNet，一种面向直流电气等效的模拟电路图表示学习框架。该框架采用异步图神经网络结构和电气模拟消息传递机制，并基于基尔霍夫电流定律（KCL）设计表示学习方法，通过约束每个深度层 outgoing 与 incoming 电流嵌入之和相等来维持嵌入空间的有序性。实验表明，KCLNet在模拟电路分类、子电路检测和电路编辑距离预测等下游任务中均取得显著性能提升。

【方法概述 / Method】

KCLNet 采用异步图神经网络架构，通过电气模拟消息传递机制处理模拟电路的连续电气特性。核心创新在于将基尔霍夫电流定律（KCL）融入表示学习：在网络每一深度层，强制节点的 outgoing 电流嵌入总和与 incoming 电流嵌入总和相等，以此编码电路的物理约束，增强嵌入空间的结构性和泛化能力。

【实验结果 / Results】

论文在多个下游任务上验证了 KCLNet 的有效性，包括模拟电路分类、子电路检测和电路编辑距离预测。结果表明，该方法显著优于现有基线，能够有效捕捉模拟电路的电气等效特性，并在不同任务间展现出良好的泛化性能。

【应用价值 / Applications】

KCLNet 为电子设计自动化（EDA）领域的模拟电路分析提供了新的技术路径，可支持电路智能分类、模块化子电路识别、以及电路相似性度量等关键任务。该方法有助于提升模拟集成电路设计的自动化水平，降低人工分析成本，加速芯片设计迭代周期。
