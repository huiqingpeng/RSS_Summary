---
title: "MSRAMIE: Multimodal Structured Reasoning Agent for Multi-instruction Image Editing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16967"
published: "2026-03-19"
summarized: "2026-03-19T15:03:19.530663"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MSRAMIE，一种基于多模态大语言模型（MLLM）的无训练智能体框架，用于解决多指令图像编辑任务。该框架通过结构化多模态推理，将复杂指令分解为多个编辑步骤，实现了状态转换、跨步骤信息聚合和原始输入召回。实验表明，随着指令复杂度增加，MSRAMIE可将指令遵循率提升超过15%，单次完成所有修改的概率提升超过100%，同时保持感知质量和视觉一致性。

【方法概述 / Method】
MSRAMIE采用MLLM驱动的"Instructor-Actor"架构，通过迭代交互处理多指令任务。核心创新在于提出"状态树（Tree-of-States）"和"引用图（Graph-of-References）"的新型推理拓扑结构，实现系统化的图像编辑空间探索和渐进式输出优化。该框架将现有编辑模型作为即插即用组件，无需重新训练即可适配复杂场景。

【实验结果 / Results】
实验结果显示，MSRAMIE在处理复杂多指令时显著优于基线方法：指令遵循准确率提升超15%，单次完成全部修改的成功率提升超100%。此外，该方法在提升编辑完成度的同时，有效保持了生成图像的感知质量和视觉一致性，且推理拓扑可视化提供了可解释和可控的决策路径。

【应用价值 / Applications】
MSRAMIE适用于需要复杂多步骤图像编辑的实际场景，如专业图像设计、广告内容生成和视觉创意制作等领域。其无训练特性使其能够快速集成现有编辑模型，降低数据收集和模型重训练成本；可视化的推理拓扑则为用户提供了透明、可控的编辑流程，增强人机协作效率。
