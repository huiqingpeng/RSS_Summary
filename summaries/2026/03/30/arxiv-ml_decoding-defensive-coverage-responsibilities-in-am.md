---
title: "Decoding Defensive Coverage Responsibilities in American Football Using Factorized Attention Based Transformer Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25901"
published: "2026-03-30"
summarized: "2026-03-31T07:19:34.731259"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种基于因子化注意力机制的Transformer模型，用于预测NFL橄榄球比赛中每位防守队员的盯人任务、攻防对位关系以及传球目标防守者。该模型通过分离时间维度和球员维度的注意力机制，实现了从开球前到传球到达期间的逐帧动态预测，在各项任务上均达到约89%以上的准确率。研究还衍生出"伪装率"和"双人包夹率"等新指标，为赛事转播和球队战术分析提供了新工具。

【方法概述 / Method】
论文采用因子化注意力Transformer架构处理多智能体追踪数据，将时间与球员两个维度的注意力计算解耦，分别建模球员运动模式和球员间交互关系。模型在随机截断的轨迹数据上训练，能够基于不完整观测进行帧级别的覆盖责任预测。

【实验结果 / Results】
模型在覆盖任务分配、攻防对位预测和传球目标防守者识别三项任务上均实现约89%以上的准确率，实际真实准确率可能更高（因标注数据存在固有歧义）。逐帧预测结果成功捕捉了防守责任从开球前到传球到达的动态演变过程。

【应用价值 / Applications】
该研究可应用于电视转播中的实时战术解说与数据可视化，提升观众观赛体验；同时为球队提供可操作的战术策略开发工具和球员评估指标（如识别防守伪装能力和包夹协作效率），辅助教练组制定针对性训练计划和比赛策略。
