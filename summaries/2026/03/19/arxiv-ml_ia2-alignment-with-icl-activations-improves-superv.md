---
title: "IA2: Alignment with ICL Activations Improves Supervised Fine-Tuning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.22621"
published: "2026-03-19"
summarized: "2026-03-19T14:07:00.215714"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为ICL Activation Alignment（IA²）的自蒸馏技术，通过复制上下文学习（ICL）的激活模式来改进监督微调（SFT）。研究发现ICL和SFT产生不同的激活模式，表明两者通过不同的功能机制实现模型适应。在12个主流基准测试和两个模型家族上的大量实验表明，将IA²作为SFT前的预训练步骤能显著提升模型输出的准确性和校准度，同时为理解模型适应的内部机制提供了概念窗口。

【方法概述 / Method】
IA²是一种自蒸馏技术，通过让SFT模型模仿ICL的激活模式来激励ICL式的内部推理。具体实现上，该方法首先分析ICL和SFT产生的不同激活模式，然后设计目标函数使SFT模型在内部计算层面与ICL对齐，作为标准SFT前的"预启动"步骤。

【实验结果 / Results】
研究在12个流行基准测试和两个模型家族上进行了广泛评估，结果表明执行IA²作为SFT前置步骤能显著提升模型准确性和校准度。实验验证了ICL和SFT确实存在不同的功能机制，且通过激活对齐可以有效结合两者的优势。

【应用价值 / Applications】
该技术可应用于需要高精度且良好校准的语言模型场景，如医疗诊断、法律问答等高风险决策领域。IA²提供了一种计算高效的方案，在保持SFT推理效率的同时获得ICL的泛化能力和校准特性，特别适用于数据稀缺的实际部署环境。
