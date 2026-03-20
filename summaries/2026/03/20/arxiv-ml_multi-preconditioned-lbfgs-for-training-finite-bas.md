---
title: "Multi-Preconditioned LBFGS for Training Finite-Basis PINNs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.08709"
published: "2026-03-20"
summarized: "2026-03-20T15:03:09.636978"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种多预条件LBFGS（MP-LBFGS）算法，用于训练有限基物理信息神经网络（FBPINNs）。该算法受非线性加性Schwarz方法启发，利用FBPINNs基于域分解的加性架构，在子域上定义局部神经网络以实现网络表示的局部化。数值实验表明，MP-LBFGS相比标准LBFGS能够提高收敛速度和模型精度，同时降低通信开销。

【方法概述 / Method】

MP-LBFGS算法通过在FBPINNs的局部架构上构建并行的子域局部拟牛顿修正来实现优化。其核心创新是一种非线性多预条件机制，通过求解低维子空间最小化问题来最优组合各子域的修正项，从而实现高效的分布式训练。

【实验结果 / Results】

实验结果显示，MP-LBFGS在收敛速度和模型精度方面均优于标准LBFGS算法，同时具有更低的通信开销。该算法有效利用了FBPINNs的局部化网络表示特性，实现了高效的并行计算。

【应用价值 / Applications】

该研究为物理信息神经网络的高效训练提供了新的优化方法，特别适用于需要大规模并行计算的科学计算和工程仿真场景。MP-LBFGS算法可应用于求解偏微分方程、物理系统建模等领域，有望加速复杂物理问题的神经网络求解过程。
