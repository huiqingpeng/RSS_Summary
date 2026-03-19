---
title: "Neighbor GRPO: Contrastive ODE Policy Optimization Aligns Flow Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.16955"
published: "2026-03-19"
summarized: "2026-03-19T14:17:49.603681"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对流匹配模型（flow matching models）的偏好对齐问题，提出了Neighbor GRPO算法。现有方法通过将ODE转换为SDE来引入随机性，但存在信用分配效率低和与高阶采样器不兼容的问题。作者从距离优化视角重新诠释了SDE-based GRPO的本质，发现其机制实为对比学习，并据此设计了无需SDE的Neighbor GRPO，通过扰动初始噪声生成候选轨迹，采用基于softmax距离的代理跳跃策略进行优化。实验表明，该方法在训练成本、收敛速度和生成质量上均显著优于SDE-based方法。

【方法概述 / Method】

Neighbor GRPO的核心创新包括：通过扰动ODE初始噪声条件生成多样化候选轨迹，建立基于softmax距离的代理跳跃策略；理论证明了该距离目标与策略梯度优化的等价性，从而严格嵌入GRPO框架；同时引入对称锚点采样降低计算开销，以及组级拟范数重加权解决奖励平坦化问题。

【实验结果 / Results】

实验表明Neighbor GRPO在多个维度显著优于SDE-based方法：训练成本更低、收敛速度更快、生成质量更高。方法完整保留了确定性ODE采样的优势，包括计算效率和对高阶求解器的兼容性，实现了更少步数的高质量采样。

【应用价值 / Applications】

该研究为图像和视频生成模型的偏好对齐提供了高效解决方案，特别适用于需要快速推理的场景（如实时生成、边缘设备部署）。其确定性ODE兼容特性使其可直接集成现有高阶采样器，降低推理成本，对扩散模型和流模型的实际部署具有重要工程价值。
