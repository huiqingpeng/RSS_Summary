---
title: "Interpretable AI-Assisted Early Reliability Prediction for a Two-Parameter Parallel Root-Finding Scheme"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16980"
published: "2026-03-19"
summarized: "2026-03-19T13:08:09.072496"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种可解释的AI辅助可靠性诊断框架，用于参数化求根算法。该框架基于kNN-LLE代理稳定性分析和多时间范围早期预测，通过最大Lyapunov指数（LLE）估计器的平滑代理轮廓构建基于收缩性的可靠性评分，并利用机器学习模型从迭代动力学的早期片段预测可靠性分数。实验表明，该框架仅需少量迭代即可实现可靠预测（R²从0.48提升至0.96），且推理成本极低。

【方法概述 / Method】
论文采用k近邻局部线性嵌入（kNN-LLE）方法构建LLE估计器的代理稳定性轮廓，结合平滑处理提取有限时间收敛特征；随后训练机器学习模型，从代理轮廓的早期时间序列片段预测可靠性评分，实现多时间范围的早期诊断。

【实验结果 / Results】
在双参数并行求根算法上的实验显示：预测 horizon T=1 时 R²=0.48，T=3 时提升至0.67，在稳定性轮廓特征最小尺度前超过0.89，更大horizon时达到0.96，平均绝对误差约0.03；单次推理耗时仅微秒级。

【应用价值 / Applications】
该框架可为数值求解器提供实时、可解释的早期稳定性诊断，支持求解过程中的动态决策（如继续迭代、重启或调整参数），特别适用于需要高可靠性保证的科学计算和工程优化场景，且计算开销可忽略不计。
