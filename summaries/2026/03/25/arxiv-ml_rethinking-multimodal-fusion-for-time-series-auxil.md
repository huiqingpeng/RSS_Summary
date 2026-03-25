---
title: "Rethinking Multimodal Fusion for Time Series: Auxiliary Modalities Need Constrained Fusion"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22372"
published: "2026-03-25"
summarized: "2026-03-26T07:13:57.558042"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文揭示了多模态时间序列预测中的一个关键问题：简单的融合策略（如直接相加或拼接）往往导致辅助模态引入无关信息，反而使多模态模型性能劣于单模态模型。为此，作者系统探索了约束融合方法，并提出了Controlled Fusion Adapter（CFA）——一种即插即用的轻量级模块，通过低秩适配器过滤无关文本信息，实现与动态时间序列特征对齐的受控跨模态交互。超过2万次实验验证了约束融合方法及CFA在多种数据集和模型架构上的 consistently 优越性。

【方法概述 / Method】
本文首先对比分析了朴素融合（naive fusion）与多种约束融合策略（如门控机制、注意力筛选等）的效果，进而提出CFA模块。CFA采用低秩适配器（low-rank adapters）对文本表征进行预处理，在融合前过滤与时间序列动态不相关的信息，且无需修改时间序列主干网络即可实现可控的跨模态交互。

【实验结果 / Results】
作者在多个时间序列数据集和文本/时间序列模型组合上进行了超过20,000组实验，结果表明约束融合方法 consistently 优于朴素融合基线；CFA作为即插即用模块，在保持计算开销可控的同时，显著提升了预测性能，展现出良好的跨架构泛化能力。

【应用价值 / Applications】
该研究为金融预测、能源负荷预测、交通流量预测等需要时间序列与文本（如新闻、社交媒体）或视觉信息融合的场景提供了通用且高效的解决方案。CFA的即插即用特性使其可快速集成至现有预测系统，帮助实践者避免多模态融合中的"噪声引入"陷阱，提升模型鲁棒性与预测准确性。
