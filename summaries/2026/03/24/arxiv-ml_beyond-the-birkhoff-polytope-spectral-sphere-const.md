---
title: "Beyond the Birkhoff Polytope: Spectral-Sphere-Constrained Hyper-Connections"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20896"
published: "2026-03-24"
summarized: "2026-03-25T07:15:32.130799"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文揭示了基于Birkhoff多面体约束的Hyper-Connections（mHC）存在的三个关键缺陷：恒等退化、表达瓶颈和参数化低效。为此，作者提出Spectral-Sphere-Constrained Hyper-Connections（sHC），将可行集从刚性多面体转移到谱范数球，允许负值条目以实现减法特征解耦，同时消除了不稳定的Sinkhorn投影和阶乘级参数化开销，在保持训练稳定性的同时显著提升了模型表达能力。

【方法概述 / Method】
sHC通过将残差矩阵的约束条件从双随机矩阵（Birkhoff多面体）改为谱范数球约束，实现了几何上的关键转变。该方法允许矩阵包含负值元素，从而支持减法交互作用进行选择性特征多样化，并采用直接的谱归一化替代Sinkhorn迭代或基于置换的参数化。

【实验结果 / Results】
论文指出mHC存在恒等退化问题（学习到的矩阵坍缩至恒等矩阵）、非负性约束导致的表达瓶颈，以及Sinkhorn迭代不稳定或置换参数化阶乘级开销等问题。sHC通过谱球约束有效解决了这些缺陷，实现了非退化的、具有表达力的残差矩阵，同时保持了训练稳定性。

【应用价值 / Applications】
该研究可广泛应用于深度神经网络架构设计，特别是在需要多流特征混合的复杂模型中，如视觉Transformer、多模态融合网络等。sHC提供了一种更稳定、高效的超连接机制，有助于构建更具表达力且训练稳定的深度学习模型，降低计算开销并提升特征交互质量。
