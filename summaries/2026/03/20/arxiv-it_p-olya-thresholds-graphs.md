---
title: "P\'olya Thresholds Graphs"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2603.18452"
published: "2026-03-20"
summarized: "2026-03-20T17:06:19.350082"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Pólya阈值图模型，这是一种通过双色Pólya urn过程序贯生成的随机阈值图。作者推导了该模型的随机性质（包括精确度分布、距离衰减中心性期望）和代数性质（包括拉普拉斯矩阵的显式谱分解），并将其应用于离散时间共识动态分析。

【方法概述 / Method】
该模型从空图开始，每一步从Pólya urn中抽取一个指示变量，决定新加入节点是"通用节点"（与所有现有节点及自身相连）还是"孤立节点"（不与任何现有节点相连）。作者利用Pólya抽取过程的结构特性，建立了邻接矩阵的显式表示，并基于此进行后续的随机和代数分析。

【实验结果 / Results】
论文获得了任意节点的精确度分布及其均值与方差的闭式表达；给出了距离衰减中心性（distance-based decay centrality）期望的显式公式；完整刻画了随机阈值图的拉普拉斯矩阵，得到了其谱和特征基的闭式描述。

【应用价值 / Applications】
该研究为复杂网络分析提供了新的可解析随机图模型，其显式的代数结构特别适用于网络共识动态、流行病传播等需要精确谱信息的应用场景，也为理解基于偏好依附（preferential attachment-like）机制的网络演化提供了理论工具。
