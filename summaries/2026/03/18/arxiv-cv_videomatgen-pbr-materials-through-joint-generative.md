---
title: "VideoMatGen: PBR Materials through Joint Generative Modeling"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16566"
published: "2026-03-18"
summarized: "2026-03-18T18:15:18.580177"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了VideoMatGen，一种基于视频扩散Transformer架构的物理基础材质（PBR）生成方法。该方法以输入几何形状和文本描述为条件，联合建模多种材质属性（基础颜色、粗糙度、金属度、高度图），生成物理合理的材质。研究还引入了一种定制的变分自编码器，将多种材质模态编码到紧凑的潜在空间中，实现了多模态联合生成而不增加token数量，最终生成的高质量材质可兼容常见内容创作工具。

【方法概述 / Method】
VideoMatGen采用视频扩散Transformer作为核心架构，通过几何条件和文本提示引导材质生成过程。关键创新在于设计了一个多模态变分自编码器，将四种材质属性（base color、roughness、metallic、height）共同编码到共享的潜在空间，使得扩散模型能够在一个统一的潜在表示上进行联合生成，避免了独立生成各通道带来的不一致性问题。

【实验结果 / Results】
论文展示了该方法能够根据文本提示为3D形状生成高质量的PBR材质，生成的材质在视觉上具有物理合理性且各属性之间相互一致。由于采用了联合建模策略，生成的材质属性在空间上保持对齐，避免了传统分通道生成方法中常见的属性错位问题，且与主流内容创作工作流程兼容。

【应用价值 / Applications】
该方法可广泛应用于游戏开发、影视制作和3D内容创作领域，显著加速材质制作流程。设计师只需提供简单的文本描述即可快速获得完整的PBR材质套装，降低了专业材质制作的技术门槛，同时保证了输出结果与行业标准工具（如Blender、Unreal Engine等）的无缝集成。
