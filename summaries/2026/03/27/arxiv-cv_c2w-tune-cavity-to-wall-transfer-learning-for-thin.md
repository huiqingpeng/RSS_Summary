---
title: "C2W-Tune: Cavity-to -Wall Transfer Learning for Thin Atrial Wall Segmentation in 3D Late Gadolinium-enhanced Magnetic Resonance"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24992"
published: "2026-03-27"
summarized: "2026-03-28T07:19:48.805118"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出C2W-Tune，一种两阶段腔室到壁面的迁移学习框架，用于解决3D晚期钆增强MRI（LGE-MRI）中左心房薄壁分割的挑战。该方法首先利用高精度左心房腔室模型作为解剖先验进行预训练，然后通过渐进式层解冻策略将知识迁移至壁面分割任务。实验表明，该方法显著优于从零训练的基线模型，壁面Dice系数从0.623提升至0.814，且在减少监督数据（70例）的情况下仍保持0.78的Dice性能。

【方法概述 / Method】
C2W-Tune采用3D U-Net架构配合ResNeXt编码器和实例归一化，第一阶段预训练网络分割左心房腔室以学习稳健的心房表征；第二阶段迁移预训练权重，通过渐进式层解冻策略在保留心内膜特征的同时实现壁面特异性优化。这种受控微调机制平衡了先验知识的保持与任务特定适应。

【实验结果 / Results】
在2018左心房分割挑战数据集上，C2W-Tune取得显著性能提升：壁面Dice系数达0.814（基线0.623），1mm表面Dice达0.731（基线0.553）；边界误差大幅降低，95%豪斯多夫距离从2.95mm降至2.55mm，平均对称表面距离从0.71mm降至0.63mm。即使在70例减少监督数据下，仍保持0.78的Dice和3.15mm的HD95，超越多类基准方法（通常Dice为0.6-0.7）。

【应用价值 / Applications】
该研究为临床左心房壁厚度测绘和纤维化量化提供了更精确的分割工具，对房颤等心律失常疾病的诊断和治疗规划具有重要价值。其迁移学习策略可推广至其他医学影像中薄壁结构的分割任务，尤其在标注数据稀缺的场景下具有数据高效性优势。
