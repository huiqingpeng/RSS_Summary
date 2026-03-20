---
title: "Inverse classification with logistic and softmax classifiers: efficient optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2309.08945"
published: "2026-03-20"
summarized: "2026-03-20T14:03:56.860359"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了逆分类（inverse classification）问题的高效求解方法，即寻找与给定输入最接近的实例，使得分类器的预测标签按期望方式改变。作者针对两种最广泛使用的分类器——逻辑回归和softmax分类器，利用其特殊数学性质，分别推导出闭式解和极快速迭代算法，可在毫秒到约一秒内精确求解高维实例和多类别情况下的优化问题，满足交互式或实时应用需求。

【方法概述 / Method】

对于逻辑回归分类器，作者利用sigmoid函数的性质将问题转化为带约束的二次优化，推导出闭式解析解；对于softmax分类器，则设计了基于固定点迭代的快速算法，通过利用softmax的指数归一化结构实现高效收敛。两种方法均针对平方欧氏距离作为目标函数进行优化。

【实验结果 / Results】

实验表明，所提方法可在毫秒级时间内完成求解，即使对于高维输入（数千维）和多类别（数十至上百类）场景也能在约一秒内收敛到机器精度级别的精确解。相比通用的数值优化方法（如梯度下降或内点法），速度提升可达数个数量级，且保证全局最优性。

【应用价值 / Applications】

该研究可直接应用于需要实时响应的场景，如反事实解释（counterfactual explanations）的交互式生成、对抗样本的快速构造、以及模型反演攻击的高效实现。其高效性使得这些方法能够部署在实时决策系统、在线推荐平台和可解释性AI工具中，显著提升用户体验和系统安全性。
