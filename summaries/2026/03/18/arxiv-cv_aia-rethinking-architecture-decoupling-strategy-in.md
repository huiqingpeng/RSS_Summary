---
title: "AIA: Rethinking Architecture Decoupling Strategy In Unified Multimodal Model"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.22663"
published: "2026-03-18"
summarized: "2026-03-18T18:29:54.372685"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对统一多模态模型中图像生成与理解任务的目标冲突问题，提出了一种新的解决思路。研究发现，传统的架构解耦策略（如双编码器、MoE/MoT架构或冻结MLLM）虽能缓解冲突，但会损害模型的交错生成能力，且本质上只是驱动模型趋向任务特定的跨模态交互模式。为此，作者提出了注意力交互对齐（AIA）损失函数，在不进行模型解耦的情况下显式学习任务特定的多模态交互模式，在Emu3和Janus-Pro上的实验表明AIA能同时提升生成和理解性能。

【方法概述 / Method】

作者首先通过分析跨模态注意力行为，发现架构解耦并未真正解决任务冲突，而是使模型行为趋近于任务特定模型（如Qwen3-VL和HunyuanImage-3.0）。基于这一发现，提出Attention Interaction Alignment（AIA）损失，通过在训练过程中显式对齐不同任务的注意力交互模式，替代昂贵的模型结构解耦。AIA可直接应用于现有统一多模态模型的SFT和post-training阶段，无需修改模型架构。

【实验结果 / Results】

AIA在Emu3和Janus-Pro两个代表性统一多模态模型上验证了通用性：应用于Emu3的SFT阶段以及Janus-Pro的post-training阶段后，模型不仅优化了跨模态注意力模式，同时在图像生成和理解两项任务上均取得性能提升。实验表明，无需复杂的架构改动，仅通过训练目标优化即可实现与解耦策略相当甚至更优的效果。

【应用价值 / Applications】

该研究为统一多模态模型的训练提供了更高效、更优雅的解决方案，避免了过度解耦带来的模型碎片化问题，有助于保持模型的统一性和可扩展性。AIA方法可广泛应用于需要同时支持视觉理解与生成能力的AGI系统、多模态大模型产品，以及资源受限场景下需要精简架构的部署环境。
