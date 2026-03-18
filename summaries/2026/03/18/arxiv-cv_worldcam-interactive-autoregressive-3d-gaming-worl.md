---
title: "WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16871"
published: "2026-03-18"
summarized: "2026-03-18T18:22:04.488715"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了WorldCam，一种基于自回归模型的交互式3D游戏世界生成方法。核心创新在于将相机位姿作为统一的几何表示，同时解决精确动作控制和长程3D一致性问题。作者构建了包含3000分钟真实人类游戏玩法的数据集，实验表明该方法在动作可控性、长程视觉质量和3D空间一致性方面显著优于现有最先进方法。

【方法概述 / Method】
论文采用两阶段技术方案：首先定义基于物理的连续动作空间，将用户输入表示为李代数以推导精确的6自由度相机位姿，并通过相机嵌入器注入生成模型；其次利用全局相机位姿作为空间索引检索相关历史观测，实现长程导航中的几何一致重访。整体架构基于视频扩散Transformer的自回归生成框架。

【实验结果 / Results】
实验表明WorldCam在动作可控性、长程视觉质量和3D空间一致性三个关键指标上均大幅超越现有最先进的交互式游戏世界模型。具体性能提升体现在：精确动作对齐、数百帧长程生成稳定性，以及同一位置重访时的视觉一致性保持。

【应用价值 / Applications】
该技术可直接应用于开放世界游戏的内容生成、虚拟现实环境的实时构建，以及机器人仿真训练场景的合成。其统一的几何表示框架为可交互的AI生成内容（AIGC）提供了新的技术范式，有望降低3D游戏开发成本并支持无限探索的沉浸式体验。
