---
title: "In-Context Compositional Q-Learning for Offline Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.24067"
published: "2026-03-19"
summarized: "2026-03-19T14:07:10.224456"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了上下文组合式Q学习（ICQL），一种针对离线强化学习的新框架，通过将Q学习重新表述为上下文推断问题来解决传统全局Q函数难以捕捉多子任务组合结构的问题。ICQL利用线性Transformer从检索到的转移数据中自适应地推断局部Q函数，无需显式的子任务标签。理论分析证明了在局部Q函数线性可近似和权重推断准确两个假设下，ICQL能够实现有界的Q函数近似误差并支持近最优策略提取。实验表明，ICQL在Kitchen任务上性能提升高达16.4%，在MuJoCo和Adroit任务上分别提升8.8%和6.3%。

【方法概述 / Method】
ICQL将Q学习框架转化为上下文推断问题，使用线性Transformer架构根据检索到的历史转移上下文自适应地计算局部Q函数的权重。该方法通过注意力机制动态组合相关经验，避免了传统方法中单一全局Q函数的局限性，实现了对复杂任务中不同子结构的灵活建模。

【实验结果 / Results】
ICQL在多个标准离线强化学习基准上取得显著性能提升：在Franka Kitchen多任务组合环境中最高提升16.4%，在MuJoCo连续控制任务上平均提升8.8%，在Adroit机器人操作任务上提升6.3%。这些结果表明ICQL在具有组合结构的真实机器人任务中尤其有效。

【应用价值 / Applications】
ICQL适用于需要处理复杂多阶段任务的离线强化学习场景，如机器人操作、多步骤决策系统等，特别是在无法与环境交互、只能利用历史数据的实际应用中。该方法为构建更鲁棒、可迁移的决策系统提供了新思路，有助于推动离线强化学习在真实世界机器人控制和自动化系统中的部署。
