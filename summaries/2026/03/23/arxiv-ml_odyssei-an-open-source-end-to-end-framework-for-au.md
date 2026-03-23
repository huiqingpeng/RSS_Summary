---
title: "ODySSeI: An Open-Source End-to-End Framework for Automated Detection, Segmentation, and Severity Estimation of Lesions in Invasive Coronary Angiography Images"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20021"
published: "2026-03-23"
summarized: "2026-03-24T07:24:19.844597"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ODySSeI，一个开源的端到端框架，用于侵入性冠状动脉造影（ICA）图像中病变的自动检测、分割和严重程度估计。该框架创新性地引入了金字塔增强方案（PAS）来提升深度学习模型的鲁棒性和实时性能，并提出了无需定量冠状动脉造影的病变严重程度估计（LSE）技术，可直接从预测的几何结构计算最小管腔直径和直径狭窄率。实验表明，PAS在复杂任务中带来显著性能提升（病变检测性能提高2.5倍），且LSE预测的MLD值与真实值仅相差±2-3像素，整个框架可在CPU上几秒、GPU上不到一秒内处理单张图像。

【方法概述 / Method】
ODySSeI采用深度学习架构，整合了病变检测和分割两个核心模型，并通过新颖的金字塔增强方案（PAS）进行训练以增强模型对不同患者群体的泛化能力。严重程度估计采用无定量冠状动脉造影的LSE技术，直接从分割预测的几何结构中计算最小管腔直径（MLD）和直径狭窄率，避免了传统QCA分析的主观性和复杂性。

【实验结果 / Results】
在欧洲、北美和亚洲2149例患者的多中心数据集上，PAS在复杂任务（病变检测）中实现了2.5倍的性能提升，而在相对简单的任务（病变分割）中提升1-3%；LSE技术预测的MLD值与金标准仅相差±2-3像素。框架在分布内和分布外临床数据集上均展现出强泛化能力，处理速度达到CPU数秒级、GPU亚秒级。

【应用价值 / Applications】
ODySSeI作为即插即用的开源Web界面，可支持实时临床决策，为冠状动脉疾病评估提供自动化、可重复且可扩展的分析工具。该框架有望减少ICA解读的主观性和操作者间差异，适用于需要快速、标准化病变评估的临床场景，如导管室实时指导、多中心临床研究和大规模人群筛查。
