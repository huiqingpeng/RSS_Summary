---
title: "Toward Phonology-Guided Sign Language Motion Generation: A Diffusion Baseline and Conditioning Analysis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17388"
published: "2026-03-19"
summarized: "2026-03-19T15:09:56.221575"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对文本驱动的3D手语动作生成任务，提出了一种基于扩散模型的强基线方法，并系统研究了音系属性（如手形、位置和动作）条件化对生成质量的影响。研究发现，将符号化的ASL-LEX 2.0标注转换为自然语言是使用CLIP编码器进行有效属性条件化的必要条件，而T5编码器对此不敏感。最佳变体（CLIP配合映射后的自然语言属性）在所有指标上均超越了当前最先进的CVAE方法SignAvatar，凸显了输入表示对文本编码器条件化的关键作用。

【方法概述 / Method】
作者采用基于Human Motion MDM的扩散模型架构，以SMPL-X参数化人体表示生成3D身体动作。研究设计了系统的条件化分析框架，对比测试了两种文本编码器（CLIP与T5）、两种条件化模式（仅 gloss vs. gloss+音系属性）以及两种属性表示格式（符号化 vs. 自然语言），并探索了gloss与音系属性通过独立路径编码的结构化条件化策略。

【实验结果 / Results】
所提出的扩散基线在gloss可区分性指标上显著优于当前最先进的SignAvatar方法。条件化分析表明：CLIP编码器依赖自然语言形式的属性描述才能有效利用音系信息，而T5对符号与自然语言格式均表现稳健。最终最佳配置（CLIP+自然语言映射属性）在所有评估指标上全面超越SignAvatar，验证了结构化多路径条件化的有效性。

【应用价值 / Applications】
该研究为听障人士辅助技术中的高质量手语合成提供了更可靠的生成模型基础，有助于改善人机交互的无障碍体验。研究成果对计算手语学及音系学驱动的动作生成具有方法论指导意义，可推广至多模态虚拟人动画、教育手语词典生成及实时手语翻译系统等应用场景。
