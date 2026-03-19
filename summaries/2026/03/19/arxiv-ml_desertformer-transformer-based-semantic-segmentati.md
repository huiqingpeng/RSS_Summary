---
title: "DesertFormer: Transformer-Based Semantic Segmentation for Off-Road Desert Terrain Classification in Autonomous Navigation Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17056"
published: "2026-03-19"
summarized: "2026-03-19T13:08:27.542157"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DesertFormer，一种基于SegFormer B2的语义分割模型，专门用于非结构化越野沙漠地形分类。针对沙漠环境中低色度对比、极端光照变化和稀疏植被等独特挑战，该模型将地形划分为10个生态学有意义的类别，在自建数据集上实现了64.4%的mIoU和86.1%的像素准确率，相比DeepLabV3 MobileNetV2基线提升了24.2%。研究还系统分析了主要混淆模式（Ground Clutter与Landscape、Dry Grass与Landscape），并提出类别加权训练和复制粘贴增强策略来改善稀有地形的识别。

【方法概述 / Method】
DesertFormer采用SegFormer B2架构，以分层Mix Transformer（MiT-B2）作为主干网络，通过多尺度特征提取和高效注意力机制处理高分辨率图像。针对沙漠地形数据不平衡问题，引入类别加权损失函数和复制粘贴数据增强技术，提升稀有类别（如Flowers、Logs）的分割性能。

【实验结果 / Results】
在包含4,176张512×512分辨率标注图像的专用沙漠地形数据集上，DesertFormer达到64.4%的mIoU和86.1%的像素准确率。相比DeepLabV3 MobileNetV2基线（41.0% mIoU）有显著提升，系统分析揭示了Ground Clutter与Landscape、Dry Grass与Landscape之间的主要混淆模式。

【应用价值 / Applications】
该研究为地面机器人和自动驾驶车辆在非结构化沙漠环境中的安全感知路径规划提供了关键技术支持。10类生态学意义的地形分类结果可直接用于障碍物规避、地形通过性评估和导航决策，发布的代码、模型权重和交互式推理仪表板便于实际部署和进一步研究。
