---
title: "Circuit Complexity of Hierarchical Knowledge Tracing and Implications for Log-Precision Transformers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23823"
published: "2026-03-26"
summarized: "2026-03-27T07:17:39.714300"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文从电路复杂性角度分析层次化知识追踪中的先决条件传播问题，揭示了log-精度Transformer在深层概念层次上的计算能力边界。研究发现，递归多数先决条件传播问题无条件地属于NC¹复杂度类，但在单调性限制下，交替ALL/ANY先决条件树对单调阈值电路形成严格的深度层次。实验表明，Transformer编码器会收敛到置换不变的捷径，而通过对中间子树的辅助监督可以诱导出结构相关的计算，在深度3-4时达到近乎完美的准确率。

【方法概述 / Method】
论文采用理论分析与实证验证相结合的方法：理论上利用log-精度Transformer属于logspace-均匀TC⁰的最新结果，形式化定义递归多数掌握传播等先决条件树任务；实证上训练Transformer编码器，并通过辅助监督机制干预其学习过程。

【实验结果 / Results】
Transformer在递归多数树任务上表现出置换不变的捷径行为，仅靠显式结构无法阻止这一现象；引入中间子树的辅助监督后，模型能够利用结构信息进行计算，在深度3-4的层次结构上达到接近完美的准确率。

【应用价值 / Applications】
该研究为知识追踪系统的设计提供了理论指导，强调需要结构感知的目标函数和迭代机制来处理深层先决条件层次；对Transformer架构的局限性分析也有助于指导更高效的教育AI系统开发，特别是在需要精确建模概念依赖关系的智能辅导场景中。
