---
title: "Refining Few-Step Text-to-Multiview Diffusion via Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.20107"
published: "2026-03-18"
summarized: "2026-03-18T16:17:46.674051"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对少步数文本到多视角（T2MV）扩散模型生成质量不足的问题，提出了MVC-ZigAL强化学习微调框架。该框架通过联合建模所有生成视角的MDP形式化、基于自精炼采样策略的优势学习方法，以及结合拉格朗日对偶的统一RL框架，实现了对单视角保真度和跨视角一致性的平衡优化。实验表明，该方法在少步数T2MV扩散模型上取得了显著的性能提升。

【方法概述 / Method】
MVC-ZigAL框架包含三个核心设计：（1）新型MDP形式化，通过联合视角奖励评估所有生成视角的集体质量；（2）创新的优势学习策略，利用自精炼采样相对于标准采样的性能增益来增强学习信号；（3）统一的RL框架，采用拉格朗日对偶形式进行多视角约束优化，并通过自适应原始-对偶更新与自步阈值课程平衡探索与约束执行。

【实验结果 / Results】
论文未在提供的摘要中给出具体的定量实验结果，但明确指出该方法在少步数T2MV扩散模型上实现了"per-view fidelity"（单视角保真度）和"cross-view consistency"（跨视角一致性）两方面的实质性提升（substantial gains）。代码已开源供复现验证。

【应用价值 / Applications】
该技术可应用于实时3D内容生成、虚拟现实/增强现实场景构建、以及基于文本的3D资产生成等场景，解决了现有少步数方法在生成速度和输出质量之间的权衡难题，为交互式3D设计工具和游戏开发中的快速原型制作提供了高质量的多视角图像生成能力。
