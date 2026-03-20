---
title: "Learning Transferable Friction Models and LuGre Identification Via Physics-Informed Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2504.12441"
published: "2026-03-20"
summarized: "2026-03-20T14:15:31.826328"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种基于物理信息神经网络（PINN）的摩擦估计框架，将经典摩擦模型（如LuGre模型）与可学习组件相结合，仅需少量通用测量数据即可实现物理一致性的摩擦建模。研究在欠驱动非线性系统上验证了该方法，证明其仅用小型噪声数据集就能高精度复现动态摩擦特性，显著优于MuJoCo和PyBullet等机器人仿真器中常用的简化模型。关键的是，学习得到的摩擦模型具有跨系统迁移能力，可泛化到未训练的系统上。

【方法概述 / Method】

该方法采用物理信息神经网络架构，将LuGre等经典摩擦模型的物理约束嵌入神经网络损失函数中，确保学习过程满足物理一致性。框架通过结合解析摩擦模型的结构先验与数据驱动的神经网络表达能力，在保持模型可解释性的同时捕捉复杂摩擦现象。

【实验结果 / Results】

实验表明，该方法在小型噪声数据集上训练的摩擦模型，其动态摩擦特性复现精度显著高于传统机器人仿真器中的简化摩擦模型。核心发现是 learned friction models 可实现跨系统迁移，即在一个系统上训练的模型能够准确预测其他未训练系统的摩擦行为。

【应用价值 / Applications】

该研究为机器人仿真与控制的摩擦建模提供了可扩展、可解释的解决方案，特别适用于复杂欠驱动任务的摩擦补偿。迁移学习能力大幅降低了为新系统重新建模摩擦的成本，有望缩小仿真与现实之间的性能差距（sim-to-real gap），提升机器人控制系统的实际部署效果。
