---
title: "Generate Any Scene: Scene Graph Driven Data Synthesis for Visual Generation Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2412.08221"
published: "2026-03-18"
summarized: "2026-03-18T17:09:21.997897"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了"Generate Any Scene"（GAS），一个基于场景图的数据合成引擎，通过系统枚举对象、属性和关系的组合来生成多样化的视觉场景。该引擎将场景图转换为用于文生图/文生视频的提示词，并生成视觉问答对以实现自动化的语义对齐评估。研究展示了GAS在三个关键应用中的有效性：自提升训练框架、专有模型知识蒸馏到低成本的奖励模型训练，显著提升了组合泛化能力和语义对齐性能。

【方法概述 / Method】

GAS从结构化的对象、属性和关系分类体系中动态构建复杂度可变的场景图，通过组合采样生成涵盖广泛视觉场景的组合阵列。场景图被双向转换为自然语言描述（用于生成模型）和视觉问答对（用于自动评估与奖励建模），形成闭环的数据合成与验证流程。

【实验结果 / Results】

在自提升框架中，Stable Diffusion v1.5平均提升4%并超越CC3M微调基线；知识蒸馏仅用不到800条合成描述词，TIFA分数在组合和困难概念生成上提升10%；基于GRPO算法训练的奖励模型使SimpleAR-0.5B-SFT在DPG-Bench上超越CLIP方法5%。

【应用价值 / Applications】

GAS为视觉生成模型提供了可扩展的高质量合成数据解决方案，适用于需要精确语义控制的文生图/视频训练、低成本模型能力迁移，以及内容审核等下游任务——通过合成困难案例训练模型识别有害内容，解决了真实数据标注稀缺和隐私敏感的挑战。
