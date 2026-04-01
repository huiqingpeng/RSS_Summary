---
title: "Derived Fields Preserve Fine-Scale Detail in Budgeted Neural Simulators"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29224"
published: "2026-04-01"
summarized: "2026-04-02T07:16:32.297249"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了在固定存储预算下进行细尺度保真神经模拟的挑战。作者发现，在粗化-量化-解码流程中，原始场（primitive fields）和导出场（derived fields）在相同算子下会经历系统不同的频带保留失真。基于此观察，作者提出了导出场优化框架（DerivOpt），通过选择携带哪些物理场以及如何分配存储预算来优化状态设计。实验表明，DerivOpt在PDEBench时间依赖前向子集上不仅提升了平均rollout nRMSE，还在细尺度保真度上显著优于强基线方法，且增益在输入阶段即已显现。

【方法概述 / Method】

作者采用理论分析与实证验证相结合的方法：首先在周期性不可压缩Navier-Stokes设置中分析原始场与导出场的频谱失真特性，建立校准信道模型；然后提出DerivOpt框架，将状态设计建模为在给定存储预算下选择携带场类型及分配通道位宽的优化问题，以最大化保留细尺度信息。

【实验结果 / Results】

在PDEBench完整时间依赖前向子集上的实验显示，DerivOpt在汇总的平均rollout nRMSE指标上取得提升，更重要的是在细尺度保真度上展现出决定性优势。关键发现是：性能增益在输入阶段（rollout学习开始前）即已可见，表明携带状态设计是紧存储预算下的主导瓶颈。

【应用价值 / Applications】

该研究为计算资源受限场景下的科学模拟（如气候建模、流体力学仿真）提供了新的优化维度，可直接应用于需要高效压缩存储神经模拟状态的实际系统。研究结论强调状态设计应与架构、损失函数和rollout策略并列为核心设计轴，对推动预算受限神经模拟器的工程实践具有重要指导意义。
