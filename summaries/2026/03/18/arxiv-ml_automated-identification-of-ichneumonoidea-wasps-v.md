---
title: "Automated identification of Ichneumonoidea wasps via YOLO-based deep learning: Integrating HiresCam for Explainable AI"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16351"
published: "2026-03-18"
summarized: "2026-03-18T16:12:27.363646"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究提出了一种基于YOLO深度学习架构的自动化姬蜂总科（Ichneumonoidea）寄生蜂识别框架，集成高分辨率类激活映射（HiResCAM）以增强模型可解释性。该系统能从高分辨率图像中同时识别蜂类科属，在包含3556张膜翅目标本的 curated 数据集上实现了超过96%的识别准确率。HiResCAM可视化验证了模型关注翅脉、触角分节和腹部结构等分类学相关解剖区域，证明了学习特征的生物学合理性，为加速这一描述不足寄生蜂总科的生物多样性研究提供了可信的AI工具。

【方法概述 / Method】
研究采用YOLO目标检测架构作为核心识别模型，并集成HiResCAM技术实现高分辨率类激活可视化以提升可解释性。实验使用3556张高分辨率膜翅目昆虫图像，涵盖姬蜂科（786张）、茧蜂科（648张）、蜜蜂科（466张）及胡蜂科（460张）等主要类群。

【实验结果 / Results】
模型在精确率、召回率、F1分数和准确率等指标上均表现优异，识别准确率超过96%，且对形态变异具有稳健泛化能力。HiResCAM可视化明确显示模型决策聚焦于翅脉、触角分节和腹部结构等分类学关键形态特征，而非背景噪声或无关区域。

【应用价值 / Applications】
该框架可直接应用于生物多样性评估、生态监测和生物防治项目中的寄生蜂快速鉴定，显著降低对专家经验的依赖。可解释AI技术的集成增强了模型透明度与可信度，使其适用于严格的昆虫学研究场景，有望加速姬蜂总科这一物种丰富但研究不足类群的分类学表征工作。
