---
title: "AVERY: Intent-Driven Adaptive VLM Split Computing via Embodied Self-Awareness for Efficient Disaster Response Systems"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2511.18151"
published: "2026-03-31"
summarized: "2026-04-01T07:17:33.261272"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出AVERY，一种面向灾难响应系统的意图驱动自适应视觉语言模型（VLM）分割计算框架。针对无人机在灾难场景中需要复杂语义推理但受限于高资源消耗和网络不稳定的问题，AVERY将操作员意图作为一级系统目标，通过功能认知启发的双流分割设计（高频低分辨率Context流与低频高保真Insight流），实现层次化分割策略。实验表明，AVERY在动态网络条件下相比原始图像压缩提升11.2%准确率，比全边缘执行降低93.98%能耗，且动态适应时平均准确率仅比静态高精度基线低0.75%。

【方法概述 / Method】
AVERY采用功能认知启发的双流分割架构替代传统的深度维度分割：Context流提供高频低分辨率的实时态势感知，Insight流提供低频高保真的深度分析。系统通过轻量级自感知机载控制器，实时监测网络条件和操作员意图，从预训练压缩模型库中动态选择模型，在运行时导航准确率-吞吐量权衡。

【实验结果 / Results】
使用LISA-7B模型在边缘-云环境下进行波动网络条件测试，AVERY相比原始图像压缩实现11.2%的准确率提升；相比全边缘执行实现93.98%的能耗降低；在动态适应过程中，平均准确率与静态高精度基线的差距控制在0.75%以内。

【应用价值 / Applications】
AVERY适用于灾难响应场景中的无人机智能系统，能够在带宽受限、网络不稳定的极端环境下，为操作员提供实时可查询的智能分析能力。该框架通过自适应资源分配支持多样化任务需求（如广域态势监控与精确空间定位调查），显著提升任务效率，对紧急救援、灾害评估等关键应用具有重要价值。
