---
title: "Semantic Interaction Information mediates compositional generalization in latent space"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27134"
published: "2026-03-31"
summarized: "2026-04-01T07:21:52.269157"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究探讨了即使所有相关变量已知时，组合泛化仍存在障碍的问题。作者提出将组合泛化建模为具有参数化交互的潜在变量变分推断问题，并开发了"Cognitive Gridworld"环境——一种静止的部分可观察马尔可夫决策过程（POMDP），其中观察由多个潜在变量联合生成，但仅对单一目标变量提供反馈。研究定义了语义交互信息（SII）来度量潜在变量交互对任务性能的贡献，并提出了表示分类链（RCCs）架构来解决交互学习与推断之间的循环依赖问题，最终实现了对新变量组合的泛化。

【方法概述 / Method】

论文采用变分推断框架将组合泛化形式化为潜在变量的推断问题，并设计了Cognitive Gridworld作为测试平台，其中多个潜在变量共同生成观察但仅反馈单一目标。作者提出语义交互信息（SII）作为量化潜在变量交互贡献的指标，并开发了Representation Classification Chains（RCCs）——一种JEPA风格的架构，通过强化学习学习变量推断、通过自监督学习学习变量嵌入，从而解耦这两个过程。

【实验结果 / Results】

使用SII分析表明，该指标能够解释Echo State网络与全训练循环神经网络（RNN）之间的准确率差距。研究还发现了一种理论预测的失效模式：模型的置信度与准确率解耦。在更具挑战性的设置中，RCCs架构成功解决了交互学习与准确推断之间的循环依赖问题，并实现了对新组合变量的组合泛化，证明了该架构在持续元学习中的有效性。

【应用价值 / Applications】

该研究为评估目标导向的通用智能体提供了基础测试环境，对开发具有组合泛化能力的AI系统具有重要指导意义。RCCs架构可应用于需要处理多变量交互的复杂决策任务，如机器人控制、智能推荐和持续学习系统。此外，SII指标为诊断和改进神经网络的泛化能力提供了可解释性工具，有助于构建更可靠的机器学习系统。
