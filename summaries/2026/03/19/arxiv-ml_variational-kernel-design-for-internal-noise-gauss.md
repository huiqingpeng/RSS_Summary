---
title: "Variational Kernel Design for Internal Noise: Gaussian Chaos Noise, Representation Compatibility, and Reliable Deep Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17365"
published: "2026-03-19"
summarized: "2026-03-19T12:10:34.426712"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了变分核设计（Variational Kernel Design, VKD）框架，用于系统性地设计深度网络内部噪声的几何结构，并确保噪声扰动与网络表示的兼容性。通过求解二次最大熵原理，作者推导出基于Dirichlet Green核的高斯混沌噪声（Gaussian Chaos Noise, GCh），该噪声在理论上具有精确的成对log-ratio变形控制、边界敏感的排序稳定性和期望内在粗糙度预算。实验表明，GCh在ImageNet和ImageNet-C上显著提升了模型校准性能，并在分布偏移下改善了负对数似然（NLL），同时保持竞争力的准确率。

【方法概述 / Method】
VKD框架通过三个组件定义噪声机制：法则族（law family）、相关核（correlation kernel）和注入算子（injection operator）。在空间子族的解析解中，作者对潜在log-场应用二次最大熵原理，得到精度由Dirichlet Laplacian给出的高斯优化器，进而通过Wick归一化构造出均值为1的正门控——高斯混沌噪声（GCh），作为实践中样本级门控的理论基础。

【实验结果 / Results】
在ImageNet和ImageNet-C基准上，GCh相比传统启发式噪声（如dropout、硬掩码）表现出一致的校准性能提升，同时在分布偏移条件下改善了NLL，且未牺牲分类准确率。理论分析进一步证明，硬二值掩码会在正相干表示上产生奇异或相干性放大的失真，而GCh避免了这一问题。

【应用价值 / Applications】
该研究为可靠深度学习提供了理论基础，特别适用于需要高校准性和分布外鲁棒性的场景，如医疗诊断、自动驾驶等安全关键应用。GCh可作为即插即用的内部噪声机制替代现有启发式方法，提升深度神经网络的可解释性和可信度。
