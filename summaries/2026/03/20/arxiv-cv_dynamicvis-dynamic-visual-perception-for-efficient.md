---
title: "DynamicVis: Dynamic Visual Perception for Efficient Remote Sensing Foundation Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2503.16426"
published: "2026-03-20"
summarized: "2026-03-20T16:11:06.819280"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了DynamicVis，一种专为遥感图像稀疏特性设计的视觉基础模型。针对遥感图像中目标极度稀疏（关键目标占比不足1%）且空间冗余巨大的特点，DynamicVis通过动态区域感知机制自适应地处理高显著性token，同时以无参数方式整合背景上下文，显著降低超长2D序列（约10万token）的处理复杂度。此外，论文创新性地提出区域级元嵌入多实例学习（MIL）预训练范式，在百万规模数据集上训练，显式解耦稀疏前景实例与密集背景。在九项下游任务上的广泛评估表明，DynamicVis在稀疏目标和实例级感知任务（如小目标检测、变化检测）上表现卓越。

【方法概述 / Method】

DynamicVis的核心架构是动态区域感知状态空间模型（Dynamic Region-Aware SSM），该机制摒弃了传统ViT的均匀密集处理方式，通过自适应路由和增量建模仅处理任务相关的高显著性token，同时采用无参数集成策略处理背景上下文信息。预训练方面，采用区域级元嵌入多实例学习（Region-Level Meta-Embedding MIL）范式，在潜在语义空间中显式分离稀疏前景与密集背景，克服了传统像素重建方法的语义模糊问题。

【实验结果 / Results】

DynamicVis在九个多样化的下游任务上进行了广泛评估，展现出卓越的有效性，尤其在稀疏目标和实例级感知任务中占据主导地位，包括小目标检测和变化检测等关键应用。该模型成功将处理超长2D token序列（约10万个token）的复杂度大幅降低，同时保持了高精度感知能力。

【应用价值 / Applications】

DynamicVis可广泛应用于高分辨率地球观测场景，如军事侦察中的舰船与车辆检测、城市变化监测、环境监测等需要处理大规模遥感图像的任务。该模型通过大幅降低计算成本同时提升小目标检测精度，为实时或资源受限环境下的遥感图像智能解译提供了高效解决方案，具有重要的实际部署价值和商业应用前景。
