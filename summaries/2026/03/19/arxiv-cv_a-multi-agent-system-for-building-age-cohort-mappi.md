---
title: "A Multi-Agent System for Building-Age Cohort Mapping to Support Urban Energy Planning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17626"
published: "2026-03-19"
summarized: "2026-03-19T15:15:04.462962"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种多智能体大语言模型系统，用于解决城市建筑年龄分布数据缺失和不一致的问题，以支持可持续市政供暖规划。该系统整合了三个关键智能体（Zensus、OSM和Monument智能体）融合多源异构数据，并构建了BuildingAgeCNN卫星图像分类器，在仅使用卫星数据的情况下实现了90.69%的整体准确率。研究还引入了校准置信度估计机制，为能源规划应用中的风险评估提供支持。

【方法概述 / Method】
论文采用多智能体LLM架构，通过数据编排器与协调器对建筑轮廓进行地理编码和去重处理。核心分类模型BuildingAgeCNN以ConvNeXt为骨干网络，融合特征金字塔网络（FPN）、CoordConv空间通道和Squeeze-and-Excitation（SE）注意力模块，实现仅基于卫星图像的建筑年代分类。

【实验结果 / Results】
在空间交叉验证下，BuildingAgeCNN达到90.69%的整体准确率，但宏平均F1分数为67.25%，反映出类别不平衡问题以及相邻历史时期建筑之间的持续混淆。系统通过校准置信度估计识别低置信度预测案例，触发人工审核机制以降低规划应用风险。

【应用价值 / Applications】
该研究可直接应用于城市能源需求规划，帮助优化区域供热网络布局，并精准定位低碳可持续能源系统的改造目标。多智能体数据融合方法为缺乏完整建筑登记数据的城市提供了可扩展的解决方案，对市政热规划决策和建筑升级优先级排序具有重要实践意义。
