---
title: "Continual Learning for Food Category Classification Dataset: Enhancing Model Adaptability and Performance"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19624"
published: "2026-03-23"
summarized: "2026-03-24T07:20:23.045803"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对传统机器学习模型无法识别训练集中未出现类别的局限性，提出了一种基于文本引导的持续学习框架用于食品分类。该方法支持增量式更新，能够在不遗忘已有知识的情况下整合新类别（如让训练于西餐的模型后续学习识别印度薄饼dosa或韩国泡菜kimchi）。研究表明该设计在自适应食品识别方面具有应用潜力，尽管仍需进一步优化。

【方法概述 / Method】
论文采用持续学习（continual learning）框架，结合文本引导机制实现食品类别的增量学习；与需要从头重新训练的传统方法不同，该方案通过特定的知识保留策略避免灾难性遗忘，使模型能够动态适应新类别的加入。

【实验结果 / Results】
论文摘要中未提供具体的定量实验结果或性能指标，仅提及该方法"显示出前景"（shows promise），并指出需要进一步改进（further refinements are needed）。

【应用价值 / Applications】
该研究的主要应用场景包括饮食监测（dietary monitoring）和个性化营养规划（personalized nutrition planning），可部署于需要动态扩展食品识别能力的智能健康管理系统，支持跨文化、跨地域的食品数据库持续更新与适配。
