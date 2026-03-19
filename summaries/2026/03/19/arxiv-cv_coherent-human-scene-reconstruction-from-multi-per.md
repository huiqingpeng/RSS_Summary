---
title: "Coherent Human-Scene Reconstruction from Multi-Person Multi-View Video in a Single Pass"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.12789"
published: "2026-03-19"
summarized: "2026-03-19T17:03:19.048382"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CHROMM，一个统一的端到端框架，能够从多人多视角视频中联合估计相机参数、场景点云和人体网格，无需依赖外部模块或预处理。该方法整合了Pi3X和Multi-HMR的几何与人体先验知识，并引入尺度调整模块解决人体与场景之间的尺度差异问题。实验表明，CHROMM在全局人体运动和多视角姿态估计任务上达到了与现有方法相当的性能，同时运行速度比基于优化的多视角方法快8倍以上。

【方法概述 / Method】
CHROMM采用单一可训练神经网络架构，通过集成3D基础模型中的强几何先验和人体先验来实现联合重建。该方法设计了尺度调整模块来处理人体与场景之间的尺度不一致性，并提出了测试时的多视角融合策略将逐视角估计聚合为统一表示。此外，还引入了基于几何的多人关联方法，相比基于外观的方法具有更强的鲁棒性。

【实验结果 / Results】
在EMDB、RICH、EgoHumans和EgoExo4D等多个基准数据集上的实验表明，CHROMM在全局人体运动估计和多视角姿态估计任务上取得了具有竞争力的性能。与先前基于优化的多视角方法相比，CHROMM的运行速度提升超过8倍，同时保持了相当的重建精度。

【应用价值 / Applications】
CHROMM可广泛应用于虚拟现实、增强现实、运动分析和电影制作等领域，能够从多视角视频快速重建包含多人的3D场景。该方法的端到端特性和高推理速度使其特别适用于需要实时或近实时性能的应用场景，如沉浸式体验、体育分析和机器人感知等。
