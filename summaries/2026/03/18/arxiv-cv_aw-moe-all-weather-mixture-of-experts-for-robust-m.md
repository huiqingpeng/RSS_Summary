---
title: "AW-MoE: All-Weather Mixture of Experts for Robust Multi-Modal 3D Object Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16261"
published: "2026-03-18"
summarized: "2026-03-18T18:10:01.814495"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出AW-MoE框架，首次将混合专家模型（MoE）应用于全天候鲁棒多模态3D目标检测。该框架通过图像引导的天气感知路由（IWR）实现精确天气分类，并动态选择最相关的天气专属专家（WSE）处理不同天气场景的数据分布差异。实验表明，AW-MoE在恶劣天气条件下性能提升约15%，且推理开销可忽略不计，同时具有良好的可扩展性。

【方法概述 / Method】

AW-MoE采用混合专家架构，核心组件包括：（1）Image-guided Weather-aware Routing（IWR），利用图像特征在天气判别上的优势及场景不变性进行精确天气分类；（2）Weather-Specific Experts（WSE），基于IWR的Top-K选择机制动态激活对应天气专家；（3）Unified Dual-Modal Augmentation（UDMA），实现LiDAR与4D Radar双模态数据的同步增强并保持场景真实感。

【实验结果 / Results】

在真实数据集上的大量实验表明，AW-MoE在恶劣天气条件下相比现有最优方法提升约15%的检测性能，同时仅引入极低的推理开销。此外，将AW-MoE集成到现有基线检测器中也能获得超越当前SOTA的性能提升，验证了该方法的强可扩展性。

【应用价值 / Applications】

AW-MoE可直接应用于自动驾驶系统的全天候感知模块，解决雨雾雪等恶劣天气下3D目标检测性能退化问题。其即插即用的特性使其能够无缝集成到现有主流检测框架中，为自动驾驶车辆在复杂气象条件下的安全运行提供可靠保障，具有重要的工程实用价值。
