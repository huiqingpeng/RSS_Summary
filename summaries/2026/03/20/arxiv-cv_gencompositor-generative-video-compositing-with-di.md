---
title: "GenCompositor: Generative Video Compositing with Diffusion Transformer"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.02460"
published: "2026-03-20"
summarized: "2026-03-20T16:13:04.959622"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GenCompositor，首个基于扩散Transformer（DiT）的生成式视频合成框架，用于自动化传统耗时耗力的视频合成流程。该框架能够以交互方式将前景视频的身份与运动信息自适应地注入目标视频，支持用户自定义动态元素的大小、运动轨迹等属性。研究还构建了包含61K组视频的VideoComp数据集，实验表明该方法在保真度和一致性方面优于现有方案。

【方法概述 / Method】
论文设计了基于DiT的新型流水线，包含三个核心组件：（1）轻量级背景保持分支，通过掩码token注入维持目标视频编辑前后的一致性；（2）DiT融合块，利用全自注意力机制继承动态元素，并配合前景增强训练策略；（3）扩展旋转位置编码（ERoPE），实现不同布局背景下前景与背景视频的融合控制。

【实验结果 / Results】
实验在自建VideoComp数据集上进行，结果表明GenCompositor在生成质量、时序一致性和用户可控性方面均显著优于现有潜在解决方案。背景保持分支有效减少了目标视频的失真，ERoPE实现了精确的位置控制，整体系统在动态元素注入的真实感和连贯性上达到最优性能。

【应用价值 / Applications】
该技术可广泛应用于影视后期制作、广告视频生成、虚拟现实内容创作等领域，大幅降低专业视频合成的门槛和成本。交互式的属性控制使非专业用户也能快速实现复杂的视觉效果，为AIGC时代的视频生产提供高效自动化工具。
