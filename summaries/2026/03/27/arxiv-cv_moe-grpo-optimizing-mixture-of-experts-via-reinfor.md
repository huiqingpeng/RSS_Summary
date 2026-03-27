---
title: "MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24984"
published: "2026-03-27"
summarized: "2026-03-28T07:19:23.274911"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 MoE-GRPO，一种基于强化学习的专家路由优化框架，用于解决视觉-语言模型（VLMs）中混合专家（MoE）架构的确定性 top-K 路由机制存在的专家选择次优和过拟合问题。该方法将专家选择建模为序列决策问题，采用 Group Relative Policy Optimization（GRPO）进行优化，并引入模态感知路由引导机制提升训练稳定性。实验表明，MoE-GRPO 在多模态图像和视频基准上 consistently 优于标准 top-K 路由及其变体，通过促进专家选择多样性实现了任务级专家特化。

【方法概述 / Method】

MoE-GRPO 将专家路由优化转化为强化学习问题，利用 GRPO 算法让模型通过探索与基于奖励的反馈学习自适应专家路由策略，替代传统的确定性 top-K 选择。此外，该方法设计了模态感知路由引导机制，通过惩罚对特定模态极少激活的专家的探索，增强训练稳定性与效率。

【实验结果 / Results】

在多模态图像和视频基准上的大量实验表明，MoE-GRPO 一致性地超越标准 top-K 路由及其变体；该方法有效促进了专家选择的多样性，缓解了专家过拟合问题，并实现了任务级别的专家特化（task-level expert specialization）。

【应用价值 / Applications】

MoE-GRPO 可广泛应用于大规模视觉-语言模型的高效推理场景，如多模态理解、视频分析等需要降低计算成本同时保持高性能的任务；其强化学习驱动的自适应路由机制为 MoE 架构的优化提供了新范式，有助于推动更具可扩展性和专业化的多模态 AI 系统部署。
