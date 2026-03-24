---
title: "Data-driven discovery of roughness descriptors for surface characterization and intimate contact modeling of unidirectional composite tapes"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20418"
published: "2026-03-24"
summarized: "2026-03-25T07:09:42.745587"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对单向复合材料胶带表面粗糙度表征问题，提出了一种基于秩降自编码器（Rank Reduction Autoencoders, RRAEs）的数据驱动方法，用于发现能够同时实现胶带分类和接触建模的粗糙度描述符。该方法通过在编码器-解码器训练过程中对潜在矩阵应用截断奇异值分解（SVD），强制潜在向量空间保持线性结构。研究发现，所提取的潜在SVD模式既能准确重构表面粗糙度，又能有效捕捉先验知识（如分类属性或建模特性），从而解决了传统统计描述符与界面物理过程脱节的关键问题。

【方法概述 / Method】

论文核心方法是秩降自编码器（RRAEs），其创新点在于训练过程中对潜在矩阵施加截断SVD约束，使潜在空间具有明确的线性结构和可解释的物理意义。该方法通过双重优化目标——重构精度与任务相关性（分类/建模）——来自动学习最优的粗糙度描述符，避免了人工特征工程的主观性。

【实验结果 / Results】

实验表明，RRAEs提取的SVD潜在模式在表面粗糙度重构任务上具有高精度，同时能够有效区分不同胶带类型并预测接触程度演化。相较于传统统计粗糙度参数（如Ra、Rq等），所发现的描述符与热塑性分子扩散和层间固结过程的物理机制具有更强的关联性，提升了工艺控制和建模的准确性。

【应用价值 / Applications】

该研究为复合材料制造过程中的在线质量监控和工艺优化提供了新工具，可应用于热塑性复合材料自动铺放（AFP）或热压罐成型等工艺中的胶带筛选与工艺参数预测。所提出的RRAE框架具有通用性，可扩展至其他需要物理可解释降维的粗糙表面表征场景，如摩擦学、密封工程或增材制造表面质量控制。
