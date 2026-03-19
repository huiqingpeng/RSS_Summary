---
title: "Gesture-Aware Pretraining and Token Fusion for 3D Hand Pose Estimation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17396"
published: "2026-03-19"
summarized: "2026-03-19T15:10:11.690740"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对单目RGB图像的3D手部姿态估计问题，提出利用手势语义作为归纳偏置的新思路。作者设计了一个两阶段框架：首先通过手势感知预训练学习信息丰富的嵌入空间，然后使用基于手势嵌入引导的逐关节Token Transformer回归MANO手部参数。实验表明，该方法在InterHand2.6M数据集上持续超越SOTA基线EANet，且其预训练优势可跨架构迁移而无需修改。

【方法概述 / Method】
论文采用两阶段训练策略：第一阶段利用InterHand2.6M的粗粒度和细粒度手势标签进行手势感知预训练，构建判别性嵌入空间；第二阶段引入逐关节Token Transformer，将手势嵌入作为中间表示来指导最终的MANO参数回归。训练目标采用分层设计，同时约束参数、关节位置和手部结构关系。

【实验结果 / Results】
在InterHand2.6M数据集上的实验表明，手势感知预训练能持续提升单手姿态估计精度，超越当前最优的EANet基线方法。关键发现是预训练获得的语义嵌入具有跨架构泛化能力，可直接应用于不同网络结构而无需调整。

【应用价值 / Applications】
该技术可直接应用于AR/VR交互系统、自然人机交互界面以及手语理解等场景。手势语义与3D姿态的联合建模特别适用于需要同时识别手势类别和精确手部姿态的下游任务，为计算资源受限场景提供了可迁移的预训练方案。
