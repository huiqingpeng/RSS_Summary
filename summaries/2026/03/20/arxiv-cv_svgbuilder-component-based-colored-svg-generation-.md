---
title: "SVGBuilder: Component-Based Colored SVG Generation with Text-Guided Autoregressive Transformers"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2412.10488"
published: "2026-03-20"
summarized: "2026-03-20T16:10:54.840900"
ai_provider: "openai"
---

【论文摘要 / Abstract】

SVGBuilder 提出了一种基于组件的自回归模型，用于从文本输入生成高质量彩色 SVG 图像，显著降低了传统方法的计算开销。该模型比基于优化的方法快达 604 倍，同时发布了首个大规模彩色 SVG 数据集 ColorSVG-100K（包含 10 万张图形）以填补现有数据集的空白。实验表明，SVGBuilder 在生成复杂 SVG 图形的效率和质量方面均优于现有最先进模型。

【方法概述 / Method】

SVGBuilder 采用组件化的设计思路，模仿人类设计师使用组件工具的工作流程，通过文本引导的自回归 Transformer 架构生成彩色 SVG。该方法将 SVG 生成分解为组件级别的序列预测任务，避免了传统优化方法的高计算成本。

【实验结果 / Results】

SVGBuilder 在生成速度上实现了 604 倍的提升，相比传统基于优化的 SVG 生成方法大幅降低了计算开销。在 ColorSVG-100K 数据集上的评估显示，该模型在实用应用场景中展现出优于现有最先进模型的性能，能够高效生成复杂的彩色 SVG 图形。

【应用价值 / Applications】

SVGBuilder 可广泛应用于需要快速生成可缩放矢量图形的场景，如网页设计、图标生成、数据可视化、动画制作和交互式图形开发等领域。其高效的生成能力和对颜色信息的支持，使其特别适合实时图形生成工具和自动化设计工作流的集成。
