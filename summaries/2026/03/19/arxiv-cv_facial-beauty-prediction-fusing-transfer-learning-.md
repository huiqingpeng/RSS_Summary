---
title: "Facial beauty prediction fusing transfer learning and broad learning system"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16930"
published: "2026-03-19"
summarized: "2026-03-19T14:20:38.893983"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对人脸美学预测（FBP）任务中数据稀缺导致的过拟合问题以及模型构建效率低下的挑战，提出了一种融合迁移学习与宽度学习系统（BLS）的新方法。该方法首先利用基于EfficientNet的迁移学习构建特征提取器，然后将提取的人脸美学特征输入BLS进行预测（E-BLS），并进一步设计了连接层以优化特征提取器与BLS的衔接（ER-BLS）。实验结果表明，所提出的E-BLS和ER-BLS方法在FBP准确率上显著优于现有的BLS和CNN方法，验证了该方法的有效性和优越性。

【方法概述 / Method】
本文采用两阶段融合策略：第一阶段使用预训练的EfficientNet作为迁移学习骨干网络提取人脸美学特征，解决小数据集下的过拟合问题；第二阶段将提取的特征输入宽度学习系统（BLS）进行快速模型构建与训练，通过随机映射节点和增强节点实现高效学习。在此基础上，ER-BLS通过引入连接层进一步优化特征提取器与BLS之间的特征传递机制。

【实验结果 / Results】
实验结果表明，相比传统的BLS和CNN方法，所提出的E-BLS和ER-BLS显著提升了人脸美学预测的准确率。该方法在保持快速训练优势的同时，有效缓解了小样本场景下的过拟合问题，展现出优于现有方法的性能表现。

【应用价值 / Applications】
该方法可广泛应用于模式识别、目标检测和图像分类等计算机视觉任务，特别适用于数据稀缺且需要快速部署模型的实际场景。其在人脸美学评估领域的成功应用，为美容推荐系统、人像摄影评分、社交媒体内容审核等商业化应用提供了高效可靠的技术方案。
