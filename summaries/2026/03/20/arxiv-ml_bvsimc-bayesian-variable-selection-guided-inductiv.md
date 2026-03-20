---
title: "BVSIMC: Bayesian Variable Selection-Guided Inductive Matrix Completion for Improved and Interpretable Drug Discovery"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18957"
published: "2026-03-20"
summarized: "2026-03-20T12:17:31.724994"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了贝叶斯变量选择引导的归纳矩阵补全方法（BVSIMC），用于解决药物发现中侧信息特征高维、 noisy 且相关性差异大的问题。该方法通过学习稀疏潜在嵌入，同时提升预测准确性和可解释性。在合成数据及两个真实药物发现任务（结核分枝杆菌耐药性预测和药物重定位中的新药物-疾病关联预测）中，BVSIMC 均优于现有先进方法，并能识别出最具临床意义的侧信息特征。

【方法概述 / Method】

BVSIMC 是一种贝叶斯生成模型，将变量选择机制整合到归纳矩阵补全框架中，通过引入稀疏先验自动筛选高维侧信息特征中的相关变量。模型采用贝叶斯推断学习药物和疾病的低维潜在表示，同时实现特征选择和矩阵补全的联合优化。

【实验结果 / Results】

在模拟研究中，BVSIMC 展现出优于多种最先进基线方法的预测性能；在两个真实药物发现应用中，该方法在预测准确性上持续领先，并成功识别出与结核耐药性及药物重定位相关的关键生物标志物和化学特征。

【应用价值 / Applications】

BVSIMC 可直接应用于基于侧信息的药物-疾病关联预测任务，辅助抗结核药物开发和计算药物重定位研究。其可解释性输出有助于研究人员理解驱动预测的关键分子特征和基因组因素，加速靶点发现和临床决策支持。
