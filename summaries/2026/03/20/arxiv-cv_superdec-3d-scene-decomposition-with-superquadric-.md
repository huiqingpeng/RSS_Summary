---
title: "SuperDec: 3D Scene Decomposition with Superquadric Primitives"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2504.00992"
published: "2026-03-20"
summarized: "2026-03-20T16:11:24.309232"
ai_provider: "openai"
---

【论文摘要 / Abstract】
SuperDec 提出了一种将3D场景分解为超二次曲面（superquadric）基元的紧凑表示方法。与现有研究主要利用几何基元实现照片级真实感渲染不同，该方法专注于构建紧凑且具表达力的场景表征。通过局部求解单物体分解问题并结合实例分割技术，实现了从物体级到完整3D场景的扩展，并在ShapeNet训练后成功泛化到ScanNet++和Replica数据集。

【方法概述 / Method】
该方法设计了一种新型神经网络架构，能够以任意物体的点云为输入，高效地将其分解为紧凑的超二次曲面集合。核心策略是将复杂场景分解问题局部化处理——先对单个物体进行超二次曲面拟合，再利用实例分割方法将解决方案扩展到完整场景尺度。

【实验结果 / Results】
模型在ShapeNet数据集上完成训练，并在ScanNet++数据集的物体实例以及完整的Replica场景上验证了良好的泛化能力。实验表明该方法能够生成紧凑的3D场景表示，在保持表达力的同时显著降低存储开销。

【应用价值 / Applications】
基于超二次曲面的紧凑表示可支持多种下游应用，包括机器人操作任务（如抓取规划）以及可控的视觉内容生成与编辑。这种语义化、参数化的基元表示为场景理解和交互式3D内容创作提供了高效的基础表征。
