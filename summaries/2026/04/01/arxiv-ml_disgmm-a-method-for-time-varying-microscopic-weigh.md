---
title: "DiSGMM: A Method for Time-varying Microscopic Weight Completion on Road Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29837"
published: "2026-04-01"
summarized: "2026-04-02T07:21:04.285450"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了时变微观路网权重补全问题，旨在从稀疏观测的车辆轨迹数据中恢复所有道路段在当前时段的权重分布。针对网络层和路段层的双重稀疏性挑战，以及复杂交通条件（如重尾分布和多模态）的建模需求，作者提出了DiSGMM方法。实验表明，该方法在两个真实数据集上优于现有最先进方法。

【方法概述 / Method】
DiSGMM采用稀疏感知嵌入与时空建模相结合的技术方案，利用稀疏已知权重、学习到的路段属性及长程相关性进行分布估计。该方法将微观权重分布表示为可学习的高斯混合模型（GMM），以闭式形式灵活捕捉复杂交通条件。

【实验结果 / Results】
在两个真实世界数据集上的实验表明，DiSGMM能够超越现有最先进的方法，有效处理双重稀疏性问题，并成功建模包括重尾和多集群在内的复杂权重分布。

【应用价值 / Applications】
该研究可支持交通微观仿真和具有可靠性保证的车辆路径规划等实际应用，为智能交通系统提供精细化的时变路况预测能力，有助于提升导航服务的准确性和交通管理的精细化水平。
