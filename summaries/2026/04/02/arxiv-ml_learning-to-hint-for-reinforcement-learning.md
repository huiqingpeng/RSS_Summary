---
title: "Learning to Hint for Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00698"
published: "2026-04-02"
summarized: "2026-04-03T07:23:56.851143"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了Hint Learning for Reinforcement Learning (HiLL)框架，旨在解决GRPO中"优势崩溃"问题——当所有rollout获得相同奖励时，相对优势为零导致无法学习。HiLL通过联合训练hinter策略和reasoner策略，使hinter能够根据reasoner的实时错误生成自适应提示，并引入"提示依赖性"指标和迁移加权奖励，确保提示不仅能恢复学习信号，还能有效迁移到无提示测试场景。实验表明HiLL在多个基准上持续优于GRPO和现有基于提示的基线方法。

【方法概述 / Method】

HiLL采用双策略联合训练架构：hinter策略接收困难问题和reasoner的错误rollout作为输入，在线生成自适应提示；reasoner策略则在提示条件下进行推理。核心创新在于引入"hint reliance"度量（衡量正确提示轨迹对提示的依赖程度），并基于此推导迁移性理论结果，设计迁移加权奖励函数来优化hinter，使其生成既能恢复GRPO学习信号、又能有效迁移到无提示场景的提示。

【实验结果 / Results】

HiLL在多个基准测试上均取得优于GRPO和固定提示基线的一致性能提升。通过自适应提示生成和迁移感知训练，HiLL有效缓解了优势崩溃问题，同时确保提示带来的改进能够迁移到实际测试时使用的无提示策略，实现了提示有效性与迁移性的统一优化。

【应用价值 / Applications】

HiLL可广泛应用于基于可验证奖励的强化学习场景，特别是数学推理、代码生成等需要逐步推理的任务，其中模型可能遇到超出当前能力的困难问题。该方法通过智能提示机制提升训练效率和最终性能，对开发更鲁棒、可扩展的大语言模型推理能力具有重要价值，同时其迁移性保证确保了提示辅助训练与实际部署的一致性。
