---
title: "Neural Pushforward Samplers for the Fokker-Planck Equation on Embedded Riemannian Manifolds"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16239"
published: "2026-03-18"
summarized: "2026-03-18T16:11:33.440519"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文将弱对抗神经前推（WANPF）方法扩展到嵌入欧氏空间中的紧致黎曼流形上的Fokker-Planck方程求解。核心创新在于利用环境空间表示的Laplace-Beltrami算子（通过切向投影和平均曲率向量），使得所有积分可转化为流形上样本的期望计算。通过流形收缩映射约束神经前推映射，确保概率守恒和流形隶属关系在构造层面得到保证，实现了无需自动微分、无需网格的训练。

【方法概述 / Method】

论文采用基于弱形式的对抗神经网络方法，将Fokker-Planck方程的解表示为神经前推映射变换后的基础分布。关键是通过切向投影矩阵P(x)和平均曲率向量H(x)的环境空间公式，结合流形收缩（retraction）操作，确保生成的样本始终位于目标流形上。选用环境空间平面波作为测试函数，并推导其Laplace-Beltrami算子的闭式表达式，避免高阶自动微分。

【实验结果 / Results】

作者推导了球面S^(n-1)和平坦环面T^n上Laplace-Beltrami算子的显式公式，并在S^2上的双稳态Fokker-Planck方程稳态问题上进行了数值验证。实验表明该方法能够准确捕捉流形上的复杂概率分布结构，且无需任何网格离散化即可实现高效采样。

【应用价值 / Applications】

该方法适用于分子动力学、统计物理、机器学习中约束在流形上的概率推断，以及机器人学中的构型空间规划等场景。其无网格特性使其特别适合高维或复杂几何流形上的演化方程求解，为物理信息神经网络在弯曲空间中的应用提供了新工具。
