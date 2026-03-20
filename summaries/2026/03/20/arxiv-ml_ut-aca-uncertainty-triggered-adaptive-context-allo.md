---
title: "UT-ACA: Uncertainty-Triggered Adaptive Context Allocation for Long-Context Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18446"
published: "2026-03-20"
summarized: "2026-03-20T13:13:11.722417"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了不确定性触发的自适应上下文分配方法（UT-ACA），用于解决长上下文推理中的注意力稀释和分布外退化问题。该方法通过动态调整上下文窗口，基于token级别的不确定性来优化计算资源分配。实验表明，UT-ACA在保持生成质量的同时显著降低了平均上下文使用量。

【方法概述 / Method】
UT-ACA框架在推理时动态调整上下文窗口，通过学习一个不确定性检测器来监测语义嵌入和基于logit的置信度，并考虑解码步骤中的不确定性累积。当检测到证据不足时，系统会回滚、扩展上下文窗口并重新生成token。

【实验结果 / Results】
实验结果表明，UT-ACA在长上下文设置中大幅减少了平均上下文使用量，同时保持了生成质量，证明了该方法在计算效率和输出质量之间取得了有效平衡。

【应用价值 / Applications】
UT-ACA适用于需要处理长文档的大型语言模型应用场景，如法律文档分析、学术论文阅读和长对话系统等，能够显著降低推理计算成本，提升长上下文任务的实际部署效率。
