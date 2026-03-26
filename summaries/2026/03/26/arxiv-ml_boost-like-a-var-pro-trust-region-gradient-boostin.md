---
title: "Boost Like a (Var)Pro: Trust-Region Gradient Boosting via Variable Projection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23658"
published: "2026-03-26"
summarized: "2026-03-27T07:16:23.786985"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了VPBoost（Variable Projection Boosting），一种针对可分离平滑近似器（如神经网络）的梯度提升算法。该方法将变量投影（Variable Projection）技术与二阶弱学习策略相结合，实现了线性权重的闭式最优解，并可解释为函数空间中的信赖域方法。理论分析证明了VPBoost在温和几何条件下收敛到稳定点，在更强假设下可达到超线性收敛速率。实验表明，VPBoost在合成数据、图像识别和科学机器学习基准上均优于基于梯度下降的 boosting 方法，并与工业级决策树 boosting 算法性能相当。

【方法概述 / Method】

VPBoost 针对具有"平滑非线性特征提取器 + 最终线性映射"结构的可分离模型，采用变量投影技术消除线性权重、降低优化维度，同时利用二阶信息（Hessian）进行弱学习器的训练。该方法将提升过程重新诠释为函数空间中的信赖域优化，每一步在信赖域约束下求解最优弱学习器，并通过变量投影获得闭式最优线性权重。

【实验结果 / Results】

在合成数据、CIFAR-10/100图像识别任务以及科学机器学习（PDE求解）基准上的综合实验表明，VPBoost 相比基于梯度下降的 boosting 方法（如 GradBoost）在评估指标上有显著提升；与工业标准的 XGBoost 决策树提升算法相比，VPBoost 使用神经网络弱学习器取得了具有竞争力的性能，同时展现了更好的平滑函数逼近能力。

【应用价值 / Applications】

VPBoost 填补了平滑参数化模型（如神经网络）在梯度提升训练方法上的空白，为需要可微、平滑预测函数的场景（如科学计算中的物理场预测、可微分模拟、端到端可微流程）提供了高效可靠的集成学习工具。其理论保证和超线性收敛特性使其特别适用于对模型可解释性和收敛稳定性要求较高的机器学习任务。
