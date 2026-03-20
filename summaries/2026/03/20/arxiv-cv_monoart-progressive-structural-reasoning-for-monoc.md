---
title: "MonoArt: Progressive Structural Reasoning for Monocular Articulated 3D Reconstruction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19231"
published: "2026-03-20"
summarized: "2026-03-20T16:07:01.695246"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MonoArt，一种基于渐进式结构推理的单目铰接物体3D重建统一框架。该方法通过将视觉观测逐步转化为规范几何、结构化部件表示和运动感知嵌入，避免了直接从图像特征预测运动参数的不稳定性问题。在PartNet-Mobility数据集上的实验表明，该方法在重建精度和推理速度上均达到最优水平，且无需外部运动模板或多阶段流水线。

【方法概述 / Method】
MonoArt采用渐进式结构推理策略，通过单一架构将视觉输入依次转换为三个层次化表示：规范几何、结构化部件表示和运动感知嵌入。这种分层解耦的设计有效分离了运动线索与物体结构，实现了稳定且可解释的铰接推理，无需依赖多视角监督、检索式组装或辅助视频生成等外部辅助手段。

【实验结果 / Results】
在PartNet-Mobility数据集上的广泛实验验证了MonoArt在重建精度和推理速度两方面均达到当前最优性能（state-of-the-art）。该方法展现出良好的泛化能力，可扩展应用于机器人操作和铰接场景重建等实际任务。

【应用价值 / Applications】
MonoArt可广泛应用于机器人操作领域，使机器人能够从单张图像理解可变形物体的结构及其运动机制。此外，该方法还可用于铰接场景的三维重建，为增强现实、虚拟现实以及智能交互系统提供高效的几何与运动理解能力，具有较强的实用价值和部署潜力。
