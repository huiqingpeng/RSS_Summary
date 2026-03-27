---
title: "Agent Factories for High Level Synthesis: How Far Can General-Purpose Coding Agents Go in Hardware Optimization?"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.25719"
published: "2026-03-27"
summarized: "2026-03-28T07:08:14.296094"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文实证研究了通用编程智能体（无需硬件特定训练）在高级综合（HLS）中优化硬件设计的能力边界。作者提出"智能体工厂"框架，通过两阶段流水线协调多个自主优化智能体，在12个HLS基准测试上实现了平均8.27倍加速，最高超过20倍。研究发现智能体能够自发重新发现已知的硬件优化模式，且最优设计往往不来自ILP排名最高的候选方案，揭示了全局优化相对于子核分解搜索的价值。

【方法概述 / Method】
论文提出两阶段智能体工厂流水线：第一阶段将设计分解为子核，独立优化每个子核的pragma和代码级转换，并建立整数线性规划（ILP）模型在面积约束下组装全局有希望的配置；第二阶段在ILP最优解上启动N个专家智能体，探索跨函数优化（pragma重组、循环融合、内存重构等）。使用Claude Code（Opus 4.5/4.6）配合AMD Vitis HLS进行实现。

【实验结果 / Results】
在HLS-Eval和Rodinia-HLS的12个内核上，智能体数量从1扩展到10时获得平均8.27倍加速，困难基准收益更高：streamcluster超过20倍，kmeans约10倍。智能体无需领域特定训练即可持续重新发现已知硬件优化模式，且最佳设计常源于非ILP顶级候选，表明全局优化能捕捉子核搜索遗漏的改进空间。

【应用价值 / Applications】
该研究为硬件设计自动化提供了新范式，证明通用大语言模型智能体可有效替代传统领域专用HLS优化工具，降低硬件设计门槛和开发周期。智能体工厂框架可集成到现有HLS编译流程中，通过可扩展的智能体数量灵活权衡计算资源与优化质量，适用于FPGA/ASIC加速的机器学习、科学计算等高性能计算场景。
