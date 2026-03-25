---
title: "Beyond the Mean: Distribution-Aware Loss Functions for Bimodal Regression"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22328"
published: "2026-03-25"
summarized: "2026-03-26T07:11:52.179137"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对机器学习模型中预测置信度估计的挑战，提出了一种新的分布感知损失函数家族。该研究解决了当预测误差呈现双峰分布时（即同时存在高置信度和模糊预测），标准回归方法因假设单峰高斯噪声而导致的均值塌陷问题。与混合密度网络（MDNs）相比，新方法在保持优化稳定性的同时，能够恢复双峰分布，并在复杂双峰数据集上将Jensen-Shannon散度降低45%，建立了新的帕累托效率前沿。

【方法概述 / Method】
作者提出将归一化RMSE与Wasserstein距离和Cramér距离相结合，构建分布感知损失函数。该方法直接应用于标准深度回归模型，无需采用不稳定的混合模型结构，即可实现对双峰预测分布的建模。损失函数设计兼顾了单峰任务的稳定性与双峰任务的分布表达能力。

【实验结果 / Results】
通过四个阶段的实验验证，Wasserstein损失在单峰任务上达到了与MSE等标准回归损失相当的稳定性，同时在复杂双峰数据集上显著降低Jensen-Shannon散度达45%。该方法在保真度和鲁棒性两方面均严格优于MDNs，实现了预测不确定性的可靠估计。

【应用价值 / Applications】
该框架适用于需要可靠偶然不确定性（aleatoric uncertainty）估计的可信AI系统，特别是在自动驾驶、医疗诊断等安全关键领域，其中模型需要区分高置信度预测和模糊预测以支持决策。研究为构建更具可解释性和可靠性的机器学习系统提供了实用工具，有助于提升高风险应用场景下的模型可信度。
