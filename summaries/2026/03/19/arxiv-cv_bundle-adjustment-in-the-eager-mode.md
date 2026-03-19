---
title: "Bundle Adjustment in the Eager Mode"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2409.12190"
published: "2026-03-19"
summarized: "2026-03-19T17:05:08.926475"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对传统C++束调整（BA）库（如GTSAM、g²o、Ceres Solver）与现代深度学习框架（如PyTorch）缺乏原生集成的问题，提出了一种eager-mode BA库。该库通过稀疏感知自动微分设计和GPU加速稀疏操作，实现了与PyTorch的无缝集成，在多个基准测试上相比传统库获得了18.5×至23×的平均加速比，同时保持了灵活性和易调试性。

【方法概述 / Method】
论文采用eager执行模式构建BA库，核心创新包括：稀疏感知自动微分设计以高效处理BA问题的稀疏结构，以及专为二阶优化设计的GPU加速稀疏操作。该方法充分利用PyTorch的动态计算图特性，实现了BA与深度学习模块的端到端可微分集成。

【实验结果 / Results】
实验表明，该eager-mode BA库在GPU上展现出显著的运行时效率优势：相比GTSAM平均加速18.5×，相比g²o加速22×，相比Ceres Solver加速23×。这些性能提升在多个标准BA基准测试中得到验证，证明了该方法在大规模优化问题上的可扩展性。

【应用价值 / Applications】
该研究为SLAM、增强现实（AR）和摄影测量等机器人应用提供了高效的BA工具，特别适用于需要联合优化传统几何约束与深度学习感知模块的现代智能系统。其原生PyTorch集成特性降低了开发门槛，支持快速原型设计和端到端训练，推动了几何优化与深度学习的深度融合。
