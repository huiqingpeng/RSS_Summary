---
title: "SymCircuit: Bayesian Structure Inference for Tractable Probabilistic Circuits via Entropy-Regularized Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20392"
published: "2026-03-24"
summarized: "2026-03-25T07:08:44.399107"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出SymCircuit，一种基于熵正则化强化学习的概率电路（PC）结构学习方法，以解决传统贪婪算法在结构学习中做出不可逆局部最优决策的问题。该方法将强化学习建模为推断框架，证明最优策略是温度化的贝叶斯后验，当正则化温度与数据集大小成反比时可恢复精确后验。SymCircuit通过语法约束的自回归Transformer（SymFormer）实现策略，并引入选项级REINFORCE算法提升样本效率，在NLTCS数据集上缩小了与LearnSPN之间93%的性能差距。

【方法概述 / Method】

SymCircuit采用熵正则化强化学习框架替代贪婪搜索，将PC结构学习建模为序列生成问题。策略网络SymFormer是一种语法约束的自回归Transformer，通过树相对自注意力机制确保每一步生成有效的电路结构。训练时使用选项级REINFORCE，仅对结构决策而非所有token进行梯度更新，从而提升信号噪声比和样本效率。

【实验结果 / Results】

在NLTCS数据集上，SymCircuit相比基线方法实现了超过10倍的样本效率提升，并缩小了与经典LearnSPN方法之间93%的性能差距。初步实验在69维的Plants数据集上展示了方法的可扩展性。三层不确定性分解（结构层面通过模型平均、参数层面通过delta方法、叶节点层面通过共轭Dirichlet-Categorical传播）有效量化了不同来源的不确定性。

【应用价值 / Applications】

该研究为高维概率建模提供了一种可扩展的贝叶斯结构学习方法，适用于需要精确概率推断的场景，如医疗诊断、自然语言处理中的语言建模以及复杂系统的风险评估。SymCircuit的可解释电路结构和不确定性量化能力使其特别适合安全关键领域的决策支持系统。
