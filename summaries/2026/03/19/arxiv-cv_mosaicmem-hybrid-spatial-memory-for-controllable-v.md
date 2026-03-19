---
title: "MosaicMem: Hybrid Spatial Memory for Controllable Video World Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17117"
published: "2026-03-19"
summarized: "2026-03-19T15:05:40.138071"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了 Mosaic Memory (MosaicMem)，一种用于可控视频世界模型的混合空间记忆机制，旨在解决显式3D结构难以处理动态物体、隐式记忆难以准确遵循相机运动的问题。MosaicMem 将图像块提升到3D空间以实现可靠定位和检索，同时利用扩散模型的原生条件机制保持对文本提示的遵循能力。实验表明，该方法在相机姿态 adherence 上优于隐式记忆基线，在动态场景建模上优于显式基线，并支持分钟级导航、基于记忆的编辑和自回归 rollout。

【方法概述 / Method】
MosaicMem 采用"分块-组合"（patch-and-compose）接口，将历史帧的图像块根据深度信息提升到3D空间形成混合记忆，在查询视角下进行空间对齐和组合。该方法结合 PRoPE（Progressive RoPE）相机条件编码和两种新的记忆对齐策略，在保持空间一致性的同时允许模型灵活生成动态内容。

【实验结果 / Results】
实验显示 MosaicMem 在相机姿态 adherence 方面显著优于隐式记忆方法，在动态物体建模方面优于纯显式3D基线。该系统能够支持分钟级别的长视频导航生成，实现了在保持场景结构一致的前提下进行记忆驱动的场景编辑，并支持自回归方式的连续视频 rollout。

【应用价值 / Applications】
MosaicMem 可应用于可控视频世界模拟器，支持虚拟环境探索、长时程视频生成和交互式场景编辑等任务。该技术为构建一致的交互式3D世界模拟器提供了基础，在游戏开发、虚拟现实、机器人仿真训练以及创意内容生成等领域具有重要价值。
