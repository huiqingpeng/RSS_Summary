---
title: "Beyond Muon: MUD (MomentUm Decorrelation) for Faster Transformer Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17970"
published: "2026-03-19"
summarized: "2026-03-19T12:18:42.602186"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MUD（MomentUm Decorrelation），一种用于加速Transformer训练的新型优化器。MUD通过三角（Cholesky-like）白化方法替代Muon中的极分解迭代，显著降低了优化器计算开销。实验表明，MUD在时间-困惑度指标上相比调优后的AdamW和Muon实现了10-50%的墙钟时间提升，峰值token处理速度提升1.3-2.6倍，最高可达近3倍，同时在ESM-2 150M蛋白质语言模型上也验证了有效性。

【方法概述 / Method】
MUD采用基于经典Gram-Schmidt和Gauss-Seidel思想的三角白化替代方案，将矩阵值动量更新进行去相关处理。该方法以行正交矩阵为不动点，其内部步骤等价于对Gram矩阵进行对称Gauss-Seidel预处理，并在不动点附近具有二次局部收敛性。

【实验结果 / Results】
在GPT-2 large等模型上，MUD相比Muon实现了约1.3-2.6倍的峰值token/s提升，最高接近3倍；在时间-困惑度指标上较AdamW和Muon提升10-50%。尽管每步收敛速度略慢于Muon，但由于优化器开销大幅降低，整体墙钟时间显著减少。在ESM-2 150M蛋白质语言模型上，MUD以更短的墙钟时间达到了与Muon相当的验证困惑度。

【应用价值 / Applications】
MUD可广泛应用于大规模Transformer模型的训练加速，尤其适用于计算资源受限或追求训练效率的场景，如大语言模型预训练、蛋白质序列建模等。该方法为深度学习社区提供了一种硬件友好、计算高效的优化器选择，有望降低大规模模型训练的时间和成本门槛。
