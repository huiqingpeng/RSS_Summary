---
title: "Neural Uncertainty Principle: A Unified View of Adversarial Fragility and LLM Hallucination"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19562"
published: "2026-03-23"
summarized: "2026-03-24T07:19:39.326790"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了**神经不确定性原理（Neural Uncertainty Principle, NUP）**，首次揭示了视觉对抗脆弱性与大语言模型幻觉这两个看似独立的问题具有共同的几何起源：输入与其损失梯度是满足不可约不确定性界限的共轭可观测量。研究表明，在接近界限的压缩状态下，模型会表现出对抗脆弱性；而提示-梯度耦合较弱时，则导致生成过程欠约束而产生幻觉。基于这一统一理论框架，作者设计了无需对抗训练即可提升鲁棒性的ConjMask和LogitReg方法，以及无需解码即可检测幻觉风险的探针工具。

【方法概述 / Method】

作者通过形式化"损失诱导状态"下的输入-梯度共轭关系，建立了神经不确定性原理的数学框架，并设计了**单次反向传播探针（single-backward probe）**来量化输入-梯度相关性通道。该探针可在预填充阶段（prefill-stage）评估提示与梯度的耦合强度，从而预测模型的不可靠行为。基于NUP理论指导，提出了两种具体技术：**ConjMask**（掩蔽高贡献输入成分）和**LogitReg**（logit侧正则化）。

【实验结果 / Results】

在视觉任务中，ConjMask方法在不进行昂贵对抗训练的情况下显著提升了模型鲁棒性；在语言任务中，单次反向传播探针能够在生成任何答案token之前有效检测幻觉风险，并实现提示选择优化。实验验证了该探针作为**免解码风险信号（decoding-free risk signal）**的有效性，为LLM的可靠性分析提供了可量化的诊断工具。

【应用价值 / Applications】

NUP框架为感知任务（视觉）和生成任务（语言）中的边界异常诊断与缓解提供了统一、可操作的解决方案。实际应用包括：**低成本提升视觉模型对抗鲁棒性**（无需对抗训练）、**LLM幻觉的早期预警与防控**（生成前风险评估）、**智能提示工程**（自动选择低幻觉风险提示）。该研究为构建更可靠的神经网络系统提供了理论基础和实践工具，特别适用于安全关键型AI应用场景。
