---
title: "Statistical Inference for Online Algorithms"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.17300"
published: "2026-03-19"
summarized: "2026-03-19T14:15:45.874241"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对在线算法（online algorithms）的统计推断问题，提出了一种名为HulC（Hull of Confidence）的计算高效、速率最优的包装方法。该方法能够绕过渐近方差估计的需求，为任何产生渐近正态估计量的在线算法构建渐近有效的置信区间和假设检验。作者主要使用带Polyak-Ruppert平均的随机梯度下降（SGD）评估方法性能，并与隐式SGD和ROOT-SGD等其他在线算法进行了广泛的数值模拟比较。

【方法概述 / Method】

HulC方法采用分而治之的策略，将数据流分割为多个子集，在每个子集上独立运行目标在线算法获得估计量，然后基于这些子估计量的经验分布构建置信区域。该方法仅需单次数据遍历（single pass），避免了传统方法中计算代价高昂的方差估计步骤，同时保持了统计最优性。

【实验结果 / Results】

实验结果表明，HulC与Polyak-Ruppert平均SGD结合使用时，在覆盖概率和区间宽度方面均表现良好，达到了与理想Wald区间相当的统计效率。数值模拟显示，该方法在多种在线算法（包括隐式SGD和ROOT-SGD）上均能产生有效的置信区间，且在计算成本显著降低的情况下保持了竞争性的统计性能。

【应用价值 / Applications】

该研究在大规模流式数据分析和实时机器学习系统中具有重要应用价值，特别是在数据只能单次访问、存储受限或延迟要求严格的场景（如在线广告、金融交易、物联网传感器网络）。HulC为实践者提供了一种即插即用的工具，可在不修改底层在线优化算法的前提下，为其输出提供可靠的统计不确定性量化。
