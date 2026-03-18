---
title: "InViC: Intent-aware Visual Cues for Medical Visual Question Answering"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16372"
published: "2026-03-18"
summarized: "2026-03-18T18:12:01.429530"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对医学视觉问答（Med-VQA）中多模态大语言模型（MLLMs）存在的"捷径回答"问题——即依赖语言先验或数据集偏见而非视觉证据生成答案——提出了InViC框架。该框架通过引入意图感知的视觉线索（Intent-aware Visual Cues），将密集视觉令牌蒸馏为与问题相关的紧凑线索令牌，作为结构化视觉中介注入LLM解码器。配合两阶段瓶颈式微调策略，InViC在三个公开医学VQA基准上显著提升了模型对视觉证据的关注度和回答可信度。

【方法概述 / Method】

InViC的核心是**线索令牌提取（CTE）模块**，该模块基于问题条件将图像的密集视觉令牌压缩为K个紧凑的线索令牌；同时设计**两阶段微调策略**：第一阶段使用注意力掩码阻断LLM对原始视觉特征的直接访问，强制所有视觉信息通过线索路径传递；第二阶段恢复标准因果注意力，训练LLM联合利用视觉令牌和线索令牌。

【实验结果 / Results】

InViC在VQA-RAD、SLAKE和ImageCLEF VQA-Med 2019三个医学VQA基准上进行了评估，覆盖多种代表性MLLM架构。实验表明，InViC相较于零样本推理和标准LoRA微调均实现了一致性提升，验证了意图感知视觉线索结合瓶颈训练策略在增强医学VQA可信度方面的有效性。

【应用价值 / Applications】

InViC作为轻量级即插即用框架，可直接集成至现有医学多模态大模型中，提升其在临床影像解读中的可靠性；特别适用于需要精细视觉证据的医学诊断场景，如X光片、CT或MRI影像的自动问答分析，有助于减少因模型忽视关键影像特征而导致的临床误判风险。
