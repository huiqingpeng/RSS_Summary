---
title: "Global Convergence of Multiplicative Updates for the Matrix Mechanism: A Collaborative Proof with Gemini 3"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19465"
published: "2026-03-23"
summarized: "2026-03-24T07:18:33.667731"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文证明了在差分隐私机器学习中出现的矩阵机制优化问题的一个开放问题：涉及Hadamard积结构的正则化核范数目标的定点迭代具有全局收敛性。作者证明了迭代公式 $v^{(k+1)} = \text{diag}((D_{v^{(k)}}^{1/2} M D_{v^{(k)}}^{1/2})^{1/2})$ 单调收敛到势函数 $J(v)$ 的唯一全局最优解，填补了Denisov等人遗留的理论空白。值得注意的是，该证明的主体工作由Gemini 3完成，本文也因此成为探讨AI辅助数学证明实践方法的案例研究。

【方法概述 / Method】

论文采用定点迭代分析技术，研究形如 $v \leftarrow \phi(v)$ 的乘法更新规则的收敛性质，其中关键步骤涉及对矩阵 $D_v^{1/2} M D_v^{1/2}$ 的平方根运算与对角元提取。证明过程中结合了单调算子理论和势函数优化框架，通过验证迭代映射的收缩性质来确立全局收敛性。

【实验结果 / Results】

论文的主要理论结果是：证明了该乘法更新迭代以单调方式收敛到唯一全局最优解；同时作为方法论探索，展示了Gemini 3能够在人类研究者的少量修正和干预下完成非平凡的数学证明任务，并记录了提示工程（prompting）的有效策略。

【应用价值 / Applications】

该成果直接应用于差分隐私机器学习中的矩阵机制优化，为设计隐私保护算法提供了理论保证；同时，本文作为AI辅助数学研究的范例，为学术界提供了与大型语言模型协作证明数学定理的实践原则和叙事参考，对数学与人工智能交叉领域具有方法论启示意义。
