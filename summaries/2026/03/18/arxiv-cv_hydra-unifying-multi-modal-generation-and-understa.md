---
title: "HYDRA: Unifying Multi-modal Generation and Understanding via Representation-Harmonized Tokenization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15228"
published: "2026-03-18"
summarized: "2026-03-18T19:05:10.729978"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出HYDRA框架，旨在解决统一多模态模型中视觉理解与生成任务之间的表征鸿沟问题。核心创新是HYDRA-TOK，一种表征和谐的纯ViT分词器，通过生成-语义瓶颈（GSB）实现从结构保留的Gen-ViT到语义编码的Sem-ViT的渐进式转换。实验表明，HYDRA在视觉重建（rFID 0.08）和生成任务（GenEval 0.86、DPG-Bench 86.4）上达到SOTA，同时在8项理解基准上平均超越先前原生统一多模态模型10.0个百分点。

【方法概述 / Method】

HYDRA-TOK采用渐进式学习架构，首先通过Gen-ViT捕获保留结构的视觉基元，然后经GSB模块将特征压缩至低维空间过滤噪声以支持鲁棒合成，再恢复维度以赋能复杂语义理解。整个框架在单一参数空间内原生集成感知与生成，无需解耦编码器或离散量化。

【实验结果 / Results】

HYDRA在视觉重建任务上实现rFID 0.08的优异指标，在生成评估中取得GenEval 0.86、DPG-Bench 86.4和WISE 0.53的顶尖成绩。在理解任务方面，相比先前原生统一多模态模型，在8项挑战性基准上平均提升10.0个百分点，首次实现生成与理解的双重SOTA。

【应用价值 / Applications】

该研究为统一多模态AI系统提供了新的技术范式，可广泛应用于需要同时具备视觉内容生成与语义理解能力的场景，如智能图像编辑、交互式视觉问答、多模态内容创作等，有望降低多任务模型的部署成本并提升跨任务协同效率。
