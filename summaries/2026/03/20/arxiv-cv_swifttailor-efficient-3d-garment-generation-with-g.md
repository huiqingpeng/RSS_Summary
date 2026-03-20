---
title: "SwiftTailor: Efficient 3D Garment Generation with Geometry Image Representation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19053"
published: "2026-03-20"
summarized: "2026-03-20T15:18:54.383961"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SwiftTailor，一种高效的3D服装生成框架，通过紧凑的几何图像表示统一了缝纫图案推理和基于几何的网格合成。该框架包含两个轻量级模块：PatternMaker（从多模态输入预测缝纫图案的高效视觉-语言模型）和GarmentSewer（将图案转换为新型服装几何图像的密集预测Transformer）。实验表明，SwiftTailor在Multimodal GarmentCodeData数据集上实现了最先进的精度和视觉保真度，同时显著降低了推理时间（从现有方法的30秒至1分钟大幅缩短），为下一代3D服装生成提供了可扩展、可解释且高性能的解决方案。

【方法概述 / Method】
SwiftTailor采用两阶段架构：第一阶段使用轻量级视觉-语言模型PatternMaker处理文本、图像等多模态输入，直接预测2D缝纫图案；第二阶段通过GarmentSewer（基于Transformer的密集预测网络）将缝纫图案转换为统一的服装几何图像（Garment Geometry Image），该表示在UV空间中编码所有服装面片的3D表面几何信息。最终通过高效的逆映射过程，结合重网格化和动态缝合算法直接组装3D网格，无需耗时的物理模拟。

【实验结果 / Results】
在Multimodal GarmentCodeData数据集上的广泛实验表明，SwiftTailor在保持与现有基于大视觉-语言模型方法相当甚至更高的精度和视觉保真度的同时，实现了显著的推理速度提升。相比传统方法需要30秒至1分钟的推理时间，SwiftTailor通过轻量级模块设计和避免物理模拟的端到端几何合成流程，大幅降低了计算开销，在效率和质量的权衡上达到了新的最先进水平。

【应用价值 / Applications】
SwiftTailor可广泛应用于数字时尚设计、虚拟试衣、游戏角色服装生成、影视特效制作等需要快速3D服装内容创作的场景。其高效的多模态输入支持（文本/图像）和低延迟特性使其特别适合实时交互式应用（如电商平台虚拟试衣间、AI辅助时装设计工具），同时可解释的两阶段设计（缝纫图案+几何合成）便于设计师进行迭代修改和创意控制，为规模化3D服装内容生产提供了实用解决方案。
