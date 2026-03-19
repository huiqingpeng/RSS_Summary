---
title: "Temporal Gains, Spatial Costs: Revisiting Video Fine-Tuning in Multimodal Large Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17541"
published: "2026-03-19"
summarized: "2026-03-19T15:13:30.116823"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文系统研究了多模态大语言模型（MLLMs）中基于视频的监督微调（Video-SFT）对视觉能力的影响。研究发现，Video-SFT 虽然能稳定提升视频理解性能，但往往以牺牲静态图像理解能力为代价，形成"时间增益、空间代价"的权衡。作者进一步提出了一种指令感知的混合帧策略（Hybrid-Frame），通过自适应分配帧数来部分缓解这一图像-视频性能权衡。

【方法概述 / Method】
研究采用系统性的实证分析方法，在多种架构、参数规模和帧采样设置下对比 Video-SFT 前后的模型表现。核心创新在于提出指令感知的 Hybrid-Frame 策略，该策略根据输入指令动态调整采样帧数——对视频相关查询使用更多帧，对图像相关查询使用较少帧，从而在单次推理中实现差异化的计算资源分配。

【实验结果 / Results】
实验揭示了一个一致模式：Video-SFT 可靠提升视频基准测试性能，但对静态图像基准测试的提升有限甚至导致性能下降。增加采样帧数通常改善视频性能，却无法可靠提升图像性能。Hybrid-Frame 策略部分缓解了这种权衡，在保持视频理解能力的同时减少了对空间理解的损害。

【应用价值 / Applications】
该研究为 MLLMs 的联合图像-视频训练提供了重要指导，提示开发者 Video-SFT 并非"免费的午餐"。提出的 Hybrid-Frame 策略可直接应用于实际部署，帮助模型在视频理解和图像理解任务间取得更好平衡，对需要同时处理静态和动态视觉内容的多模态应用（如视频问答、视觉指令遵循系统）具有直接参考价值。
