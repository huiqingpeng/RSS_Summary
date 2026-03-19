---
title: "Few-Step Diffusion Sampling Through Instance-Aware Discretizations"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17671"
published: "2026-03-19"
summarized: "2026-03-19T15:15:43.384257"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种实例感知离散化框架，用于改进扩散模型和流匹配模型的少步采样。作者发现现有方法采用全局共享的时间步调度策略，忽略了生成过程中实例特定的复杂性。通过合成数据上的对照实验，他们证明了全局调度在实例特定动态下的次优性，并开发了基于输入相关先验自适应分配时间步的方法，在多种设置下以极低的调优成本持续提升了生成质量。

【方法概述 / Method】
该方法将基于梯度的离散化搜索扩展到条件生成设置，学习时间步分配策略以适应输入相关的先验分布。核心思想是让模型根据每个样本的实例特定动态（instance-specific dynamics）自适应地决定时间步的分配，而非对所有样本使用固定的时间步调度表。

【实验结果 / Results】
实验涵盖了合成数据、像素空间扩散模型、潜在空间图像模型以及视频流匹配模型等多种设置。结果表明，该方法相比训练成本而言仅需边际调优成本（marginal tuning cost），且推理开销可忽略不计（negligible inference overhead），同时持续改善了生成质量。

【应用价值 / Applications】
该研究可广泛应用于需要高效采样的生成式AI场景，包括实时图像生成、视频合成和高分辨率内容创作。通过实现少步高质量采样，该方法能够显著降低扩散模型在实际部署中的计算成本，提升推理效率，对资源受限环境下的生成模型应用具有重要价值。
