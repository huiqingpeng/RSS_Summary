---
title: "An Efficient Global Optimization Algorithm with Adaptive Estimates of the Local Lipschitz Constants"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2211.04129"
published: "2026-03-18"
summarized: "2026-03-18T16:04:51.615242"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了HALO（混合自适应Lipschitzian优化）算法，一种基于区域划分的确定性全局优化方法，通过自适应估计目标函数不同子区域的局部Lipschitz常数来计算下界并引导搜索全局最小值。该算法无需超参数调优，并能识别重要变量以辅助问题解释，同时结合了梯度型和免导数局部优化策略以加速收敛。在数百个测试函数上的数值实验表明，HALO在求解复杂黑箱优化问题上具有显著优势。

【方法概述 / Method】
HALO采用基于绝对斜率的自适应平衡机制，动态整合全局与局部信息来估计各子区域的局部Lipschitz常数，从而构建更紧致的函数下界。算法通过区域划分策略将搜索空间分解为多个子区域，并耦合局部优化器实现全局探索与局部开发的协同。

【实验结果 / Results】
HALO与多种主流全局优化算法在数百个测试函数上进行了对比实验，数值结果显示出很强的竞争力，证明该算法能够有效处理具有挑战性的实际黑箱优化问题。算法无需手动调参的特性使其在实际应用中更具便利性。

【应用价值 / Applications】
HALO适用于工程、科学计算和机器学习等领域中的黑箱全局优化问题，特别是目标函数计算昂贵、缺乏解析形式或导数信息难以获取的场景。该算法为复杂系统优化、超参数调优和仿真优化等实际应用提供了高效且易用的工具，其开源Python实现进一步促进了学术和工业界的广泛采用。
