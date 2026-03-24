---
title: "SDE-Driven Spatio-Temporal Hypergraph Neural Networks for Irregular Longitudinal fMRI Connectome Modeling in Alzheimer's Disease"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20452"
published: "2026-03-24"
summarized: "2026-03-25T07:10:03.178034"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SDE-HGNN，一种基于随机微分方程（SDE）驱动的时空超图神经网络，用于解决阿尔茨海默病（AD）纵向fMRI连接组建模中的不规则采样和缺失访视问题。该框架通过SDE重建模块从不规则观测中恢复连续潜在轨迹，并构建动态超图捕捉脑区之间的高阶时序交互。在OASIS-3和ADNI队列上的实验表明，该方法在AD进展预测任务上显著优于现有图和超图基线方法。

【方法概述 / Method】
SDE-HGNN采用三阶段架构：首先利用SDE-based重建模块将不规则的纵向神经影像数据插值为连续潜在表示；其次基于重建特征构建动态超图以建模脑区间的复杂高阶关系；最后通过SDE控制的循环动态机制使超图卷积参数随扫描间隔自适应演化，实现疾病阶段自适应的连接模式建模。

【实验结果 / Results】
在OASIS-3和ADNI两个公开AD队列上的广泛实验表明，SDE-HGNN在AD进展预测任务上一致性地超越了最先进的图神经网络和超图神经网络基线；此外，稀疏重要性学习机制有效识别出与疾病相关的关键脑区和判别性连接模式，为神经影像标志物发现提供了可解释性支持。

【应用价值 / Applications】
该研究为临床AD监测提供了处理不规则纵向神经影像数据的鲁棒工具，可应用于疾病进展预测、早期诊断和个性化治疗规划；其SDE驱动的连续时间建模框架具有泛化潜力，可扩展至帕金森病、多发性硬化症等其他神经退行性疾病的纵向影像分析。
