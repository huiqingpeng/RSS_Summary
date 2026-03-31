---
title: "The Geometric Cost of Normalization: Affine Bounds on the Bayesian Complexity of Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27432"
published: "2026-03-31"
summarized: "2026-04-01T07:24:07.534905"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究揭示了归一化层对神经网络贝叶斯复杂度的几何约束效应。作者证明LayerNorm的均值中心化操作将数据限制在过原点的线性超平面上，导致后续权重矩阵的局部学习系数（LLC）精确降低m/2（m为输出维度）；而RMSNorm的球面投影则完全保留LLC。该效应由数据流形几何结构决定，与训练无关——对于余维一流形，任何非零曲率即可保留LLC，仅仿射平坦流形会导致下降。有限样本下该阈值呈现平滑过渡，过渡宽度取决于实际经历曲率的数据比例。

【方法概述 / Method】

研究采用奇异学习理论（Singular Learning Theory）中的局部学习系数（LLC）作为模型复杂度度量，通过分析归一化层输出的几何流形结构（超平面vs球面），建立归一化类型与LLC的解析关系。核心工具包括：对LayerNorm和RMSNorm输出流形的微分几何刻画，以及基于wrLLC框架的仿射对称性扩展定理。

【实验结果 / Results】

受控的单层缩放实验验证了理论预测：LayerNorm导致m/2的LLC下降，RMSNorm无下降；Softmax单纯形数据与显式下游偏置配对时，通过"偷运偏置"机制激活相同的m/2 LLC下降，该预测经仿射对称性扩展定理证明并获实验确认。有限样本下观测到曲率依赖的平滑交叉过渡行为。

【应用价值 / Applications】

该研究为神经网络架构设计提供了归一化层选择的理论依据：需高模型容量时应避免LayerNorm的均值中心化（如小样本学习），而追求泛化或计算效率时可利用其隐式正则化效应。此外，对Softmax输出与偏置交互的分析对Transformer等架构的优化具有指导意义。
