---
title: "Upper Entropy for 2-Monotone Lower Probabilities"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23558"
published: "2026-03-26"
summarized: "2026-03-27T07:14:22.271045"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了在可信度方法（credal approaches）中作为不确定性度量的上熵（upper entropy）的计算问题，针对2-单调下概率（2-monotone lower probabilities）这一重要类别。论文提供了该问题的完整算法与复杂度分析，证明了该问题存在强多项式时间解，并对现有算法提出了多项重大改进。

【方法概述 / Method】
论文采用计算复杂性理论与优化算法相结合的方法，针对2-单调下概率及其特例（如可能性测度、置信函数等）的上熵计算问题进行分析。作者开发了具有强多项式复杂度的算法，并通过利用2-单调性的结构特性对算法进行了优化。

【实验结果 / Results】
论文证明了上熵计算问题可以在强多项式时间内求解，突破了以往算法的效率瓶颈。所提出的改进算法在理论复杂度上显著优于现有方法，为实际应用中的大规模计算提供了可行性。

【应用价值 / Applications】
该研究在模型选择/正则化、主动学习、分布外（OOD）检测等需要量化预测不确定性的机器学习任务中具有重要应用价值。高效的 upper entropy 计算算法使得基于可信度集合的不确定性量化方法在计算上更加实用，可广泛应用于鲁棒决策和风险敏感型预测系统。
