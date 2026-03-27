---
title: "AVControl: Efficient Framework for Training Audio-Visual Controls"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24793"
published: "2026-03-27"
summarized: "2026-03-28T07:16:43.986399"
ai_provider: "openai"
---

【论文摘要 / Abstract】
AVControl 是一个基于 LTX-2 音视频基础模型的高效可扩展框架，通过为每种控制模态训练独立的 LoRA 适配器，并利用并行画布（parallel canvas）将参考信号作为额外 token 注入注意力层，实现了无需修改底层架构的多模态控制。该框架在 VACE Benchmark 的深度/姿态引导生成、修复、外扩等任务上超越所有基线方法，并首次为联合生成模型提供了模块化的音视频控制。每种模态仅需小数据集和数百至数千步训练即可收敛，计算和数据效率远超单体模型方案。

【方法概述 / Method】
AVControl 采用 LoRA（Low-Rank Adaptation）微调策略，在冻结的 LTX-2 基础模型上为每种控制模态（深度、姿态、相机轨迹、音频变换等）训练独立的轻量级适配器。核心创新是"并行画布"机制：将控制信号编码为与主视频序列并行的额外 token 序列，通过注意力层实现条件注入，避免了复杂的架构改动。研究发现直接将图像上下文方法扩展到视频会导致结构控制失败，而并行画布有效解决了这一问题。

【实验结果 / Results】
在 VACE Benchmark 上，AVControl 在深度引导生成、姿态引导生成、视频修复（inpainting）和外扩（outpainting）四项任务中均优于所有评估基线；在相机控制和音视频基准测试上取得有竞争力的结果。训练效率显著：每个模态仅需小数据集，收敛步数仅为数百至数千步，远低于单体替代方案的训练预算。

【应用价值 / Applications】
AVControl 适用于需要灵活多模态控制的视频/音频生成场景，如影视制作中的相机轨迹规划、人物动作控制、深度构图指导，以及音频驱动的视频编辑等。其模块化设计允许用户按需组合独立训练的 LoRA（如同时启用深度+姿态+音频控制），大幅降低新模态接入成本，为专业内容创作和交互式生成工具提供了高效可扩展的技术基础。项目已开源代码和预训练 LoRA 检查点。
