---
title: "DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards via Dynamic Jensen-Shannon Replay"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16157"
published: "2026-03-18"
summarized: "2026-03-18T15:41:13.930301"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出Dynamic Jensen-Shannon Replay (DyJR)，一种用于强化学习中的经验回放正则化框架，旨在解决GRPO等在线策略算法的样本效率低下和模式崩溃问题。DyJR通过动态参考分布保留历史数据的多样性而非单纯强化准确性，包含时间敏感的动态缓冲区（FIFO+自适应大小）和Jensen-Shannon散度正则化两项创新。实验表明，DyJR在数学推理和Text-to-SQL任务上显著优于GRPO、RLEP和Ex-GRPO等基线，同时保持与原始GRPO相当的训练效率。

【方法概述 / Method】
DyJR采用双组件架构：（1）时间敏感动态缓冲区，利用FIFO机制和自适应大小策略仅保留时间上邻近的样本，使缓冲区与模型演化同步；（2）Jensen-Shannon散度正则化，用分布约束替代直接梯度更新，防止多样性崩溃。该方法将历史rollouts构建为动态参考分布，通过正则化而非直接更新来利用过往经验。

【实验结果 / Results】
DyJR在数学推理和Text-to-SQL基准测试中显著超越GRPO及RLEP、Ex-GRPO等对比方法，同时保持与原始GRPO相近的训练效率。从Rank-k token概率演化分析显示，DyJR有效提升了生成多样性，并减轻了对Rank-1最高概率token的过度依赖，揭示了各子模块对训练动态的具体影响机制。

【应用价值 / Applications】
该研究适用于大语言模型推理能力提升场景，特别是需要平衡探索与利用的复杂推理任务（如数学问题求解、代码生成和Text-to-SQL转换）。DyJR为强化学习训练中的样本高效利用和多样性保持提供了实用方案，有助于缓解在线策略学习中的模式崩溃问题，提升模型泛化能力和鲁棒性。
