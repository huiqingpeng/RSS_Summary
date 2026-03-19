---
title: "AR-CoPO: Align Autoregressive Video Generation with Contrastive Policy Optimization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17461"
published: "2026-03-19"
summarized: "2026-03-19T15:11:20.347523"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了AR-CoPO（自回归对比策略优化）框架，用于解决流式自回归视频生成模型在基于人类反馈的强化学习（RLHF）对齐中的难题。现有SDE-based GRPO方法在少步ODE和一致性模型采样器场景下效果不佳，因其短程、低随机性的轨迹对初始化噪声高度敏感。AR-CoPO通过分块级对齐机制（forking机制构建邻域候选）和半在线策略训练策略，实现了跨域生成质量的提升，并证明其带来了真正的对齐效果而非奖励黑客行为。

【方法概述 / Method】
AR-CoPO将Neighbor GRPO的对比视角适配到流式自回归生成中，通过forking机制在随机选择的分块处构建邻域候选序列，分配序列级奖励并进行局部化GRPO更新。此外，提出半在线策略训练策略，结合在线策略探索与参考回放缓冲区的利用，以平衡探索与开发。

【实验结果 / Results】
在Self-Forcing基准上的实验表明，AR-CoPO相比基线方法在域外泛化能力和域内人类偏好对齐方面均有显著提升，验证了该方法实现了真正的对齐效果而非简单的奖励过拟合。

【应用价值 / Applications】
该研究为低延迟、高质量的自回归视频生成模型提供了有效的RLHF对齐方案，可广泛应用于实时视频生成、交互式内容创作等需要流式生成的场景，推动视频生成模型更好地符合人类偏好和实际应用需求。
