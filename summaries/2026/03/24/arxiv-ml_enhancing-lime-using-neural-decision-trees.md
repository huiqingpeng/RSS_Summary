---
title: "Enhancing LIME using Neural Decision Trees"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20919"
published: "2026-03-24"
summarized: "2026-03-25T07:16:04.816517"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为NDT-LIME的新型可解释机器学习方法，通过将神经决策树（Neural Decision Trees, NDTs）作为替代模型（surrogate model）集成到LIME框架中，以解决传统LIME变体中线性回归和决策树等替代模型难以准确捕捉复杂非线性决策边界的问题。该方法利用NDT的结构化层次特性，旨在提供更准确、更有意义的局部解释。在多个表格数据基准数据集上的评估表明，NDT-LIME在解释保真度（explanation fidelity）方面相比传统LIME替代模型有持续提升。

【方法概述 / Method】
本文的核心方法是将神经决策树（NDTs）作为替代模型嵌入LIME框架，替代传统的线性回归或标准决策树。NDTs结合了神经网络的表达能力与决策树的结构化可解释性，能够更好地逼近复杂黑盒模型的局部非线性行为，从而在保持解释性的同时提高替代模型的拟合精度。

【实验结果 / Results】
作者在多个表格数据基准数据集上评估了NDT-LIME的有效性，实验结果表明该方法在解释保真度方面 consistently 优于传统LIME替代模型。虽然摘要中未提供具体的量化指标，但"consistent improvements"表明该改进在不同数据集上具有稳健性。

【应用价值 / Applications】
该研究主要适用于需要高透明度的表格数据场景，如金融风控（信贷审批、欺诈检测）、医疗诊断辅助、保险理赔决策等领域，帮助领域专家理解复杂黑盒模型的局部预测依据，在满足监管合规要求的同时提升模型可信度。此外，该方法为模型调试和偏见检测提供了更可靠的工具。
