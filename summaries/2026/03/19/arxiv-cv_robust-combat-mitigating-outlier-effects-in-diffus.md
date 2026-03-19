---
title: "Robust-ComBat: Mitigating Outlier Effects in Diffusion MRI Data Harmonization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17968"
published: "2026-03-19"
summarized: "2026-03-19T16:19:35.811708"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Robust-ComBat方法，用于解决扩散MRI数据协调中病理异常值带来的问题。传统ComBat方法假设数据服从高斯分布，但神经疾病患者的扩散指标常显著偏离健康对照，导致站点效应估计失真。研究评估了10种异常值拒绝方法与4种ComBat变体，发现简单的MLP能有效补偿异常值，在包含高达80%神经疾病患者的多站点队列中，Robust-ComBat始终优于传统统计基线，同时保留疾病相关信号。

【方法概述 / Method】
Robust-ComBat采用多层感知机（MLP）进行稳健的异常值补偿，替代传统的统计过滤策略。该方法不直接剔除病理样本，而是通过神经网络学习对异常值的鲁棒处理，从而在协调过程中同时处理站点效应和病理偏差。研究在7种神经疾病条件下，对比了多种ComBat变体（包括标准ComBat、ComBat-GAM等）与不同异常值检测策略的组合。

【实验结果 / Results】
在包含高达80%神经疾病患者的真实多站点队列中，Robust-ComBat在所有ComBat变体上均实现了更低的协调误差。研究表明，许多传统的异常值过滤策略在存在病理情况时失效，而MLP-based的补偿方法能有效分离站点效应与疾病信号，在保持疾病相关生物学变异的同时消除站点偏差。

【应用价值 / Applications】
该方法对临床实践具有重要价值，尤其适用于诊断前未知病理状态的神经影像数据协调。Robust-ComBat可整合到现有的多站点神经影像研究流程中，支持阿尔茨海默病、帕金森病等神经退行性疾病的跨中心研究，无需预先排除潜在患者即可实现可靠的统计分析和生物标志物发现。
