---
title: "Hallucination Detection in Virtually-Stained Histology: A Latent Space Baseline"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2411.15060"
published: "2026-03-20"
summarized: "2026-03-20T14:14:25.637243"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文首次系统性地形式化了虚拟染色（Virtual Staining, VS）中的幻觉检测问题，并提出了一种可扩展的后验检测方法——神经幻觉前兆（Neural Hallucination Precursor, NHP）。NHP 利用生成器的潜在空间特征来预先标记可能出现的幻觉区域。跨多种VS任务的广泛实验表明，NHP 既有效又稳健。研究还发现，幻觉较少的模型并不一定具有更好的可检测性，揭示了当前VS评估中的关键缺口，并强调了建立幻觉检测基准的必要性。

【方法概述 / Method】
NHP 是一种基于生成器潜在空间的后验检测方法，通过分析扩散模型或生成对抗网络等VS模型内部的潜在表征，识别可能导致幻觉的异常模式。该方法无需重新训练生成模型，可直接部署于现有VS流程中，实现计算高效的实时检测。

【实验结果 / Results】
实验在多种虚拟染色任务上进行验证，证明NHP能够有效检测幻觉且具有良好的跨任务鲁棒性。关键发现是幻觉率与可检测性之间存在解耦现象：生成质量更高（幻觉更少）的模型，其幻觉反而更难被检测到，这对现有仅关注幻觉率的评估范式提出了挑战。

【应用价值 / Applications】
该研究为数字病理学和计算显微镜领域提供了重要的安全保障机制，可在临床诊断工作流程中部署，防止AI生成的虚假组织学特征误导病理学家。同时，研究呼吁建立标准化的幻觉检测基准，推动虚拟染色技术从实验室研究向临床实际应用的转化。
