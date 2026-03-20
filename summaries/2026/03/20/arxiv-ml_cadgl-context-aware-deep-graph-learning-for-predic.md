---
title: "CADGL: Context-Aware Deep Graph Learning for Predicting Drug-Drug Interactions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2403.17210"
published: "2026-03-20"
summarized: "2026-03-20T14:04:26.782684"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CADGL（Context-Aware Deep Graph Learning），一种用于预测药物-药物相互作用（DDI）的新型深度学习框架。该研究针对现有DDI预测模型在极端情况下的泛化能力、鲁棒特征提取和实际应用方面的挑战，通过定制的变分图自编码器（VGAE）从局部邻域和分子上下文两个视角提取关键结构和理化信息。CADGL在预测具有临床价值的新型DDI方面超越了现有最先进模型，并通过严格的案例研究进行了验证。

【方法概述 / Method】
CADGL基于定制的变分图自编码器架构，包含图编码器、潜在信息编码器和MLP解码器三个组件。该方法采用两个上下文预处理器，分别从局部邻域（图结构信息）和分子上下文（异构图中的理化特征）两个不同角度进行特征提取，以捕获全面的药物表征信息。

【实验结果 / Results】
CADGL在DDI预测任务上优于其他最先进模型，展现出更强的泛化能力和鲁棒性。该模型在预测新型、临床有价值的DDI方面表现卓越，并通过严格的案例研究证实了其实际有效性，能够识别具有潜在临床应用前景的药物相互作用。

【应用价值 / Applications】
该研究可应用于药物发现和开发流程，帮助识别有利的药物组合以创造创新药物。CADGL能够辅助临床医生评估药物联用的安全性与有效性，为精准医疗和个性化用药提供决策支持，同时降低药物不良反应的风险。
