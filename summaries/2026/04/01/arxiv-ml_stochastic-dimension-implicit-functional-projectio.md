---
title: "Stochastic Dimension Implicit Functional Projections for Exact Integral Conservation in High-Dimensional PINNs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29237"
published: "2026-04-01"
summarized: "2026-04-02T07:16:55.237780"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了随机维度隐式函数投影（SDIFP）框架，用于在高维物理信息神经网络（PINNs）中精确强制执行宏观守恒定律（如质量和能量守恒）。该方法通过对连续网络输出应用全局仿射变换，结合分离的蒙特卡洛积分，避免了传统离散投影对空间网格的依赖。SDIFP还引入了双随机无偏梯度估计器（DS-UGE），将内存复杂度从$\mathcal{O}(M \times N_{\mathcal{L}})$降至$\mathcal{O}(N \times |\mathcal{I}|)$，实现了可扩展的无网格高维守恒型PDE求解。

【方法概述 / Method】

SDIFP采用全局仿射变换替代传统的离散向量投影，直接作用于神经网络的连续输出函数；通过分离式蒙特卡洛积分计算积分约束的闭式解，消除了对确定性求积和空间网格的依赖。训练过程中使用DS-UGE，将空间采样与微分算子子采样解耦，实现双随机估计以降低内存开销。

【实验结果 / Results】

论文表明SDIFP能够有效缓解采样方差问题，同时保持解的正则性；推理阶段保持$\mathcal{O}(1)$的计算效率。所提出的DS-UGE显著降低了高阶算子带来的内存负担，使方法能够扩展到传统方法难以处理的高维守恒型PDE问题。

【应用价值 / Applications】

SDIFP适用于需要精确满足物理守恒定律的高维偏微分方程求解场景，如计算流体力学、等离子体物理和量子多体系统等。该方法为科学机器学习提供了可扩展的无网格计算框架，在保持物理一致性的同时突破了维度灾难的限制，具有重要的科学与工程应用价值。
