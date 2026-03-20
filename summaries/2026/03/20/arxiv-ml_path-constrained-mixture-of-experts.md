---
title: "Path-Constrained Mixture-of-Experts"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18297"
published: "2026-03-20"
summarized: "2026-03-20T12:10:09.153802"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Path-Constrained Mixture-of-Experts（PathMoE），通过跨连续层共享路由器参数来约束传统MoE中指数级增长的专家路径空间（N^L）。实验表明，该方法在0.9B和16B参数模型上均优于独立路由，同时无需辅助负载均衡损失。分析发现，相同路径的token会按语言功能自然聚类，PathMoE能产生更集中的分组、更好的跨层一致性和更强的路由扰动鲁棒性。

【方法概述 / Method】
PathMoE的核心创新是跨层参数共享的路由机制，替代了传统MoE中每层独立选择专家的方式。这种约束将可能的专家路径空间从指数级（N^L）大幅降低，使模型能够在有限的训练数据下更有效地学习有意义的路径结构。

【实验结果 / Results】
在0.9B和16B两种规模的模型上，PathMoE在困惑度和下游任务上均持续优于独立路由基线。该方法完全消除了对辅助负载均衡损失的需求，且展现出更强的路由稳定性——对路由扰动的鲁棒性显著提升。

【应用价值 / Applications】
PathMoE为大规模语言模型的高效训练与部署提供了新思路，特别适用于需要稳定、可解释专家路径的场景。其路径约束机制有助于构建更具结构化、功能专化的专家系统，可广泛应用于自然语言理解、生成任务及多模态大模型的高效扩展。
