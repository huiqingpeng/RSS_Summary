---
title: "SignAgent: Agentic LLMs for Linguistically-Grounded Sign Language Annotation and Dataset Curation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19059"
published: "2026-03-20"
summarized: "2026-03-20T16:03:56.344594"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了SignAgent，一种基于智能体的大型语言模型（LLM）框架，用于可扩展的、语言学基础的手语标注和数据集整理。该框架通过SignAgent Orchestrator（一个协调多种语言学工具的推理型LLM）和SignGraph（一个提供词汇和语言学基础的知识型LLM），解决了传统计算方法忽略语言学细节以及人工标注成本高昂的问题。实验表明，该智能体方法在伪标注（Pseudo-gloss Annotation）和ID标注（ID Glossing）两项下游任务中表现优异，能够实现大规模、语音学感知的数据标注和管理。

【方法概述 / Method】

SignAgent采用双组件架构：SignAgent Orchestrator作为中央推理引擎，协调多模态证据提取、约束满足和序列排序等语言学工具；SignGraph作为知识基础模块，整合手语词汇和语言学知识以提供语义和语音学约束。该框架通过多智能体协作，将视觉证据与语言学规则相结合，实现对手语序列的推理式标注。

【实验结果 / Results】

论文在两个下游任务上评估了框架性能：在伪标注任务中，智能体利用多模态证据进行约束分配，提取并排序合适的词汇标签；在ID标注任务中，智能体通过推理视觉相似性和语音学重叠来检测和优化视觉聚类，正确识别和分组词汇变体。结果表明，该智能体方法在大规模语言学感知数据标注和整理方面取得了强劲性能。

【应用价值 / Applications】

SignAgent可显著降低手语数据集构建的成本和时间，推动大规模、语言学丰富的手语资源开发，对计算手语学研究和手语识别技术的发展具有重要价值。该框架的模块化设计使其可扩展至其他低资源语言和需要语言学专家知识的标注任务，为多模态语言资源建设提供了可复用的技术范式。
