---
title: "MIPHEI-ViT: Multiplex Immunofluorescence Prediction from H&E Images using ViT Foundation Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2505.10294"
published: "2026-03-20"
summarized: "2026-03-20T16:11:36.309195"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出MIPHEI-ViT，一种基于ViT病理基础模型的U-Net架构，用于从H&E染色图像预测多重免疫荧光（mIF）信号，以解决mIF因成本和物流限制难以临床普及的问题。该模型利用预训练的视觉Transformer编码器，针对核内容、免疫细胞谱系、上皮、间质、血管和增殖等全面标志物面板进行预测。在OrionCRC数据集上训练并在五个独立数据集验证的结果表明，MIPHEI在Pan-CK、alpha-SMA等标志物的细胞类型分类中显著优于现有基线，为大规模H&E数据集的无mIF细胞类型分析提供了新途径。

【方法概述 / Method】
MIPHEI采用U-Net风格的编码器-解码器架构，其中编码器使用预训练的ViT病理基础模型提取H&E图像的丰富表征，解码器则将这些特征上采样以预测多通道mIF信号。模型在OrionCRC公开的结直肠癌H&E与mIF配对图像数据集上进行端到端训练，学习从形态学特征到分子标志物表达的复杂映射关系。

【实验结果 / Results】
在OrionCRC测试集上，MIPHEI实现了准确的细胞类型分类，Pan-CK的F1分数达0.93，alpha-SMA为0.83，CD3e为0.68，CD20为0.36，CD68为0.28，多数标志物显著优于最先进基线和随机分类器。模型在HEMIT、PathoCell、IMMUcan、Lizard和PanNuke五个独立外部数据集上完成验证，证明了良好的泛化能力。

【应用价值 / Applications】
MIPHEI使研究者能够仅利用常规获取的H&E图像进行细胞类型感知分析，无需昂贵的mIF实验，从而降低大规模病理研究成本。该技术可应用于挖掘空间细胞组织与患者预后之间的关系，支持肿瘤微环境研究和精准医疗中的生物标志物发现，为现有H&E病理档案的回顾性分子分析提供可能。
