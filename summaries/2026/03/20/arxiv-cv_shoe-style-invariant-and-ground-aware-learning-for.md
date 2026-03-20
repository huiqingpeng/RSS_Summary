---
title: "Shoe Style-Invariant and Ground-Aware Learning for Dense Foot Contact Estimation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.22184"
published: "2026-03-20"
summarized: "2026-03-20T16:15:30.269874"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了首个针对单张RGB图像的密集足部接触估计框架FECO，解决了现有方法仅关注关节级接触、无法捕捉足-地精细交互的问题。针对鞋子外观多样性导致的泛化困难，作者引入鞋子风格对抗训练来学习风格不变特征；针对地面单调外观导致的信息提取困难，设计了基于空间上下文感知的地面特征提取器。实验表明，该方法能够在不同鞋款外观下实现鲁棒的足部接触估计，并有效利用地面信息。

【方法概述 / Method】

该框架采用双分支设计：通过鞋子风格对抗训练（shoe style adversarial training）分离鞋子外观与接触估计相关的特征，强制模型学习风格无关的接触表征；同时引入地面特征提取器（ground feature extractor），利用空间上下文关系捕捉地面属性，增强对单调地面的感知能力。

【实验结果 / Results】

论文未在提供的摘要中给出具体的定量实验结果和性能指标数值，但明确指出所提方法实现了"robust foot contact estimation regardless of shoe appearance"（不受鞋子外观影响的鲁棒足部接触估计），并能有效利用地面信息，暗示在跨鞋款泛化和接触估计精度方面取得了优于现有方法的性能。

【应用价值 / Applications】

该研究可广泛应用于人体运动分析、虚拟现实/增强现实中的真实感角色动画、机器人步态规划以及体育科学中的生物力学分析等领域，为精确建模人体与环境的物理交互提供了关键技术支撑，有望提升数字人重建和动作捕捉系统的真实感与物理合理性。
