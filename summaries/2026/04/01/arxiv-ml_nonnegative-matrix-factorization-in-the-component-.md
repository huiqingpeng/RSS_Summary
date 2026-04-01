---
title: "Nonnegative Matrix Factorization in the Component-Wise L1 Norm for Sparse Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29715"
published: "2026-04-01"
summarized: "2026-04-02T07:19:53.394089"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了基于分量L1范数的非负矩阵分解（L1-NMF），该方法适用于受重尾噪声（如拉普拉斯噪声、椒盐噪声）或异常值污染的数据。作者证明了即使当秩r=1时，L1-NMF也是NP难问题，这与标准的最小二乘NMF形成对比；同时发现L1-NMF会对稀疏输入数据产生过度稀疏的因子解，进而提出了加权L1-NMF（wL1-NMF）模型及其稀疏坐标下降算法（sCD），该算法复杂度与数据非零元素数量成正比，可高效处理大规模稀疏数据。

【方法概述 / Method】

论文提出了加权L1-NMF（wL1-NMF）模型，通过在数据零值位置对应的WH项上添加惩罚参数来控制分解稀疏性；并设计了稀疏坐标下降算法（sCD），利用加权中位数算法求解每个子问题，使计算复杂度仅依赖于数据的非零元素数量。

【实验结果 / Results】

大量合成数据和真实数据实验表明，wL1-NMF模型在存在假零值的稀疏数据上优于标准L1-NMF；sCD算法作为首个复杂度随非零元素数量线性增长的L1-NMF算法，在处理大规模稀疏数据时展现出显著的计算效率优势。

【应用价值 / Applications】

该研究适用于含异常值或重尾噪声的稀疏数据分析场景，如推荐系统、文本挖掘、生物信息学中的基因表达数据分析等领域；wL1-NMF模型和sCD算法为大规模稀疏数据的鲁棒性因子分解提供了可解释且计算高效的解决方案。
