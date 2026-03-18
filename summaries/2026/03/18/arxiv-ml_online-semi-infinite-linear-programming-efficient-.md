---
title: "Online Semi-infinite Linear Programming: Efficient Algorithms via Function Approximation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16200"
published: "2026-03-18"
summarized: "2026-03-18T15:41:55.658808"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了动态资源分配问题，其中决策空间有限但需满足大量甚至无限约束（通过流式数据或oracle反馈揭示），将其建模为在线半无限线性规划（OSILP）问题。核心贡献是通过函数近似将约束数量降至常数q，突破了传统在线LP算法遗憾界依赖于约束数量的瓶颈。在随机输入和随机排列两种经典模型下，分别证明了$O(q\sqrt{T})$和$O((q+q\log T)\sqrt{T})$的遗憾界，且与约束数量无关；进一步提出两阶段算法在更强假设下达到$O(q\log T + q/\epsilon)$遗憾。

【方法概述 / Method】

本文采用函数近似技术将无限约束转化为有限维表示，构建新的LP近似形式；设计基于对偶的求解算法，通过选择合适的势函数（potential functions）实现广泛适用性。针对一般函数设定扩展算法，并提出两阶段改进算法以突破$O(\sqrt{T})$遗憾下界。

【实验结果 / Results】

实验验证所提算法在面对大量约束时显著优于现有方法；理论分析表明遗憾界仅依赖于近似维度q而与真实约束数量无关，在随机输入模型下为$O(q\sqrt{T})$，随机排列模型下为$O((q+q\log T)\sqrt{T})$；两阶段算法在更强条件下改进为$O(q\log T + q/\epsilon)$。

【应用价值 / Applications】

该研究适用于流式数据环境下的实时资源分配决策，如云计算资源调度、在线广告投放、供应链管理等场景，其中约束条件随时间动态揭示且规模巨大；函数近似方法使得算法能够处理传统方法无法应对的无限或大规模约束问题，具有广泛的实际应用潜力。
