---
title: "EffectErase: Joint Video Object Removal and Insertion for High-Quality Effect Erasing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19224"
published: "2026-03-20"
summarized: "2026-03-20T16:06:20.227494"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了EffectErase，一种高质量视频对象效果擦除方法，旨在同时消除动态目标物体及其视觉效应（如变形、阴影、反射等）并恢复无缝背景。为支持该任务，作者构建了大规模VOR数据集，包含60K对高质量视频，涵盖五种效应类型和多样场景。EffectErase通过将视频对象插入作为逆辅助任务，采用互惠学习机制，实现了优于现有方法的性能。

【方法概述 / Method】
EffectErase采用互惠学习框架，将视频对象移除与对象插入作为联合任务进行训练。模型包含任务感知区域引导机制，聚焦受影响区域的学习并支持灵活任务切换；同时引入插入-移除一致性目标，促进互补行为并共享效应区域定位与结构线索。

【实验结果 / Results】
在VOR数据集上的大量实验表明，EffectErase在多样化场景中实现了高质量的视频对象效果擦除，显著优于现有基于扩散的视频修复和对象移除方法，尤其在处理复杂动态多对象场景时展现出更强的效应消除能力和背景连贯性合成能力。

【应用价值 / Applications】
该技术可广泛应用于影视后期制作中的特效清理、广告内容编辑、隐私保护视频处理以及增强现实内容生成等领域，为专业视频编辑提供自动化的高效工具，降低人工逐帧修复的成本和时间消耗。
