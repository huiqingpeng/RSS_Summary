---
title: "MST-Direct: Matching via Sinkhorn Transport for Multivariate Geostatistical Simulation with Complex Non-Linear Dependencies"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18036"
published: "2026-03-20"
summarized: "2026-03-20T12:06:00.742366"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对多元地质统计模拟中复杂非线性依赖关系（如双峰分布、阶梯函数和异方差关系）的精确重现问题，提出了一种基于最优传输理论的新算法MST-Direct。该方法利用Sinkhorn算法直接匹配多元分布，同时保持空间相关结构，通过将所有变量作为单一多维向量同时处理，实现了在完整联合空间中的关系匹配，而非依赖成对线性相关性。相比传统的高斯Copula和LU分解等方法，MST-Direct能够有效保留复杂的联合分布模式。

【方法概述 / Method】
MST-Direct基于最优传输（Optimal Transport）理论，采用Sinkhorn算法进行正则化熵优化求解，以计算源分布与目标分布之间的最优匹配。该方法将多个地质变量整合为统一的多维向量进行联合处理，通过直接在完整的联合概率空间中进行分布匹配，突破了传统方法仅处理两两变量间线性关系的局限。

【实验结果 / Results】
（注：论文摘要中未提供具体实验结果和性能指标的详细描述，仅说明该方法能有效处理双峰分布、阶梯函数和异方差关系等复杂非线性依赖结构，并能在保持空间相关性的同时实现多元分布的精确匹配。）

【应用价值 / Applications】
MST-Direct在矿产资源评估、油气储层表征和环境地质建模等领域具有重要应用价值，能够提供更准确的地质不确定性量化。该方法特别适用于变量间存在复杂非线性关系的场景，可提升多变量联合模拟的可靠性，为决策制定提供更稳健的地质统计模型支持。
