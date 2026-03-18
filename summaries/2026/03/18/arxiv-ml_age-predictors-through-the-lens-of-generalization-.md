---
title: "Age Predictors Through the Lens of Generalization, Bias Mitigation, and Interpretability: Reflections on Causal Implications"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16377"
published: "2026-03-18"
summarized: "2026-03-18T15:43:43.668313"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究探讨了年龄预测模型在分布外（OOD）泛化方面的挑战，指出种族、性别或组织等外生属性会导致模型失效。论文通过对抗表示学习构建可解释的神经网络，学习对这些属性的不变表示，以同时实现OOD泛化、偏差缓解和公平性。利用公开的小鼠转录组数据集，作者验证了该模型与Elamipretide药物效应研究的一致性，并讨论了从纯预测模型推导因果解释的局限性。

【方法概述 / Method】
论文采用基于对抗表示学习的可解释神经网络框架，通过显式约束学习对混杂因素（如种族、性别、组织）不变的潜在表示。该方法将偏差缓解、因果推断中的混杂控制与公平性目标统一在理论框架下，并与传统机器学习方法进行对比分析。

【实验结果 / Results】
在公开小鼠转录组数据集上的实验表明，该对抗表示学习模型能有效分离年龄相关信号与混杂因素，实现更稳健的OOD泛化。模型预测结果与已发表的Elamipretide对小鼠骨骼肌和心肌效应研究一致，验证了其在生物学意义上的可靠性。

【应用价值 / Applications】
该研究为生物医学年龄预测提供了一种兼顾泛化性、公平性和可解释性的建模范式，特别适用于跨人群、跨组织的衰老研究和药物效应评估。同时，论文对预测模型因果解释局限性的讨论为后续研究提供了重要的方法论警示。
