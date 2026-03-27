---
title: "Accelerating Physics-Based Electromigration Analysis via Rational Krylov Subspaces"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2602.00330"
published: "2026-03-27"
summarized: "2026-03-28T07:09:07.557846"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对纳米级VLSI互连中的电迁移（EM）应力演化分析计算成本高昂的问题，提出了两种基于有理Krylov子空间降阶的快速EM应力分析技术。与传统Krylov方法在零频率处展开不同，有理Krylov方法可在选定时间常数处展开，直接对齐成核时间和稳态时间等关键指标。实验表明，所提方法仅需4-6阶Krylov阶数即可实现亚0.1%的成核时间和电阻变化预测误差，同时获得20-500倍加速，而标准扩展Krylov方法需要50阶以上仍产生10-20%的成核时间误差。

【方法概述 / Method】

本文开发了两种互补框架：频域扩展有理Krylov方法（ExtRaKrylovEM）和时域有理Krylov指数积分方法（EiRaKrylovEM）。核心创新在于利用有理Krylov子空间在特定"偏移时间"（shift time）处进行模型降阶，而非传统方法在零频率处展开；并引入坐标下降优化策略自动确定最优降阶阶数和偏移时间，以同时优化成核阶段和成核后稳态阶段的分析精度。

【实验结果 / Results】

在合成结构和工业级电源网络上的实验表明，所提方法以仅4-6阶Krylov阶数实现了亚0.1%的成核时间和电阻变化预测误差，同时获得20-500倍的速度提升。相比之下，标准扩展Krylov方法需要超过50阶仍产生10-20%的成核时间误差，证明了所提方法在效率和精度上的显著优势。

【应用价值 / Applications】

该方法可广泛应用于EM感知优化和随机EM分析等需要大规模、高精度快速仿真的场景，为先进工艺节点下的VLSI互连可靠性设计提供了高效的计算工具，有助于在芯片设计早期阶段快速评估和优化电迁移可靠性，缩短设计周期并降低因EM失效导致的芯片返工风险。
