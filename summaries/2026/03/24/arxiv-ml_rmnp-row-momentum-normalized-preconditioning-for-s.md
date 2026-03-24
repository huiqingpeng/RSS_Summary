---
title: "RMNP: Row-Momentum Normalized Preconditioning for Scalable Matrix-Based Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20527"
published: "2026-03-24"
summarized: "2026-03-25T07:11:18.829452"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了RMNP（行动量归一化预条件优化器），一种用于大规模矩阵优化的新型预条件自适应方法。RMNP通过简单的行-wise ℓ₂归一化操作替代了Muon中使用的Newton-Schulz迭代，将每迭代计算复杂度从O(mn·min(m,n))降低到O(mn)，同时保持了相当的优化性能。理论分析证明了RMNP在非凸设置下具有与Muon匹配的最优收敛保证，大规模语言模型预训练实验表明RMNP在显著减少预条件计算时间的同时取得了与Muon竞争的性能。

【方法概述 / Method】
RMNP的核心创新在于利用Transformer层Hessian矩阵经验观察到的对角块结构，用行-wise ℓ₂归一化替代复杂的Newton-Schulz迭代来构建预条件更新。该方法直接对梯度矩阵的行进行归一化处理，避免了显式构造预条件矩阵，实现了更高效的预条件梯度计算。

【实验结果 / Results】
在大规模语言模型预训练任务上的广泛实验表明，RMNP与Muon相比具有竞争力的优化性能，同时大幅降低了预条件的实际计算时间（wall-clock time）。实验验证了计算复杂度理论分析的准确性，展示了RMNP在可扩展性方面的优势。

【应用价值 / Applications】
RMNP主要适用于大规模深度学习模型（特别是Transformer架构）的训练优化，可显著加速预条件自适应优化过程。该方法为训练大型语言模型等计算密集型任务提供了更高效的优化器选择，在保证模型收敛质量的同时降低了计算开销，对AI基础设施和模型训练效率提升具有重要实践意义。
