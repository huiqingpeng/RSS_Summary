---
title: "CustomTex: High-fidelity Indoor Scene Texturing via Multi-Reference Customization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19121"
published: "2026-03-20"
summarized: "2026-03-20T16:04:32.017171"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CustomTex，一种基于参考图像的实例级高保真室内场景纹理生成框架。该框架通过双蒸馏方法（语义级蒸馏与像素级蒸馏）解决现有文本驱动方法缺乏细粒度控制、易产生伪影和烘焙光照等问题，实现了与参考图像的精确实例级对齐，并生成高分辨率、低伪影的统一纹理贴图。

【方法概述 / Method】
CustomTex采用双蒸馏策略：语义级蒸馏结合实例交叉注意力机制确保语义合理性和"参考-实例"对齐，像素级蒸馏则保证高视觉保真度；两者统一于变分分数蒸馏（VSD）优化框架中，以无纹理3D场景和多张参考图像为输入，输出高分辨率纹理。

【实验结果 / Results】
实验表明，与最先进方法相比，CustomTex在实例级一致性、纹理清晰度方面表现更优，显著减少了伪影和烘焙光照问题，能够生成高质量的定制化室内场景纹理。

【应用价值 / Applications】
该研究为3D室内场景外观编辑提供了更直接、用户友好的解决方案，可应用于游戏开发、虚拟现实、建筑可视化等领域，支持设计师通过参考图像精确控制场景中各物体的外观材质。
