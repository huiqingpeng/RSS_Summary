---
title: "Interpretable Prostate Cancer Detection using a Small Cohort of MRI Images"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18460"
published: "2026-03-20"
summarized: "2026-03-20T15:09:16.987792"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究开发了一种可解释的自动化前列腺癌检测框架，仅使用162张T2加权MRI图像（102例癌症，60例正常），通过迁移学习和数据增强解决数据稀缺问题。研究全面比较了Vision Transformers（ViT、Swin）、CNN（ResNet18）和经典方法（逻辑回归、SVM、HOG+SVM），发现迁移学习的ResNet18以仅1100万参数达到最佳性能（准确率90.9%，敏感度95.2%，AUC 0.905），而HOG+SVM也取得相当效果（AUC 0.917）。与依赖双参数MRI和大样本量的现有方法不同，本研究仅用T2加权图像即达到竞争性表现，在22例读片研究中AI模型敏感度（95.2%）显著高于五名放射科医生的平均水平（67.5%）。

【方法概述 / Method】
研究采用多种深度学习架构（ViT、Swin Transformer、ResNet18）与传统机器学习方法（逻辑回归、SVM、HOG+SVM）进行对比实验，利用ImageNet预训练权重进行迁移学习，并结合数据增强技术应对小样本限制。通过Grad-CAM等技术实现模型可解释性，以可视化方式呈现模型关注区域。

【实验结果 / Results】
迁移学习的ResNet18表现最优，准确率达90.9%，敏感度95.2%，AUC为0.905，且参数量仅1100万；相比之下，Vision Transformers尽管复杂度更高，性能却较低。令人意外的是，传统HOG+SVM方法也取得AUC 0.917的竞争力结果。在22例读片研究中，AI模型敏感度（95.2%）远超五名放射科医生的平均敏感度（67.5%，Fleiss Kappa=0.524）。

【应用价值 / Applications】
该研究为资源有限场景下的前列腺癌筛查提供了实用解决方案，仅需T2加权MRI即可实现高性能检测，避免了DWI序列采集的复杂性和成本。AI辅助诊断系统有望减少漏诊率、提升诊断一致性，特别适用于基层医疗机构和早期筛查项目，且模型可解释性有助于增强临床医生对AI决策的信任。代码和数据公开可用，便于后续研究和临床转化。
