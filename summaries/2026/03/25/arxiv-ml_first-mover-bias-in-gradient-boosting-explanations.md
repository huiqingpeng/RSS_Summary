---
title: "First-Mover Bias in Gradient Boosting Explanations: Mechanism, Detection, and Resolution"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22346"
published: "2026-03-25"
summarized: "2026-03-26T07:13:04.918958"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究首次系统性地识别并实证分析了梯度提升中的"先发偏差"（first-mover bias）机制——这是一种由顺序残差拟合导致的路径依赖性特征重要性集中现象，是SHAP特征排序在多共线性条件下不稳定性的具体成因。研究发现，当相关特征竞争早期分裂时，梯度提升会为首先被选中的特征创造自我强化的优势，使SHAP重要性集中于任意单一特征而非分散到相关特征组。作者提出DASH（Diversified Aggregation of SHAP）方法和简单的种子平均策略（Stochastic Retrain），通过打破模型间的顺序依赖链来恢复解释稳定性，并开发了无需真实标签即可检测先发偏差的诊断工具FSI和IS Plot。

【方法概述 / Method】

论文核心方法DASH通过训练多个独立的梯度提升模型（打破顺序依赖链），聚合其SHAP解释以获得稳定的特征重要性估计；同时提出两种诊断工具——特征稳定性指数（FSI）衡量特征重要性跨模型的一致性，重要性-稳定性图（IS Plot）可视化稳定性与重要性的权衡关系。对比方法包括单一大型模型（Large Single Model）、单最佳工作流（single-best workflow）以及简单的随机重训练平均（Stochastic Retrain）。

【实验结果 / Results】

在高相关性条件下（rho=0.9），DASH和Stochastic Retrain均达到0.977的稳定性，显著优于单最佳工作流（0.958）和大型单一模型（0.938）；在乳腺癌数据集上，DASH将稳定性从0.32提升至0.93（+0.61）。关键发现是：模型独立性足以在线性条件下解决先发偏差，在非线性数据生成过程中仍是最有效的缓解策略；而简单地扩大单一模型规模会放大而非缓解该偏差效应。

【应用价值 / Applications】

该研究为机器学习可解释性实践提供了重要的质量保障工具：FSI和IS Plot使从业者能够在依据特征排名采取行动之前，无需 ground truth 即可审计解释可靠性，特别适用于医疗诊断、金融风控等高 stakes 场景中基于特征重要性的决策。DASH方法可直接集成到现有的梯度提升工作流中，为处理高维共线性数据的模型解释提供标准化解决方案。
