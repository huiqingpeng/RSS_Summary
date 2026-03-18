---
title: "DiG: Differential Grounding for Enhancing Fine-Grained Perception in Multimodal Large Language Model"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.12633"
published: "2026-03-18"
summarized: "2026-03-18T18:31:37.677019"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DiG（Differential Grounding），一种新颖的代理任务框架，通过让多模态大语言模型识别和定位相似图像对之间的所有差异来提升细粒度视觉感知能力，且无需预先知道差异数量。研究开发了基于3D渲染的自动化数据生成管道，以支持可扩展训练，并采用课程学习策略从单差异到多差异逐步增加复杂度。实验表明，DiG显著提升了模型在多种视觉感知基准上的性能，且所学技能可有效迁移到RefCOCO等下游任务。

【方法概述 / Method】
DiG采用"找不同"作为核心代理任务，使MLLM通过对比相似图像对来学习细粒度感知；配合基于3D渲染的自动化数据生成系统，可精确控制并生成包含可控差异的高质量图像对；同时引入课程学习机制，通过渐进式增加差异数量来缓解差异信号的稀疏性问题，实现稳定优化。

【实验结果 / Results】
DiG在多个视觉感知基准上显著提升了模型性能，包括细粒度感知任务和标准下游任务；具体在指代表达理解基准RefCOCO、RefCOCO+、RefCOCOg上均取得明显提升，同时泛化能力在通用多模态感知基准上也得到验证；研究表明差异定位技能可有效迁移至各类下游视觉推理任务。

【应用价值 / Applications】
该研究为提升多模态大语言模型的细粒度视觉理解能力提供了可扩展的训练范式，适用于需要精确空间推理和细节感知的场景，如视觉问答、图像编辑指令跟随、机器人视觉导航等；自动化数据生成管道降低了高质量训练数据的获取成本，使该方法具有较强的实用推广价值。
