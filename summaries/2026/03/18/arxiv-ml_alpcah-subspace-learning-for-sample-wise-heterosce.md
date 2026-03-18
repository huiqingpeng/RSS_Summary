---
title: "ALPCAH: Subspace Learning for Sample-wise Heteroscedastic Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.07272"
published: "2026-03-18"
summarized: "2026-03-18T17:10:21.471665"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了ALPCAH（Adaptive Low-rank Principal Component Analysis with Heteroscedasticity），一种用于样本级异方差数据的子空间学习方法。该方法能够同时估计每个样本的噪声方差，并利用这些信息改进低秩子空间基底的估计。ALPCAH不对低秩成分做分布假设，也不需要预先知道噪声方差或子空间维度（通过软秩约束实现）。此外，作者还开发了矩阵分解版本LR-ALPCAH，以牺牲维度已知性为代价换取更高的计算效率和内存效率。

【方法概述 / Method】

ALPCAH采用自适应加权策略，通过迭代优化同时估计样本特定的噪声方差和子空间结构，核心是一个带软秩约束的优化问题。LR-ALPCAH则通过显式的低秩矩阵分解（X = UV^T）替代特征值分解，将计算复杂度从O(n³)降低到O(ndr)，其中n为样本数，d为维度，r为子空间维度。

【实验结果 / Results】

模拟实验和真实数据表明，考虑数据异方差性显著提升了子空间估计的准确性，ALPCAH优于现有的异方差PCA方法。LR-ALPCAH在保持相近估计精度的同时，大幅减少了运行时间和内存占用，尤其适用于大规模数据集。

【应用价值 / Applications】

该方法适用于数据质量参差不齐的实际场景，如传感器网络（不同节点噪声水平各异）、众包数据标注（标注者可靠性不同）、天文观测（仪器或天气条件导致的测量质量差异）等，能够从这些异质数据中提取更可靠的低维表示。
