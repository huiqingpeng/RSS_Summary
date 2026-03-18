---
title: "Revisiting RGBT Tracking Benchmarks from the Perspective of Modality Validity: A New Benchmark, Problem, and Solution"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2405.00168"
published: "2026-03-18"
summarized: "2026-03-18T18:24:42.221630"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文指出现有RGBT跟踪基准大多采集于常规场景，缺乏对多模态保证（MMW）场景（如夜间、恶劣天气）的代表性，导致在这些关键场景下跟踪失败。为此，作者提出了首个考虑模态有效性的新基准MV-RGBT，专门采集于RGB或TIR模态失效的极端条件，并据此划分为两个子集。此外，论文提出了"何时融合"的新问题，并设计了基于混合专家模型的解决方案MoETrack，实验表明融合并非总是有益，尤其在MMW场景下。

【方法概述 / Method】

论文提出了MoETrack方法，采用混合专家（Mixture of Experts）架构，其中每个专家独立生成跟踪结果并输出置信度分数，通过置信度机制动态决定是否进行模态融合，从而自适应地处理模态有效性问题。该方法能够根据场景条件灵活选择单模态跟踪或融合策略，实现了"何时融合"的智能决策。

【实验结果 / Results】

MoETrack在多个基准数据集上取得了最先进的性能，包括新提出的MV-RGBT、GTOT和LasHeR。实验结果揭示了重要发现：在MMW场景下，盲目融合反而会导致性能下降，而基于置信度的选择性融合策略更为有效。MV-RGBT基准的多样性（36个目标类别、19种场景）也验证了其推动RGBT跟踪发展的潜力。

【应用价值 / Applications】

该研究对自动驾驶、安防监控、无人机跟踪等需要在全天候、全时段工作的实际系统具有重要价值，特别是在夜间、强光、雾霾、雨雪等恶劣成像条件下。MV-RGBT基准和MoETrack方法为开发更鲁棒的多模态跟踪系统提供了理论指导和评估工具，有助于推动RGBT跟踪技术在真实复杂环境中的落地应用。
