---
title: "Fundamental Limits of Neural Network Sparsification: Evidence from Catastrophic Interpretability Collapse"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18056"
published: "2026-03-20"
summarized: "2026-03-20T12:06:47.617903"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究揭示了神经网络极端稀疏化（90%激活削减）与可解释性之间的根本性矛盾：尽管全局表征质量保持稳定，局部特征可解释性却系统性崩溃。通过在dSprites和Shapes3D数据集上的实验，研究发现Top-k和L1两种稀疏化方法均导致大量"死亡神经元"（最高达90.6%），且延长训练无法恢复。该崩溃现象随数据集复杂度增加而加剧，表明这是压缩过程的内在特性，而非特定算法或训练条件的产物。

【方法概述 / Method】

研究采用混合变分自编码器-稀疏自编码器（VAE-SAE）架构，设计了一种自适应稀疏度调度框架，在50个训练周期内将活跃神经元从500逐步减少至50。实验对比了Top-k（硬阈值）和L1正则化（软约束）两种稀疏化方法，并在两个基准数据集（dSprites和Shapes3D）上评估特征存活情况。

【实验结果 / Results】

关键发现显示：Top-k稀疏化在dSprites和Shapes3D上分别产生34.4%和62.7%的死亡神经元率，而L1正则化结果更差（41.7%和90.6%）。额外100个周期的训练无法恢复死亡神经元，且崩溃模式对所有阈值定义均稳健。数据集复杂度显著影响崩溃程度——Shapes3D（RGB图像，6个因素）的死亡神经元率是dSprites（灰度图像，5个因素）的1.8-2.2倍。

【应用价值 / Applications】

该研究为神经网络压缩与可解释性的权衡提供了重要理论边界，警示在追求极端模型效率时可能丧失 mechanistic interpretability。这对需要高可解释性的关键应用领域（如医疗诊断、自动驾驶）具有直接指导意义，同时也为开发保持可解释性的新型稀疏化算法指明了研究方向。
