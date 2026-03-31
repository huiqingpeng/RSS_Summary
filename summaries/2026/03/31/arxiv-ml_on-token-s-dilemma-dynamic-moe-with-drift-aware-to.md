---
title: "On Token's Dilemma: Dynamic MoE with Drift-Aware Token Assignment for Continual Learning of Large Vision Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27481"
published: "2026-03-31"
summarized: "2026-04-01T07:24:56.894865"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对大型视觉语言模型（LVLMs）的持续学习问题，提出了一种动态混合专家（MoE）框架LLaVA-DyMoE。研究揭示了"token困境"现象：新任务数据中的模糊token和旧任务token对新专家的学习贡献极小，却因路由分配不明确而导致灾难性遗忘。该框架通过漂移感知token分配策略，有效缓解了路由漂移引起的遗忘问题，相比基线方法实现了超过7%的最终平均准确率提升和12%的遗忘率降低。

【方法概述 / Method】
LLaVA-DyMoE采用动态MoE架构，通过分析token的路由分数分布来表征token类型（新token、模糊token、旧token）。核心机制包括：token级分配引导策略，将模糊token和旧token导向旧专家以保留已建立的路由模式；以及互补的路由分数正则化，强制实现专家组分离并促进新专家专业化。

【实验结果 / Results】
实验结果表明，该方法显著缓解了路由漂移导致的遗忘问题，在多个持续学习基准上取得了超过7%的最终平均准确率提升，同时将遗忘率降低了12%。这些性能增益验证了漂移感知token分配策略在保持旧知识的同时有效学习新任务的能力。

【应用价值 / Applications】
该研究为大型视觉语言模型的持续部署和增量更新提供了实用解决方案，适用于需要模型不断适应新任务场景而不遗忘历史知识的应用，如多模态对话系统、视觉问答平台的持续优化，以及需要长期学习的智能助手等实际场景。
