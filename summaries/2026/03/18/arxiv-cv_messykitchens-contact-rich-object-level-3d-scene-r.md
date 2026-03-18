---
title: "MessyKitchens: Contact-rich object-level 3D scene reconstruction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16868"
published: "2026-03-18"
summarized: "2026-03-18T18:21:42.472220"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MessyKitchens，一个包含杂乱真实场景的高保真物体级3D重建数据集，提供精确的物体形状、姿态和接触关系标注。作者还开发了Multi-Object Decoder (MOD)，扩展了SAM 3D方法以实现联合物体级场景重建。实验表明，该数据集在配准精度和物体间穿透方面显著优于现有数据集，MOD方法在三个数据集上均取得了一致且显著的性能提升。

【方法概述 / Method】
论文基于SAM 3D单物体重建方法，设计了Multi-Object Decoder (MOD)模块，实现多物体的联合重建。MOD能够同时处理场景中的多个物体，建模物体间的空间关系和物理约束，确保重建结果满足非穿透性和真实接触等物理合理性要求。

【实验结果 / Results】
MessyKitchens数据集在配准精度上显著优于之前的数据集，并有效减少了物体间的相互穿透现象。MOD方法在三个不同数据集上的对比实验表明，相比现有最优方法，该方法在物体级场景重建任务上取得了一致且显著的改进。

【应用价值 / Applications】
该研究对机器人操作和动画制作具有重要价值，可为机器人提供物理合理的场景理解以支持抓取和交互任务，同时满足动画场景中对真实接触和碰撞的严格要求。公开的数据集、代码和预训练模型将推动物体级3D重建领域的进一步研究。
