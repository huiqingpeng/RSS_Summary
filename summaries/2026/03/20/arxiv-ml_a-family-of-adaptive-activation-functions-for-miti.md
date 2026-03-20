---
title: "A Family of Adaptive Activation Functions for Mitigating Failure Modes in Physics-Informed Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18328"
published: "2026-03-20"
summarized: "2026-03-20T12:10:45.189260"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对物理信息神经网络（PINNs）中常见的训练失败模式，提出了一族基于小波的自适应激活函数。该激活函数通过将可训练的小波函数与可训练或固定的双曲正切（tanh）和softplus函数相结合，显著提升了训练稳定性和表达能力。研究在四类代表性偏微分方程（PDE）上系统评估了五种不同的激活函数变体，结果表明其相比传统激活函数具有更强的鲁棒性和精度，并在与基线PINNs、PINNsFormer等Transformer架构及其他深度学习模型的直接对比中验证了其有效性和通用性。

【方法概述 / Method】
本研究将小波函数与经典激活函数（tanh/softplus）相结合，设计了五种自适应激活函数变体，包括可训练小波与固定/可训练经典函数的组合形式。这些激活函数被嵌入PINN框架中，通过端到端训练自动调整小波参数以适应不同PDE问题的频谱特性。

【实验结果 / Results】
实验在四类代表性PDE（包括波动方程、热方程等）上进行，全面比较显示所提方法在训练稳定性和求解精度上均优于传统激活函数（如tanh、ReLU）。与PINNsFormer等先进架构的直接对比进一步证明了该方法的有效性和广泛适用性，具体性能提升通过柱状图进行了可视化展示。

【应用价值 / Applications】
该研究为科学计算和工程仿真中的PDE求解提供了更可靠的神经网络工具，特别适用于需要高频信息捕捉的复杂物理系统建模。自适应小波激活函数可集成到现有PINN框架中，提升计算流体力学、结构力学、电磁学等领域的仿真精度和训练效率，降低对人工调参的依赖。
