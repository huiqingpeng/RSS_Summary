---
title: "A Direct Classification Approach for Reliable Wind Ramp Event Forecasting under Severe Class Imbalance"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22326"
published: "2026-03-25"
summarized: "2026-03-26T07:11:43.511194"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对风力发电爬坡事件（WPRE）预测中的严重类别不平衡问题（爬坡事件占比通常低于15%），提出了一种直接分类方法。该方法将WPRE预测转化为多元时间序列分类任务，并结合多数类欠采样与集成学习策略，有效解决了传统机器学习模型偏向多数类的缺陷。在真实数据集上的数值模拟表明，该方法准确率超过85%，加权F1分数达88%，优于基准分类器。

【方法概述 / Method】
论文采用多元时间序列分类框架，设计了数据预处理策略：从近期功率观测中提取特征，并对不可用的爬坡信息进行掩码处理，使其可与传统实时爬坡识别工具集成。核心技术结合多数类欠采样（majority-class undersampling）与集成学习（ensemble learning），以缓解类别不平衡对模型性能的负面影响。

【实验结果 / Results】
在真实世界数据集上的数值实验显示，所提方法实现了超过85%的准确率和88%的加权F1分数，显著优于基准分类器。结果表明，该直接分类方法在处理严重类别不平衡的风电爬坡事件预测任务中具有可靠的性能表现。

【应用价值 / Applications】
该研究可直接应用于风力发电厂的决策支持系统，为控制室操作员提供实时爬坡事件预警，支撑及时的电网稳定性评估与预防性调控。研究成果有助于提升低碳电力系统的运行可靠性，对可再生能源大规模并网背景下的电网安全具有重要实践意义。
