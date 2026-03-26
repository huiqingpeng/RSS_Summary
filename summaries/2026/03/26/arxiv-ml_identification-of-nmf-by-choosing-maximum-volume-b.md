---
title: "Identification of NMF by choosing maximum-volume basis vectors"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24227"
published: "2026-03-26"
summarized: "2026-03-27T07:22:08.093484"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对非负矩阵分解（NMF）的可识别性问题，提出了一种新的最大体积约束NMF框架（maximum-volume-constrained NMF）。与现有最小体积约束NMF通过使基向量尽可能相似来诱导稀疏性不同，新方法通过使基向量尽可能互异来解决高度混合数据的分解失败问题。作者建立了该框架的可识别性定理，并提供了相应的估计算法，实验验证了方法的有效性。

【方法概述 / Method】
论文提出最大体积约束NMF框架，通过最大化基向量构成的单形体体积来增强基向量的可区分性。该方法建立了严格的可识别性理论保证，并设计了相应的优化算法来估计最大体积约束下的NMF解。

【实验结果 / Results】
实验结果表明，所提出的最大体积约束NMF在高度混合数据场景下优于传统的最小体积约束方法，能够有效恢复真实的基向量而非其混合形式，验证了理论分析的正确性和算法的实用性。

【应用价值 / Applications】
该方法适用于光谱解混、文本挖掘、基因表达分析等需要处理高度混合数据的盲源分离场景，为NMF在复杂数据环境下的可靠应用提供了理论基础，特别是在真实基向量需要具有明确物理或语义解释性的领域具有重要价值。
