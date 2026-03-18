---
title: "Physics-Informed Neural Systems for the Simulation of EUV Electromagnetic Wave Diffraction from a Lithography Mask"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15584"
published: "2026-03-18"
summarized: "2026-03-18T17:08:19.869187"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了用于求解极紫外（EUV）电磁波从现代光刻掩模衍射问题的物理信息神经网络（PINNs）和神经算子（NOs）。研究引入了一种新颖的混合波导神经算子（WGNO）架构，将波导方法中计算最昂贵的组件替换为神经网络。实验表明，PINNs和神经算子在13.5 nm和11.2 nm波长下达到了与现有数值求解器相当的精度，同时显著减少了预测时间，其中WGNO架构达到了最先进的性能。

【方法概述 / Method】
论文采用物理信息神经网络（PINNs）和神经算子（NOs）两类深度学习方法，并创新性地提出混合波导神经算子（WGNO）——一种将传统波导方法与神经网络相结合的混合架构，用神经网络替代原方法中计算成本最高的组件。这些方法被用于求解麦克斯韦方程组描述的EUV电磁波衍射问题。

【实验结果 / Results】
在具有精确解析解的基准问题上，PINNs和神经算子的精度与推理时间均与现代数值求解器进行了对比评估。针对13.5 nm和11.2 nm波长的数值实验显示，所提方法在2D和3D真实掩模上达到了有竞争力的精度，推理速度显著提升；WGNO架构实现了最先进的性能。神经算子表现出显著的泛化能力，对未见过的问题参数仍能保持接近训练集的求解精度。

【应用价值 / Applications】
该研究为下一代光刻掩模的设计和优化工作流程提供了高效加速方案，可大幅缩短半导体制造中掩模仿真与优化的周期。研究成果对极紫外光刻（EUV lithography）领域具有重要价值，有助于推动先进制程芯片的开发，降低计算成本并提升设计迭代效率。
