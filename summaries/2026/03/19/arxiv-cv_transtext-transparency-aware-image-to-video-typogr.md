---
title: "TransText: Transparency Aware Image-to-Video Typography Animation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17944"
published: "2026-03-19"
summarized: "2026-03-19T16:19:12.031596"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了首个将图像到视频模型适配于图层感知文本（字形）动画的方法TransText，解决了动态视觉设计中的关键需求。现有方法通常将透明度编码（alpha通道）作为额外维度附加到RGB空间，需要重建以RGB为中心的变分自编码器（VAE），但高质量透明字形数据稀缺会导致计算成本高且可能破坏大规模RGB语料库学到的语义先验。TransText通过创新的"Alpha-as-RGB"范式，在不修改预训练生成流形的情况下联合建模外观与透明度，实现了高保真透明动画生成。

【方法概述 / Method】
TransText采用Alpha-as-RGB范式，通过潜在空间拼接将alpha通道嵌入为RGB兼容的视觉信号，而非扩展VAE的潜在维度。该方法显式确保RGB与Alpha之间的严格跨模态一致性，同时防止特征纠缠，避免了重新训练VAE带来的计算开销和语义先验损失。

【实验结果 / Results】
实验表明TransText显著优于基线方法，能够生成连贯、高保真的透明动画，并具有多样化、细粒度的视觉效果。该方法有效解决了潜在模式混合问题，在透明字形动画任务上展现出优越的性能和稳定性。

【应用价值 / Applications】
该研究可直接应用于动态视觉设计、视频字幕动画、广告制作和UI/UX动效设计等领域，使设计师能够高效生成具有透明通道的专业级文字动画效果。TransText降低了透明动画生成的技术门槛和计算成本，为数字内容创作行业提供了实用的自动化工具。
