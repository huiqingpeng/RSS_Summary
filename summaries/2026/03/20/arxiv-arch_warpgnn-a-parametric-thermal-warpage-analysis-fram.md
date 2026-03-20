---
title: "WarPGNN: A Parametric Thermal Warpage Analysis Framework with Physics-aware Graph Neural Network"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.18581"
published: "2026-03-20"
summarized: "2026-03-20T12:04:28.181277"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了WarPGNN，一种基于物理感知图神经网络（GNN）的高效参数化热翘曲分析框架，用于解决系统级封装（SiP）芯粒设计和异构2.5D/3D集成中的热诱导翘曲可靠性问题。该方法通过直接在芯粒布局构建的图上运行，实现了快速的翘曲感知布局探索，并在多种封装配置间展现出强大的可迁移性。实验表明，WarPGNN相比传统有限元方法实现了超过205倍的加速，同时保持了可比拟的精度。

【方法概述 / Method】

WarPGNN首先将多芯粒布局编码为简化传递闭包图（rTCGs），然后采用基于图卷积网络（GCN）的编码器提取层次化结构特征，最后通过U-Net风格的解码器从图特征嵌入重建翘曲图。此外，为应对翘曲数据分布的长尾特性，研究者开发了物理感知损失函数，并改进了基于图同构网络（GIN）的消息传递编码器，以增强极端情况的学习性能和图嵌入的表达能力。

【实验结果 / Results】

WarPGNN相比2-D高效有限元方法实现205.91倍加速，相比3-D FEM方法COMSOL实现119,766.64倍加速，同时保持仅1.26%的全尺度归一化RMSE和2.21%的翘曲值误差。与近期基于DeepONet的模型相比，该方法在可比拟预测精度和推理加速的同时，训练时间降低3.4倍。此外，WarPGNN在未见过数据集上展现出卓越的可迁移性，归一化RMSE仅为3.69%。

【应用价值 / Applications】

该研究为先进封装设计中的热翘曲快速分析提供了实用工具，可显著加速芯粒布局探索迭代，缩短复杂2.5D/3D集成系统的设计周期。其高可迁移性使其能够适应多样化的封装配置，为半导体行业的可靠性分析和设计优化提供了高效、可扩展的解决方案。
