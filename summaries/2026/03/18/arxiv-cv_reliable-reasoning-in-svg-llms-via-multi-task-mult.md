---
title: "Reliable Reasoning in SVG-LLMs via Multi-Task Multi-Reward Reinforcement Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16189"
published: "2026-03-18"
summarized: "2026-03-18T18:08:11.800366"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CTRL-S（Chain-of-Thought Reinforcement Learning for SVG），一个统一的框架，通过引入思维链机制使模型在SVG生成过程中显式暴露推理过程。研究构建了包含145K样本的高质量数据集SVG-Sophia，涵盖SVG代码优化、文本到SVG和图像到SVG三类任务。通过多奖励优化框架和多任务训练，CTRL-S在任务成功率、SVG代码质量和视觉保真度方面均优于现有方法。

【方法概述 / Method】
CTRL-S采用GRPO（Group Relative Policy Optimization）强化学习算法，设计了包含DINO视觉特征、图文相似度、格式规范性和代码效率的多奖励优化框架。模型被训练生成组级别的结构化SVG代码，以提升结构一致性和视觉保真度，并通过联合多奖励优化与多任务训练系统增强整体生成能力。

【实验结果 / Results】
实验表明，CTRL-S在多个评估维度上均超越现有方法，实现了更高的任务成功率、更优的SVG代码质量以及卓越的视觉保真度。通过显式的思维链推理机制，模型有效解决了传统方法泛化能力有限、代码路径冗余以及缺乏显式推理等问题。

【应用价值 / Applications】
该研究可广泛应用于自动化图形设计、矢量图标生成、UI/UX设计辅助以及教育领域的编程可视化等场景。通过生成高质量、结构化的SVG代码，CTRL-S能够为设计师和开发者提供可靠的智能辅助工具，同时其多任务框架也为其他结构化代码生成任务提供了可迁移的技术范式。
