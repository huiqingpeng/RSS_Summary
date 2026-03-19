---
title: "Eye image segmentation using visual and concept prompts with Segment Anything Model 3 (SAM3)"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17715"
published: "2026-03-19"
summarized: "2026-03-19T15:16:39.530495"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究评估了Segment Anything Model 3 (SAM3)在眼图像分割任务中的表现，并与前代模型SAM2进行对比。研究发现，SAM3无论是采用视觉提示还是概念（文本）提示模式，在大多数情况下的眼图像分割性能均未超越SAM2，且SAM2运行速度更快。因此，作者得出结论：SAM2仍是眼图像分割的最佳选择，并提供了适配SAM3代码库以处理任意时长视频的开源实现。

【方法概述 / Method】
研究采用对比实验方法，在两类数据集上评估SAM2与SAM3的性能：一是实验室环境采集的高分辨率高质量眼视频，二是野外场景下采集的TEyeD挑战性眼视频数据集。测试涵盖了SAM3新增的文本提示（concept prompting）功能与传统视觉提示两种交互模式。

【实验结果 / Results】
实验结果表明，SAM3在视觉提示和概念提示两种模式下，对实验室数据和野外数据的眼图像分割效果均未优于SAM2。SAM2不仅在分割精度上表现更佳，同时具有更快的推理速度。作者据此否定了"更新版本即更优"的假设，并公开了支持任意时长视频处理的SAM3代码适配版本。

【应用价值 / Applications】
该研究为眼动追踪、眼科诊断及人机交互等领域的研究者提供了重要的模型选型参考，避免因盲目追求新版本而降低系统性能。开源的代码适配方案解决了SAM3原生代码对视频时长的限制问题，便于后续研究者在实际应用中处理长时程眼动记录数据。
