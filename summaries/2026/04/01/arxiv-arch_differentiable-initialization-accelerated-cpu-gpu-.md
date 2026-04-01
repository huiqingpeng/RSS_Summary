---
title: "Differentiable Initialization-Accelerated CPU-GPU Hybrid Combinatorial Scheduling"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.28943"
published: "2026-04-01"
summarized: "2026-04-02T07:11:38.641858"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种CPU-GPU混合框架，用于求解整数线性规划（ILP）形式的组合调度问题。该方法首次将可微优化与经典ILP求解器相结合，利用可微预求解快速生成高质量部分解作为热启动，显著提升了商业求解器（CPLEX、Gurobi）和开源求解器HiGHS的早期剪枝效率。在工业规模基准测试上实现了高达10倍的性能提升，将最优性差距缩小至0.1%以下，为机器学习基础设施与经典精确优化方法的融合开辟了新途径。

【方法概述 / Method】
核心方法采用可微预求解（differentiable presolving）技术，在GPU上快速生成高质量的初始部分解，然后将这些解作为热启动（warm-starts）传递给CPU上的精确ILP求解器。该混合架构充分利用了GPU的并行计算能力进行近似优化，同时保留了CPU上精确求解器的完备性保证。

【实验结果 / Results】
实验在多个工业规模基准测试上进行，结果表明该方法相比最先进的独立求解器可实现高达10倍的加速，同时将最优性差距控制在0.1%以内。该方法与CPLEX、Gurobi和HiGHS等主流求解器均兼容，展现了良好的通用性和可扩展性。

【应用价值 / Applications】
该研究适用于云计算资源调度、供应链优化、生产排程等大规模组合优化场景，能够显著降低精确求解的计算开销。通过桥接机器学习与经典优化方法，为实时决策系统和资源受限环境下的优化问题提供了高效可靠的解决方案框架。
