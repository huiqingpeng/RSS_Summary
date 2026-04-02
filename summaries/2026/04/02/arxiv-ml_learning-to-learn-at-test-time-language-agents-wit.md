---
title: "Learning to Learn-at-Test-Time: Language Agents with Learnable Adaptation Policies"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00830"
published: "2026-04-02"
summarized: "2026-04-03T07:25:33.180199"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了Meta-TTL框架，用于学习测试时学习（TTL）中的自适应策略，而非依赖人工设计的固定规则。该框架将自适应策略的发现形式化为双层优化问题：内循环执行标准TTL过程评估候选策略的效果，外循环通过进化搜索在多样化训练任务上迭代优化策略。实验表明，Meta-TTL在Jericho和WebArena-Lite基准的分布内和分布外场景均显著优于手工设计的基线，且学习的策略具有跨任务泛化能力。

【方法概述 / Method】

Meta-TTL采用双层优化架构：内循环中，语言智能体基于候选自适应策略在测试时与环境交互，通过多轮episode积累经验并更新行为策略；外循环则根据智能体在任务上的最终表现，使用进化搜索算法（如CMA-ES）优化自适应策略的参数。该框架将自适应策略本身视为可学习的组件，使其能够从任务环境中自动发现有效的错误修正和知识迁移机制。

【实验结果 / Results】

在文本游戏环境Jericho和网页智能体基准WebArena-Lite上，Meta-TTL相比最优手工设计基线（如Reflexion、ExpeL）在分布内任务上提升显著，且在分布外任务上展现出更强的泛化性。实验覆盖多种元智能体骨干模型（如GPT-4、Claude等），结果一致表明学习的自适应策略能够编码可迁移的元认知策略，如选择性记忆检索和失败模式识别。

【应用价值 / Applications】

该研究为构建更具自主适应能力的语言智能体提供了新范式，特别适用于需要长期交互和持续学习的场景，如复杂任务自动化、交互式决策系统和个性化助手。通过自动化自适应策略的设计，降低了人工调优成本，使智能体能够根据具体环境特性动态调整学习行为，提升了在开放世界任务中的实用性和鲁棒性。
