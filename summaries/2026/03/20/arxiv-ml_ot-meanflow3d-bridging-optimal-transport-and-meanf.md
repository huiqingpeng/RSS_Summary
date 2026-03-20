---
title: "OT-MeanFlow3D: Bridging Optimal Transport and Meanflow for Efficient 3D Point Cloud Generation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.22592"
published: "2026-03-20"
summarized: "2026-03-20T14:07:58.531855"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了OT-MeanFlow3D（OT-MF3D），一种结合最优传输（Optimal Transport）与MeanFlow的3D点云生成框架。该方法在保持单步推理效率的同时，通过最优传输采样更好地逼近原始多步流的轨迹，解决了传统MeanFlow在样本质量上的退化问题。实验表明，该方法在ShapeNet数据集上实现了优于近期基线方法的生成与补全质量，同时降低了训练和推理成本。

【方法概述 / Method】
本文将最优传输理论融入MeanFlow框架，利用OT-based采样策略来保持底层多步流的几何结构和分布特性。该方法在训练阶段通过最优传输规划来优化流匹配目标，使得单步生成能够更准确地逼近多步扩散/流模型的输出分布。

【实验结果 / Results】
在ShapeNet数据集上的实验表明，OT-MF3D在3D点云生成和补全任务上均优于现有基线方法，同时相比传统扩散模型和流匹配模型显著减少了推理步数和计算开销。该方法实现了单步推理的高效性与多步模型质量的平衡。

【应用价值 / Applications】
该方法可广泛应用于实时3D内容生成、虚拟现实/增强现实中的场景重建、自动驾驶中的点云补全，以及计算机辅助设计（CAD）中的快速原型生成。其单步推理特性特别适合对延迟敏感的边缘计算和实时交互应用。
