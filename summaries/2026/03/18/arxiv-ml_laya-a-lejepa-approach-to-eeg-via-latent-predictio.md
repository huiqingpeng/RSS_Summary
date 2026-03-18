---
title: "Laya: A LeJEPA Approach to EEG via Latent Prediction over Reconstruction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16281"
published: "2026-03-18"
summarized: "2026-03-18T15:42:36.331092"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Laya，首个基于LeJEPA（Latent Joint Embedding Predictive Architecture）的EEG基础模型。研究指出，现有EEG基础模型依赖信号重建作为自监督学习目标，导致表征偏向高方差伪影而非任务相关的神经结构。Laya通过潜在空间预测而非原始信号重建来学习可迁移的EEG表征，在线性探测设置下相比基于重建的基线模型展现出更优性能，为学习高层级EEG表征提供了新方向。

【方法概述 / Method】
Laya采用LeJEPA框架进行自监督学习，通过预测潜在空间中的表征而非重建原始EEG信号。该方法利用联合嵌入架构，在潜在空间执行预测任务，避免了传统重建目标对噪声和伪影的过度关注，同时继承了LeJEPA的稳定训练特性而无需额外启发式技巧。

【实验结果 / Results】
在多个EEG基准数据集上，Laya在线性探测（linear probing）条件下相比基于重建的自监督基线模型实现了性能提升。实验结果表明，潜在预测目标能够有效学习可迁移的高层EEG表征，且对下游任务的适应能力更强，减少了对精细微调策略的依赖。

【应用价值 / Applications】
Laya可广泛应用于临床神经科学诊断、脑机接口（BCI）系统以及大规模EEG数据分析。该方法为开发更鲁棒的EEG基础模型提供了新范式，有助于降低下游任务对大量标注数据和复杂微调策略的依赖，推动EEG在医疗监测和神经工程中的实际部署。
