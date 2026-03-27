---
title: "Not All Pretraining are Created Equal: Threshold Tuning and Class Weighting for Imbalanced Polarization Tasks in Low-Resource Settings"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23534"
published: "2026-03-27"
summarized: "2026-03-28T07:13:19.088649"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文介绍了作者参加SemEval-2025极化共享任务的系统提交，针对社交媒体文本中的极化检测与分类问题。研究开发了基于Transformer的英语和斯瓦希里语系统，涵盖二元极化检测、多标签目标类型分类和多标签表现形式识别三个子任务。最佳配置mDeBERTa-v3-base在验证集上达到0.8032的macro-F1分数，但隐式极化、语码转换以及区分激烈政治话语与真正极化仍是持续挑战。

【方法概述 / Method】
作者采用多语言及非洲语言专用预训练模型（mDeBERTa-v3-base、SwahBERT、AfriBERTa-large），结合类别加权损失函数处理严重类别不平衡问题。此外，使用迭代分层数据划分策略，并对多标签任务实施逐标签阈值调优，以优化分类决策边界。

【实验结果 / Results】
mDeBERTa-v3-base在二元极化检测验证集上取得0.8032的macro-F1最佳性能；多标签任务表现相对有限，最高达到0.556 macro-F1。实验显示不同预训练模型效果差异显著，且类别不平衡对模型性能影响突出。

【应用价值 / Applications】
该研究为低资源环境下的社交媒体极化内容监测提供了可落地的技术方案，特别适用于非洲语言（如斯瓦希里语）的在线内容审核。研究成果可助力社交平台识别有害极化言论，同时为多语言、不平衡分类任务的方法设计提供参考。
