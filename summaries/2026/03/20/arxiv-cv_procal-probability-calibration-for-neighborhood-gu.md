---
title: "ProCal: Probability Calibration for Neighborhood-Guided Source-Free Domain Adaptation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18764"
published: "2026-03-20"
summarized: "2026-03-20T15:15:56.563544"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ProCal，一种用于无源域自适应（SFDA）的概率校准方法，通过双模型协同预测机制动态校准基于邻域的预测。该方法将源模型的初始预测与当前模型的在线输出相结合，有效缓解局部噪声干扰并保留源模型的判别信息，在知识保留与域自适应之间取得平衡。理论分析证明ProCal能收敛到源知识与目标信息有效融合的均衡状态，在4个公开数据集的31个跨域任务上验证了其有效性。

【方法概述 / Method】
ProCal采用双模型协同预测机制，整合源模型的初始预测和当前模型的在线输出来动态校准邻居概率分布。该方法设计了联合优化目标，结合软监督损失和多样性损失来引导目标模型学习，并通过理论分析确保收敛到知识融合的最优均衡点。

【实验结果 / Results】
ProCal在4个公开数据集（包括Office-31、Office-Home、VisDA和DomainNet）的31个跨域任务上进行了广泛验证，实验结果表明该方法有效减少了知识遗忘和过拟合问题，在标准SFDA基准上取得了领先的性能表现。

【应用价值 / Applications】
ProCal适用于无法获取源训练数据的域自适应场景，如隐私敏感的医疗影像分析、跨设备视觉识别和模型部署后的持续适应等实际应用，为预训练模型在新环境下的可靠迁移提供了高效解决方案。
