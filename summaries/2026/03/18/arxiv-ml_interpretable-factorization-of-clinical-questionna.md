---
title: "Interpretable factorization of clinical questionnaires to identify latent factors of psychopathology"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2312.07762"
published: "2026-03-18"
summarized: "2026-03-18T16:15:58.884962"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为ICQF（可解释性约束问卷因子分解）的非负矩阵分解方法，专门用于解决精神病学问卷数据分析中的因子可解释性差、混杂变量干扰以及缺失数据等问题。该方法通过针对性正则化促进因子可解释性和解的稳定性，并提供了具有理论收敛保证的优化程序以及自动检测潜在维度的方法。在两个独立的真实数据集（Healthy Brain Network和Adolescent Brain Cognitive Development研究）上的验证表明，ICQF在保持诊断信息的同时显著提升了领域专家定义的可解释性，尤其在较小样本量时优于竞争方法。

【方法概述 / Method】
ICQF是一种专为问卷数据设计的非负矩阵分解方法，通过引入 tailored 正则化项来增强因子可解释性和解的稳定性。该方法包含一个具有理论收敛保证的优化算法，以及一个自动确定潜在因子维度数量的程序，无需手动调参。

【实验结果 / Results】
使用真实感合成数据验证表明，ICQF能够准确检测潜在维度。在两个独立的真实数据集应用中，ICQF在领域专家评估的可解释性方面表现优异，同时保留了跨多种精神障碍的诊断信息；特别地，在样本量较小的情况下，ICQF显著优于现有竞争方法。

【应用价值 / Applications】
ICQF可广泛应用于精神病学研究和临床实践中基于问卷数据的心理病理学评估，帮助研究人员和临床医生从复杂的行为测量中提取可解释、稳定的潜在因子结构。该方法对数据量有限的临床场景尤为适用，有望改善精神障碍的分类、诊断和理解，并促进精准精神医学的发展。Python实现已开源，便于实际部署和进一步研究。
