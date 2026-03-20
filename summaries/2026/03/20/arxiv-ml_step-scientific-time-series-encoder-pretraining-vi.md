---
title: "STEP: Scientific Time-Series Encoder Pretraining via Cross-Domain Distillation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18688"
published: "2026-03-20"
summarized: "2026-03-20T12:14:49.467060"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了来自音频、通用时间序列和脑信号等相关领域的基础模型向科学时间序列的知识迁移能力，发现这些模型具有互补优势且能有效迁移到科学任务。基于此，作者提出STEP框架，通过跨域蒸馏将多领域知识整合到统一编码器中，并引入自适应分块和统计补偿机制处理科学时间序列的极端长度和多样数值尺度。在七个科学时间序列任务上的实验表明，STEP在模型结构和预训练范式上均取得显著效果。

【方法概述 / Method】
STEP框架包含三个核心组件：（1）自适应分块（adaptive patching）动态处理极端长度的科学时间序列；（2）统计补偿方案（statistics compensation）适应不同科学信号的数值尺度差异；（3）跨域蒸馏（cross-domain distillation）将多个相关领域基础模型的互补知识蒸馏到统一的科学时间序列编码器中。

【实验结果 / Results】
在七个科学时间序列任务上的实验表明，STEP显著优于现有方法，验证了跨域知识迁移的有效性和多领域基础模型的互补性。该方法同时提供了有效的模型架构和预训练范式，在科学时间序列表示学习任务上取得领先性能。

【应用价值 / Applications】
STEP为科学AI中的时间序列分析提供了统一的表示学习框架，可广泛应用于物理、化学、生物、地球科学等领域中稀疏、异构的科学信号处理。该方法通过利用现有大规模预训练模型的知识，降低了对大规模科学数据标注的依赖，有助于加速科学发现和研究进程。
