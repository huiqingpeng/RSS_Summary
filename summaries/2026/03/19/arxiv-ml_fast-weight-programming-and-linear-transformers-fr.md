---
title: "Fast weight programming and linear transformers: from machine learning to neurobiology"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2508.08435"
published: "2026-03-19"
summarized: "2026-03-19T14:05:29.637473"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文综述了快速权重编程器（Fast Weight Programmers, FWPs）这一新型循环神经网络架构，其核心特征在于使用二维矩阵形式的隐状态而非传统RNN的向量形式隐状态，从而实现动态变化的突触权重（快速权重）作为短期记忆存储。文章系统回顾了FWPs的技术基础、计算特性及其与Transformer和状态空间模型的联系，并探讨了FWPs与大脑突触可塑性模型之间的关联，指出自然智能与人工智能在此领域的趋同。

【方法概述 / Method】
FWPs采用"编程器-执行器"架构，其中编程器网络（通常通过梯度下降训练）根据输入观测动态生成对快速权重的修改指令，而执行器网络则利用这些不断更新的快速权重进行计算；这种2D矩阵隐状态设计使模型能够高效地存储和检索上下文信息，并与线性Transformer和状态空间模型建立了理论等价性。

【实验结果 / Results】
（注：本文为综述性"Primer"文章，未报告具体实验结果；主要贡献在于统一理论框架的构建，阐明了FWPs与线性注意力Transformer、RNN及神经科学可塑性模型之间的形式化等价关系，并分析了其计算效率优势。）

【应用价值 / Applications】
FWPs为开发更高效的语言模型和序列处理系统提供了新思路，其线性复杂度特性使其适用于长序列建模；同时，该框架为理解大脑神经可塑性机制提供了计算模型，有望促进神经科学与人工智能的跨学科研究，推动类脑计算和可解释AI的发展。
