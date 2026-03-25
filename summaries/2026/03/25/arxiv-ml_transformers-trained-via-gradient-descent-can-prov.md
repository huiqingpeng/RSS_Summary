---
title: "Transformers Trained via Gradient Descent Can Provably Learn a Class of Teacher Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22801"
published: "2026-03-25"
summarized: "2026-03-26T07:17:20.811932"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文从理论角度揭示了Transformer模型通过梯度下降训练能够学习一类教师模型的能力。作者证明了一层简化版"仅位置"注意力Transformer可以成功恢复包括卷积层、图卷积层以及稀疏token选择模型和组稀疏线性预测器等经典统计学习模型在内的多种教师模型的所有参数块，达到最优总体损失。此外，基于训练后Transformer对教师模型的高效模仿能力，研究还证明了其在温和假设下对广泛分布外数据具有良好的泛化性能。

【方法概述 / Method】
本研究的核心方法是识别出多种学习任务共享的一个基本双线性结构，并基于此建立统一的学习保证框架。作者采用理论分析手段，针对一层具有简化"position-only"注意力机制的Transformer，严格证明其通过梯度下降训练能够收敛并精确恢复各类教师模型的参数。

【实验结果 / Results】
论文的主要理论结果表明：所分析的Transformer架构能够以最优总体损失成功学习所涵盖的教师模型类别；在分布外泛化方面，训练后的Transformer在温和假设条件下可对广泛的数据分布实现良好泛化。这些结果为理解Transformer的强表达能力提供了严格的理论保证。

【应用价值 / Applications】
该研究为理解Transformer在多样化场景和任务中的强大能力奠定了理论基础，有助于指导Transformer架构的设计和训练策略优化。研究成果可应用于需要理论保证的机器学习场景，如需要可解释性和可靠性的深度学习系统，同时为分析Transformer在分布外数据上的鲁棒性提供了理论工具。
