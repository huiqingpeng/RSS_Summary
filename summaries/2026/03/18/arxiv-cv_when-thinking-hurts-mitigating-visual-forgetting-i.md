---
title: "When Thinking Hurts: Mitigating Visual Forgetting in Video Reasoning via Frame Repetition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16256"
published: "2026-03-18"
summarized: "2026-03-18T18:09:42.605793"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文揭示了多模态大语言模型（MLLMs）在视频问答任务中采用思维链（CoT）推理时出现的"视觉锚点漂移"问题——即模型过度依赖自生成的文本而忽视视觉输入，导致性能下降和幻觉现象。为此，作者提出了FrameRepeat框架，通过轻量级的重复评分模块自动识别需要强化的关键帧，并设计了"Add-One-In（AOI）"训练策略，利用MLLM输出概率生成监督信号来训练帧评分网络。实验表明，该方法在多个模型和数据集上均有效且具有良好的泛化能力。

【方法概述 / Method】
FrameRepeat框架核心包含两个组件：（1）重复评分模块，用于评估视频中各帧的重要性并决定是否需要重复输入；（2）AOI训练策略，通过对比"原始帧序列"与"增加一帧重复"后的MLLM输出概率变化，自动生成重复增益的监督信号，无需人工标注即可训练帧评分网络。

【实验结果 / Results】
实验在多个视频问答数据集和不同架构的Video-LLM上进行验证，结果表明FrameRepeat能够有效缓解视觉遗忘问题，提升推理准确性；同时，该方法展现出良好的跨模型泛化能力，且相比现有需要特定机制重新关注视觉输入的方法，训练成本显著降低。

【应用价值 / Applications】
该研究为视频理解领域的MLLM推理优化提供了轻量级、可迁移的解决方案，适用于需要长程视频推理的问答系统、视频分析平台等场景；其自动化的监督信号生成方式也为其他多模态任务中缓解模态遗忘问题提供了可借鉴的技术路径。
