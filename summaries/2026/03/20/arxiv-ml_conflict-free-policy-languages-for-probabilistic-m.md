---
title: "Conflict-Free Policy Languages for Probabilistic ML Predicates: A Framework and Case Study with the Semantic Router DSL"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18174"
published: "2026-03-20"
summarized: "2026-03-20T12:08:41.337737"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对基于概率性机器学习信号（如嵌入相似度、领域分类器）的策略语言中的冲突检测问题，提出了一个三层可判定性层次结构： crisp 冲突可通过 SAT 判定，嵌入冲突可归约为球冠相交问题，而分类器冲突在没有分布知识时不可判定。作者证明在实际占主导的嵌入场景中，用温度缩放 softmax 替代独立阈值机制可将嵌入空间划分为互斥的 Voronoi 区域，从而消除共触发冲突，且无需重新训练模型。该检测与预防机制已在生产级 LLM 推理路由语言 Semantic Router DSL 中实现。

【方法概述 / Method】

论文通过理论分析建立了冲突检测的可判定性层次框架，并针对嵌入相似度这一核心场景设计了基于温度缩放 softmax 的空间划分方法，将传统的独立阈值判断转化为互斥的区域决策。该方案在 Semantic Router DSL 中实现了编译时冲突检测和运行时冲突预防的双重机制。

【实验结果 / Results】

（注：论文摘要未提供具体量化实验结果，主要贡献为理论框架与机制设计）

作者展示了所提方法在 Semantic Router DSL 中的成功部署，证明该方案能够有效检测和预防基于嵌入相似度的路由冲突，实现无冲突的策略执行。理论分析表明嵌入冲突的可判定性可归约为计算几何中的球冠相交问题，而分类器冲突在缺乏分布假设时不可判定。

【应用价值 / Applications】

该研究直接应用于 LLM 推理路由系统，可确保语义路由器将查询正确导向目标模型，避免多个路由规则同时触发导致的错误路由。其思想同样适用于基于语义的角色访问控制（RBAC）和 API 网关策略场景，为日益普及的 ML 驱动决策系统提供了可靠的冲突安全保障机制。
