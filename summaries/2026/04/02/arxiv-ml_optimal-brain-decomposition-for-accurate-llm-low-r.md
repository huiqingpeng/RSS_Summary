---
title: "Optimal Brain Decomposition for Accurate LLM Low-Rank Approximation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00821"
published: "2026-04-02"
summarized: "2026-04-03T07:25:24.708031"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了OBD-LLM（Optimal Brain Decomposition LLM），一种利用二阶Hessian信息进行低秩分解的新方法。通过Kronecker分解严格推导，作者证明最优分解需要同时考虑层的输入和输出信息，而非仅依赖输入信息。该方法通过双向白化实现损失感知的权重矩阵分解，相比先前的SVD-LLM方法取得了20-40%的性能提升。

【方法概述 / Method】
OBD-LLM采用基于Hessian矩阵的二阶优化方法，通过Kronecker因子化将Hessian分解为输入和输出相关的组件。核心创新在于对权重矩阵进行双向白化（bi-directional whitening），同时建模输入激活和输出梯度的联合分布，从而获得闭式最优解。

【实验结果 / Results】
实验表明，OBD-LLM在低秩近似任务上显著优于现有SOTA方法SVD-LLM，性能提升达20-40%。该方法在保持相同压缩率的同时，实现了更精确的权重重建和更低的任务性能损失。

【应用价值 / Applications】
该技术可直接应用于大语言模型的微调和推理加速，包括模型压缩、参数高效微调（PEFT）和边缘设备部署。通过更精确的低秩近似，OBD-LLM能够在减少计算资源消耗的同时，更好地保持模型原有能力。
