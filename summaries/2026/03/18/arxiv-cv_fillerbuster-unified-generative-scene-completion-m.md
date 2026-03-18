---
title: "Fillerbuster: Unified Generative Scene Completion Model for Casual Captures"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2502.05175"
published: "2026-03-18"
summarized: "2026-03-18T18:25:19.519220"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 Fillerbuster，一个统一的生成式场景补全模型，利用多视图潜在扩散 Transformer 补全 3D 场景中未知区域。该模型针对日常随意拍摄的稀疏、不完整数据（常缺失物体后方或场景上方的内容），能够同时处理数百帧输入图像，生成未知目标视图，并在相机参数未知时恢复图像位姿。研究展示了在现有数据集上的部分场景补全结果，并提出了无标定场景补全新任务，模型可联合预测位姿和生成新内容。

【方法概述 / Method】

Fillerbuster 采用多视图潜在扩散 Transformer 架构，训练一个能够消费大量输入帧上下文的生成模型，联合修复所有输入并生成未知区域的目标视图。该方法支持灵活的统一修复框架，可同时预测多张图像和相机位姿，并具备扩展到深度等其他模态的潜力。

【实验结果 / Results】

论文在两个现有数据集上验证了部分场景补全的效果，并展示了无标定场景补全任务中模型同时预测相机位姿和生成新内容的能力。模型已开源并集成到 Nerfstudio 和 Gsplat 等主流重建平台。

【应用价值 / Applications】

该研究适用于日常随意拍摄的三维场景重建与补全，可解决稀疏视角下缺失区域（如遮挡后方、场景顶部）的内容生成问题。开源框架便于集成到现有神经辐射场和高斯溅射平台，为增强现实、虚拟现实内容创作、机器人导航等需要完整 3D 场景表示的应用提供实用工具。
