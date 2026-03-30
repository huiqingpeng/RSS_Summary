---
title: "KANEL: Kolmogorov-Arnold Network Ensemble Learning Enables Early Hit Enrichment in High-Throughput Virtual Screening"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25755"
published: "2026-03-30"
summarized: "2026-03-31T07:26:55.369468"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究提出KANEL（Kolmogorov-Arnold Network Ensemble Learning），一种用于高通量虚拟筛选中早期命中率富集的集成学习框架。该工作将可解释的Kolmogorov-Arnold网络（KAN）与XGBoost、随机森林和多层感知机相结合，利用互补的分子表征（LillyMol描述符、RDKit描述符和Morgan指纹）进行训练。研究表明，在虚拟筛选应用中，基于前N个命中的阳性预测值（PPV@N）等早期命中率富集指标比传统的AUC等全局指标更具实际指导意义，KANEL在该任务上展现出优越性能。

【方法概述 / Method】

KANEL采用集成学习策略，核心组件包括Kolmogorov-Arnold网络（一种基于Kolmogorov-Arnold表示定理的新型神经网络架构）以及三种经典机器学习模型（XGBoost、随机森林、MLP）。该方法整合三种不同的分子表征：LillyMol专有描述符、RDKit开源描述符和Morgan分子指纹，通过多模型、多表征的协同预测提升虚拟筛选的可靠性。

【实验结果 / Results】

论文强调KANEL在早期命中率富集任务上的有效性，特别是在PPV@N等针对前N个候选化合物的评估指标上表现优异。相较于传统全局评估指标（如AUC），KANEL的集成策略能更准确地优先筛选出少量高活性化合物用于实验验证，但具体的基准数据集对比数值和统计显著性结果在提供的摘要中未详细说明。

【应用价值 / Applications】

该研究对药物发现中的高通量虚拟筛选具有直接应用价值，可帮助研究人员从海量化合物库中高效识别潜在活性分子，减少实验筛选成本。KANEL的集成设计兼顾模型可解释性（通过KAN）与预测性能，适用于需要优先确定少量候选化合物进行后续湿实验验证的实际场景，为机器学习辅助药物设计提供了更实用的评估范式。
