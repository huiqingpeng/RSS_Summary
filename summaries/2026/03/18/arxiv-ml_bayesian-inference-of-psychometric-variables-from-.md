---
title: "Bayesian Inference of Psychometric Variables From Brain and Behavior in Implicit Association Tests"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16741"
published: "2026-03-18"
summarized: "2026-03-18T15:47:41.059122"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究提出了一种基于稀疏层次贝叶斯模型的方法，利用多模态神经和行为数据（以隐式联想测验IAT为数据生成引擎）推断心理健康相关的心理测量变量。该方法克服了传统D-score方法仅依赖反应时间且预测性能有限（通常低于0.7 AUC）的局限，在自杀意念相关E-IAT和精神病性症状相关PSY-IAT任务中分别达到0.73和0.76的AUC，在重度抑郁障碍亚组中更达到0.79的显著性能。

【方法概述 / Method】
研究采用稀疏层次贝叶斯模型，将D-score推广为多变量形式并引入可训练参数，专门针对IAT研究常见的小样本场景进行参数效率优化。该模型整合脑电（EEG）和行为反应时间等多模态数据，通过层次结构建模个体间变异，实现对心理健康相关症状体验的预测。

【实验结果 / Results】
在E-IAT（n=39）和PSY-IAT（n=34）两个数据集上，最佳模态配置下AUC分别达到0.73和0.76，但校正后95%置信区间较宽（±0.18），FDR校正后边缘显著（q=0.10）。限制E-IAT仅分析重度抑郁障碍参与者时，AUC提升至0.79 [0.62, 0.97]（q=0.05显著）。该方法性能与针对各任务优化的参考方法（收缩LDA和EEGNet）相当，且跨任务表现更为一致，显著优于接近随机的D-score（0.50-0.53 AUC）。

【应用价值 / Applications】
该框架有望增强基于IAT的心理健康评估，特别是针对被困感（entrapment）和精神病性症状等相关体验的检测，可潜在扩展至其他精神健康状况的客观评估工具开发。然而，其在临床应用前仍需在更大规模独立队列中进一步验证。
