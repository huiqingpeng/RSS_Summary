---
title: "Optimal low-rank stochastic gradient estimation for LLM training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20632"
published: "2026-03-24"
summarized: "2026-03-25T07:12:37.514749"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对大语言模型（LLM）训练中内存受限和高维参数空间随机梯度噪声的问题，提出了一种无偏、内存高效的低秩随机梯度估计器。该方法通过将高维随机梯度投影到随机低维子空间再还原，在保证无偏性的同时控制均方误差，并通过求解约束泛函优化问题得到最优投影分布（包括Haar-Stiefel投影）。实验表明，该方法在RoBERTa-large微调中实现最低峰值GPU内存（3.83GB vs 全量反向传播的16.7GB），在LLaMA预训练中优于传统方法。

【方法概述 / Method】

核心方法是将高维随机梯度估计器投影到随机低维子空间并还原，通过约束泛函优化求解最优投影分布，设计出方差最低的随机投影器。该方法适用于常见的随机梯度估计范式，包括Haar-Stiefel投影等具体实现。

【实验结果 / Results】

在RoBERTa-large微调任务中，该方法达到对比方法中最低的峰值GPU内存（3.83GB），相比全量反向传播（16.7GB）大幅降低，同时保持竞争力的准确率；在自回归LLM预训练（LLaMA-20M/60M/100M）中，该方法优于传统方法，验证了最优投影策略的有效性。

【应用价值 / Applications】

该研究为大规模语言模型训练提供了内存高效的梯度估计方案，特别适用于显存受限场景下的模型微调和预训练。其最优投影设计可指导算法开发，在保持模型性能的同时显著降低硬件门槛，有助于推动更大规模LLM的可及性研究和实际部署。
