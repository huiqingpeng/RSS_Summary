---
title: "Non-Adversarial Imitation Learning Provably Free of Compounding Errors: The Role of Bellman Constraints"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22713"
published: "2026-03-25"
summarized: "2026-03-26T07:16:34.161791"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文重新审视了非对抗性Q值模仿学习方法IQ-Learn，理论上证明其本质上退化为行为克隆（BC），仍受累积误差困扰。为此，作者提出了一种新的原始-对偶框架Dual Q-DM，通过引入贝尔曼约束将高Q值从已访问状态传播到未访问状态，实现了对专家策略的泛化。这是首个理论上保证消除累积误差的非对抗性模仿学习方法。

【方法概述 / Method】

论文采用理论分析与算法设计相结合的方法：首先通过严格的数学证明揭示IQ-Learn的局限性——在所有未被演示覆盖的状态上均匀抑制Q值；然后基于分布匹配的原始-对偶框架，设计Dual Q-DM方法，核心机制是利用贝尔曼约束实现Q值的动态传播与泛化。

【实验结果 / Results】

理论证明Dual Q-DM等价于对抗性模仿学习（AIL），能够恢复演示之外的专家动作，从而消除累积误差；实验结果进一步验证了理论分析的正确性，表明Dual Q-DM在避免对抗训练不稳定性的同时，达到了与AIL相当的性能，且显著优于IQ-Learn和行为克隆。

【应用价值 / Applications】

该研究为模仿学习提供了兼具理论保证和训练稳定性的新范式，适用于机器人控制、自动驾驶等需要高样本效率和稳定训练的长时序决策任务，解决了传统对抗性方法训练不稳定与非对抗性方法累积误差的两难问题。
