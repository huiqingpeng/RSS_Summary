---
title: "SpikeCLR: Contrastive Self-Supervised Learning for Few-Shot Event-Based Vision using Spiking Neural Networks"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16338"
published: "2026-03-18"
summarized: "2026-03-18T18:11:02.580622"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SpikeCLR，首个面向事件相机的脉冲神经网络（SNN）对比自监督学习框架，旨在解决事件视觉领域标注数据稀缺的问题。该框架通过代理梯度训练将帧级对比学习方法适配到脉冲域，并设计了一套针对事件数据的空间、时间和极性变换增强策略。实验表明，在低数据场景下，自监督预训练结合微调的范式显著优于监督学习，且学习到的表征具有跨数据集迁移能力。

【方法概述 / Method】
SpikeCLR采用基于InfoNCE的对比学习框架，使用代理梯度训练实现SNN的端到端优化。核心创新在于设计了事件专属的数据增强策略，包括空间变换（随机裁剪、翻转）、时间变换（时间重采样、时间翻转）和极性变换（极性反转、极性丢弃），以学习事件数据的时空不变性表征。

【实验结果 / Results】
在CIFAR10-DVS、N-Caltech101、N-MNIST和DVS-Gesture四个基准数据集上，SpikeCLR在少样本（few-shot）和半监督设置下均取得一致的性能提升。消融研究表明，空间与时间增强的组合对学习有效的时空不变性至关重要，且预训练获得的表征可跨不同事件数据集迁移。

【应用价值 / Applications】
该研究为资源受限的嵌入式神经形态系统提供了高效的事件视觉解决方案，特别适用于高速感知、机器人导航、自动驾驶等标注成本高昂或难以获取的场景。通过自监督预训练降低对大规模标注数据的依赖，推动了事件相机与SNN在边缘计算设备上的实际部署。
