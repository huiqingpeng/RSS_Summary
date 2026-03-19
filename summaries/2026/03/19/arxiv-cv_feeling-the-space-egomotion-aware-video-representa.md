---
title: "Feeling the Space: Egomotion-Aware Video Representation for Efficient and Accurate 3D Scene Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17980"
published: "2026-03-19"
summarized: "2026-03-19T16:20:04.563608"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Motion-MLLM框架，通过融合惯性测量单元（IMU）采集的自我运动（egomotion）数据与视频信息，增强多模态大语言模型（MLLMs）的3D场景理解能力。该框架解决了现有方法依赖计算昂贵的3D表示（如点云或BEV地图）或缺乏物理尺度感知的问题。实验表明，Motion-MLLM在3D场景理解和空间推理任务上达到或超越当前最优方法，同时计算开销显著降低（成本效益分别提升1.40倍和1.63倍）。

【方法概述 / Method】
Motion-MLLM包含两个核心组件：（1）级联运动-视觉关键帧过滤模块，利用IMU数据和视觉特征高效筛选稀疏且具有代表性的关键帧；（2）非对称跨模态融合模块，以运动token为中介，将自我运动线索和跨帧视觉上下文注入视觉表示，实现视觉内容与物理运动轨迹的 grounding。

【实验结果 / Results】
Motion-MLLM在多种3D场景理解和空间推理任务上取得显著提升；与基于视频帧的SOTA方法相比，在保持相当或更高精度的同时，计算成本大幅降低；相较于依赖显式3D数据的方法，同样展现出更高的成本效益（1.63倍），证明了其在准确性与效率之间的优越平衡。

【应用价值 / Applications】
该研究适用于机器人导航、自动驾驶、增强现实（AR）等需要实时3D场景理解的领域，尤其在资源受限的嵌入式设备上具有优势。通过IMU与视频的低成本融合，为移动设备提供精确的空间推理能力，无需昂贵的3D传感器或重建流程。
