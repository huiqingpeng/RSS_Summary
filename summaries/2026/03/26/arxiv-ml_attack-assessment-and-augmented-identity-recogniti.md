---
title: "Attack Assessment and Augmented Identity Recognition for Human Skeleton Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24232"
published: "2026-03-26"
summarized: "2026-03-27T07:22:15.066318"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了Attack-AAIRS框架，用于评估和提升基于LiDAR骨骼数据的人员识别模型（HCN-ID）对抗对抗攻击的鲁棒性。该框架利用小规模真实数据集和GAN生成的合成数据集，学习对抗攻击样本的分布来扩充训练数据，从而实现模型的"免疫接种"。实验表明，该方法能有效防御FGSM、PGD等多种未见过的攻击，同时保持原始模型在真实数据上的测试准确率。

【方法概述 / Method】

Attack-AAIRS通过GAN学习能够利用HCN-ID模型弱点的对抗攻击样本分布，而非局限于对有限真实训练样本的扰动。生成的攻击样本用于数据增强训练，使模型在面对多种对抗攻击时具有更强的鲁棒性。该方法采用十折交叉验证评估模型对未见攻击的防御能力。

【实验结果 / Results】

Attack-AAIRS显著提升了对FGSM、PGD、加性高斯噪声、MI-FGSM和BIM等多种未见对抗攻击的鲁棒性。合成数据质量评分显示生成的攻击样本与AAIRS原始良性合成样本质量相当。更重要的是，经免疫接种的模型在真实数据上的最终测试准确率与原始模型保持一致，实现了鲁棒性提升而不牺牲正常性能。

【应用价值 / Applications】

该研究适用于基于LiDAR骨骼数据的人员识别安全系统，特别是在训练数据有限的安全敏感场景中。Attack-AAIRS为小型数据集训练的安全关键型机器学习模型提供了一种实用的对抗防御方案，可在安防监控、身份认证等领域应用，帮助解决数据采集成本高与模型安全性之间的平衡问题。
