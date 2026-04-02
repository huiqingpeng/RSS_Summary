---
title: "Exploring Silent Data Corruption as a Reliability Challenge in LLM Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00726"
published: "2026-04-02"
summarized: "2026-04-03T07:24:02.533764"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文系统研究了静默数据损坏（Silent Data Corruption, SDC）对大语言模型（LLM）预训练可靠性的影响。通过在GPU矩阵乘法指令层面进行定向故障注入，作者发现硬件引发的SDC可导致梯度损坏、损失尖峰、参数发散等严重后果，且局部故障可能产生全局影响。基于对损坏特征的分析，论文提出了一种轻量级检测方法，通过识别有害参数更新并重新计算最近训练步骤，有效缓解了SDC的影响。

【方法概述 / Method】
研究采用控制实验方法，在GPU矩阵乘法指令级别进行定向故障注入，系统分析不同比特位、内核函数和执行阶段对SDC的敏感性。基于观察到的损坏特征（如NaN传播、损失/梯度范数/注意力logits的短期尖峰、参数持续发散），设计了轻量级检测机制。

【实验结果 / Results】
实验在60M、350M和1.3B参数的LLaMA模型上进行，验证了SDC可导致多种有害现象，包括数值异常传播和训练不稳定。所提出的检测-重计算方法能有效识别并缓解有害参数更新，显著降低SDC对训练过程的负面影响。

【应用价值 / Applications】
该研究为大规模LLM训练的可靠性保障提供了重要见解，提出的轻量级检测方案可直接集成到现有训练框架中，以较低开销实现SDC的实时监测与恢复。这对于降低超大规模模型训练中的硬件故障风险、节省数天至数周的计算资源具有重要意义。
