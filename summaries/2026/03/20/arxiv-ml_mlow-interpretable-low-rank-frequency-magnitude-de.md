---
title: "MLOW: Interpretable Low-Rank Frequency Magnitude Decomposition of Multiple Effects for Time Series Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18432"
published: "2026-03-20"
summarized: "2026-03-20T12:11:40.907047"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为MLOW的可解释低秩频率幅度分解方法，用于时间序列预测中的多效应分离。该方法基于核心洞察：时间序列可表示为幅度谱与相位感知基函数的乘积，且不同效应的幅度谱分布呈现可观测模式。MLOW通过学习幅度谱的低秩表示来捕捉主导趋势和季节性效应，并提出了一种新的超平面非负矩阵分解（Hyperplane-NMF）方法，以解决现有低秩方法在可解释性、效率和泛化性之间的权衡问题。

【方法概述 / Method】
MLOW采用基于频率的分解流程，将时间序列分解为幅度谱和相位感知基函数，并引入低秩矩阵分解技术提取主导效应。针对现有PCA、NMF和Semi-NMF方法的局限性，作者创新性地提出Hyperplane-NMF算法；同时设计数学机制实现输入时间窗口和频率级别的灵活选择，以缓解频谱泄漏问题对低秩分解质量的限制。

【实验结果 / Results】
可视化分析表明，MLOW能够实现可解释的分层多效应分解，且对噪声具有鲁棒性。该方法可作为即插即用模块嵌入现有时间序列预测骨干网络，在最小架构修改的前提下带来显著的性能提升，验证了其在实际预测任务中的有效性和通用性。

【应用价值 / Applications】
MLOW适用于需要理解时间序列内在驱动因素的场景，如金融趋势分析、能源负荷预测和气象建模等领域，其可解释性分解有助于分析师识别趋势、季节性等独立效应。此外，其即插即用特性使其能够快速集成到工业级预测系统中，提升模型透明度和预测精度的同时降低部署成本。
