---
title: "Diffusion-DRF: Free, Rich, and Differentiable Reward for Video Diffusion Fine-Tuning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.04153"
published: "2026-03-18"
summarized: "2026-03-18T18:32:01.040223"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出Diffusion-DRF，一种用于视频扩散模型微调的新型奖励框架。该框架利用冻结的现成视觉-语言模型（VLM）作为评判器，无需训练额外的奖励模型或收集偏好数据集；通过将用户提示分解为多维度问题并生成自由形式的密集VQA解释查询，提供信息丰富的多维反馈；通过直接可微优化实现稳定的奖励微调，在VBench-2.0上比当前最优的Flow-GRPO方法提升4.74%的整体性能。

【方法概述 / Method】
Diffusion-DRF采用冻结的VLM作为评判器替代传统标量奖励模型，将单一文本提示扩展为多维度的视觉问答查询以获取细粒度、可解释的反馈；通过设计可微分的优化目标，直接对VLM生成的密集文本反馈进行梯度优化，避免了强化学习中的奖励稀疏性和信用分配问题。

【实验结果 / Results】
在未见过的VBench-2.0基准测试上，Diffusion-DRF相比最先进的Flow-GRPO方法实现4.74%的整体性能提升；实验表明该方法在定量和定性评估中均取得显著改进，有效缓解了奖励剥削和不稳定优化等问题。

【应用价值 / Applications】
该框架可广泛应用于视频生成模型的对齐微调，降低对昂贵人工偏好标注数据的依赖；其"免费、丰富、可微"的特性使其特别适用于资源受限场景下的视频扩散模型优化，有望推动更高效、可控的视频内容生成工具的发展。
