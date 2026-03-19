---
title: "Wasserstein-type Gaussian Process Regressions for Input Measurement Uncertainty"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17271"
published: "2026-03-19"
summarized: "2026-03-19T13:11:03.411427"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了输入变量存在测量误差时的高斯过程（GP）回归问题，提出了一种基于Wasserstein距离的框架来处理输入不确定性。作者将含噪声的输入表示为概率测度，并通过Wasserstein距离定义协方差函数，构建了投影Wasserstein ARD（PWA）核函数。该方法避免了传统潜变量GP模型需要引入未观测协变量或蒙特卡洛投影的复杂性，实现了更透明、更鲁棒的不确定性量化。

【方法概述 / Method】
核心方法是定义基于Wasserstein距离的核函数：将每个噪声输入视为概率分布，利用Wasserstein距离度量分布间的相似性来构造协方差。具体实现了投影Wasserstein ARD（PWA）核，其一维分量具有闭式表达式，乘积结构保证了核函数的正定性和可扩展性。

【实验结果 / Results】
（注：提供的论文片段未包含具体实验结果部分，仅包含摘要和元数据。根据摘要推断）PWA-based GPs（PWAGPs）相比标准GP回归在输入含噪声时能提供更准确的后验区间，避免了过于乐观的窄区间和偏差决策；相比潜变量GP方法，该方法无需蒙特卡洛采样即可实现高效推断。

【应用价值 / Applications】
该方法适用于任何输入测量存在不确定性的场景，如传感器数据采集、实验科学中的噪声测量、以及需要可靠不确定性量化的决策系统（如贝叶斯优化、主动学习）。其透明性和鲁棒性使其特别适合安全关键型应用中的风险评估和决策支持。
