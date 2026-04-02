---
title: "Towards Initialization-dependent and Non-vacuous Generalization Bounds for Overparameterized Shallow Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00505"
published: "2026-04-02"
summarized: "2026-04-03T07:22:02.225479"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了过参数化浅层神经网络的泛化界问题，提出了一种完全依赖于初始化的复杂度边界分析方法。现有基于初始化的复杂度分析受限于初始化矩阵的谱范数，该范数随网络宽度呈平方根增长，因此无法有效应用于过参数化模型。作者首次建立了对宽度仅呈对数依赖的完全初始化依赖泛化界，并证明了该边界在常数因子意义下是紧的，能够为过参数化网络提供非空洞（non-vacuous）的泛化保证。

【方法概述 / Method】

作者引入了一种新的"peeling"技术来处理初始化依赖约束带来的挑战，通过路径范数（path-norm）来度量参数与初始化之间的距离。该方法适用于具有一般Lipschitz激活函数的浅层神经网络，避免了传统方法对谱范数的依赖，从而实现了对网络宽度的对数级依赖。

【实验结果 / Results】

理论分析表明，所提出的泛化界在常数因子意义下是紧的（tight up to a constant factor）。实证比较显示，该分析方法能够为过参数化网络提供非空洞的泛化边界，即得到的泛化误差上界小于1（对于二分类问题而言是有意义的非平凡结果），验证了理论结果的实际有效性。

【应用价值 / Applications】

该研究为理解和解释过参数化神经网络的"良性过拟合"现象提供了新的理论工具，特别是在深度学习模型参数量远超训练样本数的场景下。研究成果可用于指导神经网络初始化策略的设计，并为模型选择、正则化方法以及泛化性能的理论分析提供更紧致的边界估计，对提升深度学习模型的可解释性和可靠性具有重要价值。
