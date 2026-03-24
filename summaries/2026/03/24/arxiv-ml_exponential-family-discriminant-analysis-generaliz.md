---
title: "Exponential Family Discriminant Analysis: Generalizing LDA-Style Generative Classification to Non-Gaussian Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20655"
published: "2026-03-24"
summarized: "2026-03-25T07:13:04.569414"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了指数族判别分析（EFDA），一个统一的生成式框架，将经典线性判别分析（LDA）从高斯假设推广到指数族的任意成员。EFDA假设每个类别的条件密度属于同一指数族，推导出所有自然参数的闭式最大似然估计，并产生一个关于充分统计量线性的决策规则。该方法在正确设定下具有渐近校准性和统计有效性，在五个指数族分布的模拟实验中，EFDA在保持与LDA、QDA和逻辑回归相当分类准确率的同时，将期望校准误差（ECE）降低了2-6倍。

【方法概述 / Method】

EFDA的核心方法是假设类别条件密度服从共同的指数族分布，利用指数族的共轭性质推导自然参数的闭式MLE估计。决策规则在充分统计量空间中是线性的，但在原始特征空间中可捕捉非线性边界；该方法被推广到K≥2个类别和多元数据情形，并为九种分布提供了完整推导。

【实验结果 / Results】

在Weibull、Gamma、Exponential、Poisson和Negative Binomial五种分布上的广泛模拟显示，EFDA与LDA、QDA和逻辑回归的分类准确率相当，但期望校准误差（ECE）显著降低2-6倍——这一差距具有结构性，在所有样本量和类别不平衡水平下持续存在。此外，EFDA的对数几率估计量在正确设定下趋近Cramér-Rao下界，是所比较方法中唯一均方误差收敛到零的估计量。

【应用价值 / Applications】

EFDA适用于任何具有非高斯类别条件分布的分类任务，特别是在需要良好概率校准的场景（如医疗诊断、金融风险评估和不确定性量化）。该框架为传统LDA无法处理的计数数据（Poisson）、等待时间数据（Exponential/Gamma/Weibull）或过离散数据（Negative Binomial）提供了原则性的生成式分类方法，同时保持计算效率和可解释性。
