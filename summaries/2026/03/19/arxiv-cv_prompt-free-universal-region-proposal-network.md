---
title: "Prompt-Free Universal Region Proposal Network"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17554"
published: "2026-03-19"
summarized: "2026-03-19T15:13:48.044815"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Prompt-Free Universal Region Proposal Network（PF-RPN），一种无需外部提示即可识别潜在目标的新型区域提议网络。该方法通过三个核心模块——Sparse Image-Aware Adapter（SIA）、Cascade Self-Prompt（CSP）和Centerness-Guided Query Selection（CG-QS）——实现自主目标定位，摆脱了对示例图像、预定义类别或文本描述的依赖。实验表明，PF-RPN仅需少量数据（如5%的MS COCO数据）即可优化，并能直接应用于水下目标检测、工业缺陷检测、遥感图像检测等19个不同领域的任务而无需微调。

【方法概述 / Method】
PF-RPN采用三阶段架构：首先，SIA模块利用可学习的查询嵌入与视觉特征动态交互，完成潜在目标的初始定位；其次，CSP模块通过自提示的可学习嵌入以级联方式自主聚合信息丰富的视觉特征，识别剩余潜在目标；最后，CG-QS模块基于中心度评分网络筛选高质量查询嵌入。整个框架完全依赖视觉特征自主学习，无需任何外部提示。

【实验结果 / Results】
该方法在19个不同领域的数据集上验证了有效性，展现出强大的跨域泛化能力。关键优势在于数据效率：仅需MS COCO 5%的训练数据即可完成优化，同时保持 competitive 的性能表现。在零样本迁移场景下，PF-RPN无需针对特定领域微调即可直接部署，显著优于依赖提示的传统方法。

【应用价值 / Applications】
PF-RPN的实际价值体现在其广泛的适用性和部署便捷性：可直接应用于水下探测、工业质检、遥感监测等专业领域，大幅降低领域适配成本；适用于数据标注稀缺或类别定义模糊的场景；为开放世界目标检测和自主机器人感知系统提供了灵活的基础组件，消除了人工设计提示的工程瓶颈。
