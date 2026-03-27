---
title: "KARMA: Knowledge-Action Regularized Multimodal Alignment for Personalized Search at Taobao"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22779"
published: "2026-03-27"
summarized: "2026-03-28T07:12:13.714906"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文揭示了在个性化搜索任务中直接微调大语言模型（LLMs）时存在的"知识-行动鸿沟"问题：判别性目标会导致语义崩溃（如注意力"汇聚"现象），严重损害LLM的泛化能力。为此，作者提出了KARMA框架，通过将语义重建作为训练专用正则化器，在优化检索用的下一兴趣嵌入（Action）的同时强制保持语义可解码性（Knowledge）。该框架在淘宝搜索系统上线后，在排序、预排序和召回阶段均取得显著提升，线上Item Click增长0.5%。

【方法概述 / Method】

KARMA采用双目标优化策略：（i）历史条件化的语义生成，将优化锚定到LLM原生下一词分布；（ii）嵌入条件化的语义重建，约束兴趣嵌入保持语义可恢复性。该方法将语义重建仅用于训练阶段作为正则化，推理时保持低开销，实现了知识保持与行动对齐的统一。

【实验结果 / Results】

消融实验显示语义可解码性带来最高+22.5%的HR@200提升；完整KARMA系统在排序阶段实现+0.25 CTR AUC，预排序阶段+1.86 HR，召回阶段+2.51 HR。注意力汇聚分析验证了KARMA有效缓解语义崩溃问题。线上A/B测试表明KARMA在排序阶段部署时带来+0.5% Item Click增长。

【应用价值 / Applications】

KARMA为工业级个性化搜索系统提供了一种高效融合LLM语义知识与实际业务目标的解决方案，特别适用于需要同时保证推荐准确性和语义泛化能力的电商平台。其低推理开销特性使其易于大规模在线部署，可推广至商品搜索、内容推荐等需要深度语义理解的用户兴趣建模场景。
