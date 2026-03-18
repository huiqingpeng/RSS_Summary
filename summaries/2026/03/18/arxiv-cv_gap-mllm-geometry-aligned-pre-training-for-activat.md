---
title: "GAP-MLLM: Geometry-Aligned Pre-training for Activating 3D Spatial Perception in Multimodal Large Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16461"
published: "2026-03-18"
summarized: "2026-03-18T18:14:08.019917"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出GAP-MLLM，一种几何对齐预训练范式，旨在激活多模态大语言模型（MLLMs）的3D空间感知能力。作者指出，现有图像-based方法在3D任务上表现不佳的根源并非几何先验不足，而是文本主导的微调解码范式未能有效激活模型内部的几何表征。通过引入视觉提示的联合任务（预测稀疏点图与语义标签）以及多级渐进融合模块，GAP-MLLM显著提升了3D视觉定位、密集描述和视频目标检测等任务的性能。

【方法概述 / Method】
GAP-MLLM采用两阶段训练策略：首先进行几何对齐预训练，通过视觉提示任务强制模型联合预测稀疏点图和语义标签以建立几何意识；随后设计多级渐进融合模块，结合token级门控机制实现几何先验与语义信息的自适应整合，避免几何特征对语义推理的抑制。

【实验结果 / Results】
实验表明，GAP-MLLM在3D视觉定位、3D密集描述和3D视频目标检测任务上均取得一致的性能提升，有效增强了几何特征融合能力；相较于依赖显式3D数据的方法，该纯RGB输入方案显著缩小了性能差距，验证了几何激活预训练的有效性。

【应用价值 / Applications】
该研究为机器人导航、自动驾驶和增强现实等需要3D空间理解的应用提供了无需昂贵3D传感器的高效解决方案；通过纯视觉输入实现3D感知，降低了硬件成本与部署门槛，同时保持了强大的语义推理能力，具有广泛的实际应用前景。
