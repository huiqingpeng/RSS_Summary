---
title: "Persistent Story World Simulation with Continuous Character Customization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16285"
published: "2026-03-18"
summarized: "2026-03-18T18:10:30.288049"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了EverTale，一个用于连续故事角色定制的持久化故事世界模拟器，解决了现有方法在角色定制准确性、语义对齐和新身份持续整合之间难以协同的问题。核心创新包括：All-in-One-World角色整合器实现统一LoRA模块内的连续角色适应；基于MLLM-as-Judge的角色质量门控通过思维链推理确保每次角色适应的保真度；以及角色感知区域聚焦采样策略解决多角色视觉叙事中的身份退化和布局冲突问题。实验表明，EverTale在单角色和多角色故事可视化任务上均优于现有方法。

【方法概述 / Method】
EverTale采用三大核心技术：首先，All-in-One-World Character Integrator将多个角色身份整合到统一的LoRA模块中，避免了传统方法为每个角色单独优化模块的开销；其次，Character Quality Gate利用多模态大语言模型（MLLM）作为评判器，通过思维链推理自动评估角色适应质量，决定是继续下一个角色还是进行额外训练；最后，Character-Aware Region-Focus Sampling策略通过协调局部角色细节与全局场景上下文，高效解决多角色生成中的身份混淆和布局冲突。

【实验结果 / Results】
实验结果表明，EverTale在单角色和多角色故事可视化任务上均显著优于多种对比方法，实现了更准确的字符定制、更好的语义对齐以及更自然的连续身份整合。具体性能指标和定量比较虽未在摘要中详细列出，但强调了该方法在角色保真度和多角色场景协调性方面的优势。

【应用价值 / Applications】
该技术可广泛应用于个性化视觉叙事生成，如定制化儿童绘本、动态漫画创作、游戏剧情过场动画以及虚拟角色IP的持续内容生产。其连续角色定制能力特别适合需要长期运营的故事世界构建，如系列动画、互动小说和元宇宙虚拟环境，能够大幅降低多角色内容创作的人工成本和技术门槛。
