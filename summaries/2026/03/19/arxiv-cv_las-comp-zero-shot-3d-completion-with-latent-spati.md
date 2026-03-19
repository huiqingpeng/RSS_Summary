---
title: "LaS-Comp: Zero-shot 3D Completion with Latent-Spatial Consistency"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.18735"
published: "2026-03-19"
summarized: "2026-03-19T16:31:27.818766"
ai_provider: "openai"
---

【论文摘要 / Abstract】
LaS-Comp 提出了一种零样本、类别无关的 3D 形状补全方法，利用 3D 基础模型的丰富几何先验知识，处理多样化的部分观测输入。该方法采用显式替换与隐式细化的两阶段设计，在无需训练的情况下实现了对真实世界和合成数据的高质量补全，并建立了 Omni-Comp 综合基准进行更全面评估。

【方法概述 / Method】
LaS-Comp 的核心是两阶段互补设计：(i) 显式替换阶段保留部分观测的几何结构以确保忠实补全；(ii) 隐式细化阶段优化观测区域与合成区域之间的边界无缝衔接。该方法无需训练，可兼容不同的 3D 基础模型。

【实验结果 / Results】
在 Omni-Comp 基准（包含真实世界与合成数据及多种挑战性部分模式）上的定量和定性实验表明，LaS-Comp 优于现有最先进方法，展现出更强的泛化能力和补全质量。

【应用价值 / Applications】
该研究可应用于机器人感知、增强现实、自动驾驶等领域的 3D 场景理解与重建，特别是在缺乏完整训练数据或面对新类别物体时，提供即插即用的补全解决方案。零样本特性显著降低了实际部署成本。
