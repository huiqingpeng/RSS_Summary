---
title: "Deep Hilbert--Galerkin Methods for Infinite-Dimensional PDEs and Optimal Control"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19463"
published: "2026-03-23"
summarized: "2026-03-24T07:18:25.498465"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了基于深度学习的Hilbert-Galerkin神经算子（HGNOs），用于求解可分Hilbert空间上的完全非线性二阶偏微分方程（如无限维控制的Hamilton-Jacobi-Bellman方程）。作者证明了首个适用于此类问题的通用逼近定理（UATs），涵盖了函数及其Fréchet导数（直至二阶）和无界算子的逼近，并针对控制问题证明了最优反馈控制的UATs。此外，本文首次提出在整个Hilbert空间上最小化PDE残差L²范数的深度Hilbert-Galerkin和Hilbert Actor-Critic训练方法，并成功应用于热方程和Burgers方程的最优控制问题。

【方法概述 / Method】

核心方法是参数化Hilbert-Galerkin神经算子（HGNOs）来逼近无限维PDE的解，通过在整个Hilbert空间上最小化PDE残差的L²_μ(H)范数进行训练，而非投影到有限维。对于控制问题，采用Hilbert Actor-Critic强化学习方法，基于逼近的价值函数HGNO学习最优反馈控制策略。

【实验结果 / Results】

论文数值求解了与确定性和随机热方程、Burgers方程最优控制相关的Kolmogorov方程和HJB方程，验证了所提深度学习方法的有效性。虽然具体量化指标未在摘要中详述，但实验结果表明该方法在无限维PDE和最优控制问题上具有良好前景。

【应用价值 / Applications】

该方法可广泛应用于物理学中的泛函微分方程、受控PDE/SPDE、路径依赖系统、部分观测随机系统以及平均场随机微分方程相关的Kolmogorov方程和HJB方程。实际价值在于为传统数值方法难以处理的无限维最优控制问题（如流体控制、随机系统控制）提供了新的计算工具，特别适用于高维或无限维状态空间的复杂控制系统。
