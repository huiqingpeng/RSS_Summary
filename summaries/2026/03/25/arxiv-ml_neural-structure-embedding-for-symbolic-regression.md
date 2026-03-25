---
title: "Neural Structure Embedding for Symbolic Regression via Continuous Structure Search and Coefficient Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22429"
published: "2026-03-25"
summarized: "2026-03-26T07:14:35.662043"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SRCO（Symbolic Regression via Continuous structure search and Coefficient Optimization），一种基于神经结构嵌入的符号回归统一框架。该框架通过Transformer模型将离散的符号结构压缩到连续嵌入空间，实现了基于梯度的结构搜索和系数优化，有效解决了传统遗传编程等方法计算成本高、性能不稳定、难以扩展到大规模方程空间的问题。实验表明，SRCO在方程精度、鲁棒性和搜索效率上均优于现有最先进方法，为符号回归开辟了连续嵌入学习与优化相结合的新范式。

【方法概述 / Method】
SRCO包含三个核心组件：（1）结构嵌入——利用传统符号回归算法生成探索性方程池，训练Transformer模型将符号结构编码为连续向量；（2）连续结构搜索——在连续嵌入空间中采用基于梯度或采样的优化方法高效探索方程结构；（3）系数优化——将发现的符号结构中的系数视为可学习参数，通过梯度优化获得精确数值解。

【实验结果 / Results】
在合成数据集和真实世界数据集上的实验表明，SRCO在方程发现精度、算法鲁棒性和搜索效率方面持续超越现有最先进方法；通过将组合结构空间的离散搜索转化为连续空间的优化问题，显著降低了计算开销。

【应用价值 / Applications】
该研究可广泛应用于科学发现、物理定律挖掘、工程系统建模等需要从观测数据中自动发现可解释数学表达式的场景；其连续嵌入范式为处理大规模方程空间和提升符号回归的实用化部署提供了新思路，有助于加速数据驱动的科学研究与工业建模流程。
