---
title: "Is Geometry Enough? An Evaluation of Landmark-Based Gaze Estimation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24724"
published: "2026-03-27"
summarized: "2026-03-28T07:15:56.183965"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究系统评估了基于面部关键点的几何方法在视线估计中的性能表现。研究发现，虽然关键点模型在域内评估中表现略逊于基于外观的深度CNN方法（主要由于关键点检测器引入的噪声），但其跨域泛化能力与ResNet18基线相当。这表明稀疏几何特征足以编码稳健的视线信息，为高效、可解释且保护隐私的边缘应用开辟了新途径。

【方法概述 / Method】
论文构建了标准化的关键点提取与归一化流程，从Gaze360、ETH-XGaze和GazeGene三个大规模数据集处理数据。研究训练了三类轻量级回归模型：极端梯度提升树（XGBoost）、整体式多层感知机（MLP）以及用于捕获双眼几何信息的孪生MLP架构。

【实验结果 / Results】
关键点模型在域内评估中性能较低，归因于关键点检测器引入的数据噪声；但在跨域评估中，所提出的MLP架构展现出与ResNet18基线相当的泛化能力。实验结果证明几何特征能够有效支持稳健的视线估计。

【应用价值 / Applications】
该研究为资源受限的边缘设备提供了轻量级、可解释的视线估计解决方案。相比黑盒CNN模型，几何方法计算开销低、易于解释，且无需存储原始图像数据，更适合隐私敏感场景（如辅助技术、人机交互和移动设备应用）。
