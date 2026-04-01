---
title: "Differentiable Initialization-Accelerated CPU-GPU Hybrid Combinatorial Scheduling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.28943"
published: "2026-04-01"
summarized: "2026-04-02T07:13:56.781712"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种CPU-GPU混合框架，用于求解整数线性规划（ILP）形式的组合调度问题。该方法创新性地将可微优化与经典ILP求解相结合，利用可微预求解快速生成高质量部分解作为商业求解器（CPLEX、Gurobi）和开源求解器HiGHS的热启动。实验表明，该方法可实现高达10倍的性能提升，最优性差距缩小至<0.1%，首次展示了利用可微优化来初始化精确ILP求解器的可行性。

【方法概述 / Method】
核心方法采用可微预求解（differentiable presolving）技术，在GPU上通过可微优化快速生成高质量的初始部分解，然后将这些解作为热启动（warm-starts）传递给CPU上的传统精确ILP求解器，形成CPU-GPU协同的混合求解架构。

【实验结果 / Results】
在工业级基准测试上的实证结果显示，相比最先进的独立求解器，该方法可实现高达10倍的性能加速，同时将最优性差距控制在0.1%以内，显著提升了早期剪枝效率。

【应用价值 / Applications】
该研究为机器学习基础设施与经典精确优化方法的融合开辟了新途径，可广泛应用于云计算资源调度、供应链优化、生产计划等大规模组合优化场景，为NP-hard调度问题的实际求解提供了兼顾效率与精度的实用方案。
