---
title: "Alternating Gradient Flow Utility: A Unified Metric for Structural Pruning and Dynamic Routing in Deep Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.12354"
published: "2026-03-18"
summarized: "2026-03-18T17:16:02.456089"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种基于交替梯度流（Alternating Gradient Flow, AGF）的统一评估指标，用于解决深度网络结构化剪枝和动态路由中的关键问题。研究发现传统启发式指标（如权重幅度或激活感知方法）存在"幅度偏置"，无法保留关键功能路径，而AGF通过绝对特征空间泰勒展开准确捕捉网络的结构"动能效用"。在极端稀疏条件下，AGF成功避免了拓扑相变导致的模型崩溃，并揭示了Vision Transformers中的"稀疏瓶颈"现象。基于这些发现，作者设计了一种混合路由框架，在ImageNet-1K的75%压缩压力下显著优于传统方法，在ImageNet-100动态推理中实现了帕累托最优效率。

【方法概述 / Method】

论文采用解耦的动力学范式，利用绝对特征空间泰勒展开来量化网络组件的AGF效用，替代传统的静态启发式指标。对于动态路由，提出将AGF引导的离线结构搜索与基于零成本物理先验的在线执行相分离的混合框架，通过梯度-幅度解耦分析识别收敛模型中动态信号的信号压缩问题。

【实验结果 / Results】

在ImageNet-1K的75%结构化剪枝压力测试中，AGF有效避免了传统指标（如Wanda、RIA）出现的性能急剧下降至随机采样以下的结构崩溃现象。在ImageNet-100动态推理任务中，混合路由方法将重型专家的使用量减少约50%，估计总体计算成本降至0.92倍，同时保持全模型精度，实现了效率与精度的帕累托最优平衡。

【应用价值 / Applications】

该研究为大规模视觉模型的高效部署提供了统一的评估和优化工具，特别适用于资源受限边缘设备上的模型压缩和自适应推理场景。混合路由框架可广泛应用于需要实时动态调整的视觉Transformer系统，如视频分析、自动驾驶感知等延迟敏感型应用，在显著降低计算成本的同时保证模型性能。
