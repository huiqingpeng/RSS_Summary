---
title: "Domain Adaptation Without the Compute Burden for Efficient Whole Slide Image Analysis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15774"
published: "2026-03-18"
summarized: "2026-03-18T17:18:26.523578"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了EfficientWSI（eWSI）框架，通过整合参数高效微调（PEFT）与多实例学习（MIL）实现全切片图像（WSI）的端到端训练。研究发现，eWSI配合ImageNet预训练特征提取器即可达到或超越使用域内预训练提取器的MIL方法性能，显著降低计算成本；当与域内特征提取器结合时，eWSI还能进一步提升分类性能，有效捕捉任务特定信息。该研究为计算病理学中的任务特异性学习提供了一条计算高效的新路径。

【方法概述 / Method】
eWSI将参数高效微调技术（PEFT）与多实例学习框架相结合，允许在保持预训练特征提取器大部分参数冻结的情况下，仅微调少量任务相关参数。该方法实现了WSI级别的端到端训练，避免了传统方法中固定特征表示带来的任务特异性信息损失，同时大幅减少了GPU内存需求和训练时间。

【实验结果 / Results】
研究在Camelyon16、TCGA和BRACS三个数据集的七项WSI级任务上进行了评估。结果表明，eWSI使用ImageNet预训练提取器即可匹配或超越使用域内预训练提取器的传统MIL方法；当应用于域内预训练提取器时，eWSI在大多数情况下进一步提升了分类性能，证明其能够有效利用任务特定信息。

【应用价值 / Applications】
eWSI为计算病理学中的全切片图像分析提供了一种实用解决方案，使资源受限的研究机构和临床实验室无需昂贵的域内预训练即可部署高性能AI辅助诊断系统。该方法可广泛应用于肿瘤检测、癌症分型等病理诊断任务，加速早期诊断和精准治疗的临床转化。
