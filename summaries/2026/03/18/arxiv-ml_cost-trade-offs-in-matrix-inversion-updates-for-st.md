---
title: "Cost Trade-offs in Matrix Inversion Updates for Streaming Outlier Detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16697"
published: "2026-03-18"
summarized: "2026-03-18T15:46:15.248547"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了在线异常检测中矩阵逆更新问题的计算成本权衡，比较了三种方法：直接求逆（DI）、迭代Sherman-Morrison（ISM）和Woodbury矩阵恒等式（WMI）。通过理论推导和Python仿真实验，作者提出了一个简洁实用的选择规则：ISM适用于秩-1更新，WMI适用于相对于矩阵尺寸较小的更新，其他情况则优选DI。该结果对任何涉及矩阵逆更新的问题具有普遍指导意义。

【方法概述 / Method】
论文针对Christoffel函数异常检测中的在线学习场景，推导了三种矩阵逆更新方法的理论计算复杂度，并在CPU环境下进行了全面的Python仿真验证，以确定不同参数设置下各方法的实际性能表现。

【实验结果 / Results】
理论分析和仿真结果表明，三种方法各有最优适用区间：ISM在秩-1更新时效率最高，WMI在更新秩相对于矩阵维度较小时表现最佳，而DI在其他情况下更为高效。这些发现形成了可量化的决策规则。

【应用价值 / Applications】
该研究为实时流式异常检测系统提供了算法选择指导，帮助开发者在资源受限环境下优化计算效率；同时，其结论可推广至任何需要动态更新矩阵逆的机器学习场景，如在线学习、自适应滤波和递归最小二乘等应用。
