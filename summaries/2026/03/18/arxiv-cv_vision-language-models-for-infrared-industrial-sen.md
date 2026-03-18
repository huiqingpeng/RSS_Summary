---
title: "Vision-Language Models for Infrared Industrial Sensing in Additive Manufacturing Scene Description"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.11098"
published: "2026-03-18"
summarized: "2026-03-18T18:30:55.468507"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了VLM-IRIS框架，首次将视觉-语言基础模型（VLMs）适配到红外工业传感领域，实现了零样本红外图像理解。研究针对增材制造场景，通过将FLIR Boson红外相机采集的热图像预处理为RGB兼容的magma伪彩色表示，结合质心提示集成技术，在不重新训练模型的情况下完成了工件存在检测任务。实验表明，该方法能有效扩展CLIP等VLMs的热成像应用能力，为无标签工业监控提供了新途径。

【方法概述 / Method】
VLM-IRIS采用两阶段适配策略：首先将单通道红外热图像通过magma颜色映射转换为三通道伪RGB图像，使其兼容预训练的CLIP视觉编码器；随后设计质心提示集成（centroid prompt ensembling）机制，通过多位置文本提示的聚合推理提升检测稳定性。整个框架基于CLIP ViT-B/32编码器，无需任何微调或领域特定训练。

【实验结果 / Results】
在3D打印机热床工件检测任务中，VLM-IRIS实现了高精度零样本检测，利用构建板与工件间的温差特征完成有效识别。对比实验表明，magma颜色映射配合质心提示集成显著优于直接灰度映射或单一提示策略，验证了红外-RGB转换与提示工程结合的有效性。

【应用价值 / Applications】
该研究为低光照、封闭腔体等挑战性制造环境（如金属3D打印、焊接监控）提供了免标注的智能检测方案，可降低工业视觉系统的部署成本。VLM-IRIS的零样本特性使其能快速适配不同热成像任务，推动红外传感在预测性维护、质量控制和自动化生产中的普及应用。
