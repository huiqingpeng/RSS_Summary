---
title: "Halfway to 3D: Ensembling 2.5D and 3D Models for Robust COVID-19 CT Diagnosis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14832"
published: "2026-03-19"
summarized: "2026-03-19T14:20:18.009792"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种融合2.5D和3D表示的深度学习框架，用于从胸部CT扫描中进行COVID-19检测和疾病分类。该方法通过整合切片级特征和体积上下文信息，在PHAROS-AIF-MIH基准数据集上实现了94.48%的二分类准确率和79.35%的多分类准确率，证明了结合预训练切片表示与体积建模对多源医学影像分析的益处。

【方法概述 / Method】
该框架包含两个分支：2.5D分支使用DINOv3视觉Transformer处理多视角CT切片（轴位、冠状位、矢状位）以提取视觉特征；3D分支采用ResNet-18架构建模体积上下文，并依次使用方差风险外推（VREx）和 supervised contrastive learning 进行预训练以增强跨源鲁棒性。最终通过logit级集成推理融合两个分支的预测结果。

【实验结果 / Results】
在二分类COVID-19检测任务中，集成模型达到94.48%准确率和0.9426 Macro F1-score，优于任一单独模型；在多分类疾病分类任务中，2.5D DINOv3模型表现最佳，取得79.35%准确率和0.7497 Macro F1-score。

【应用价值 / Applications】
该方法可应用于临床COVID-19的自动化CT筛查与诊断，提升多源数据环境下的诊断鲁棒性；同时，其2.5D-3D集成策略为其他三维医学影像分析任务（如肺结节检测、其他传染病诊断）提供了可迁移的技术范式。
