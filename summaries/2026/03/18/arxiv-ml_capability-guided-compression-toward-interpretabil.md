---
title: "Capability-Guided Compression: Toward Interpretability-Aware Budget Allocation for Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16440"
published: "2026-03-18"
summarized: "2026-03-18T15:44:12.750866"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了**Capability-Guided Compression (CGC)**框架，旨在解决现有大语言模型压缩方法中"能力盲压缩"的根本局限——即压缩预算分配时完全忽略模型组件的功能编码信息。作者利用稀疏自编码器(SAE)提取的**能力密度图**来差异化分配压缩预算，并理论证明了高能力密度组件具有更低结构冗余且更早达到性能相变点。实验发现能力密度与现有Wanda重要性指标统计独立，为能力感知压缩研究奠定了理论基础。

---

【方法概述 / Method】

CGC框架通过稀疏自编码器(SAE)分析transformer组件的特征激活分布，定义**能力密度**为综合特征广度、激活熵和跨输入一致性的标量度量。基于该指标构建组件级能力密度图，指导差异化压缩预算分配，并提供预压缩机制预测各组件的性能相变临界点。

---

【实验结果 / Results】

在GPT-2 Medium上的实验显示，能力密度与Wanda重要性分数的Spearman相关系数仅为-0.054（n=384个头），证实其为独立于现有重要性度量的新信号。作者同时报告了一个**负面结果**：基于困惑度(PPL)的压缩比较无法验证CGC假设，并诊断GPT-2 Medium作为测试平台不足以支持完整假设检验。

---

【应用价值 / Applications】

该研究为大语言模型压缩提供了**可解释性驱动的预算分配**新范式，有望改善基于困惑度的评估与推理能力损失不敏感的问题，并预测缓解性能断崖式下降（相变）。理论框架和密度形式化为未来开发更精细的能力感知压缩算法（如针对推理、代码生成等特定能力保留）奠定了基础。
