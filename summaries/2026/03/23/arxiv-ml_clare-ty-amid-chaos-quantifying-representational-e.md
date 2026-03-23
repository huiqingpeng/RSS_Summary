---
title: "CLaRE-ty Amid Chaos: Quantifying Representational Entanglement to Predict Ripple Effects in LLM Editing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19297"
published: "2026-03-23"
summarized: "2026-03-24T07:15:48.663991"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出CLaRE，一种轻量级的表示层技术，用于预测大语言模型（LLM）编辑中的"涟漪效应"（ripple effects）——即局部知识修改在隐藏空间中传播的意外行为变化。与基于梯度的方法不同，CLaRE仅利用单个中间层的前向激活来量化事实间的纠缠关系，无需昂贵的反向传播。研究构建了包含11,427个事实的大规模语料库，并计算了多模型的纠缠图，实现了62.2%的Spearman相关性提升，同时速度提升2.74倍、显存减少2.85倍。

【方法概述 / Method】

CLaRE通过分析LLM单个中间层的前向激活，量化不同事实在表示空间中的纠缠程度（entanglement），从而预测编辑某一事实对其他事实的潜在影响。该方法完全基于前向传播，避免了传统梯度方法所需的反向传播计算开销，通过构建大规模纠缠图来捕捉知识编辑在表示空间中的传播路径。

【实验结果 / Results】

在11,427个事实的大规模语料库上，CLaRE与基线方法相比，在预测涟漪效应的Spearman相关性上平均提升62.2%；计算效率方面，速度提升2.74倍，峰值GPU显存使用降低2.85倍，且存储需求仅为基线的一小部分。研究还为多个模型构建了可复用的纠缠图，支持系统性的模型编辑分析。

【应用价值 / Applications】

CLaRE的实际应用包括：构建更强的模型编辑保留集（preservation sets）以减少副作用、提供可审计的编辑追踪路径、支持高效的红队测试（red-teaming）以及可扩展的编辑后评估。该方法为LLM知识更新提供了一种高效、低成本的可靠性保障工具，特别适用于需要频繁更新知识且对安全性要求高的生产环境。
