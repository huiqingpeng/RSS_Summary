---
title: "Reconstruction Matters: Learning Geometry-Aligned BEV Representation through 3D Gaussian Splatting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19193"
published: "2026-03-20"
summarized: "2026-03-20T16:05:28.519070"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出Splat2BEV框架，通过3D高斯溅射（3D Gaussian Splatting）显式重建3D场景，以学习几何对齐的BEV表征。该方法突破了传统端到端BEV感知将整个过程视为黑盒、缺乏显式3D几何理解的局限，使BEV特征同时具备丰富的语义信息和精确的几何结构。在nuScenes和Argoverse数据集上的实验表明，该框架达到了最先进的性能，验证了显式3D重建对BEV感知的有效性。

【方法概述 / Method】
Splat2BEV首先预训练一个高斯生成器，从多视角输入显式重建3D场景，生成几何对齐的特征表征；然后将这些表征投影到BEV空间，作为下游任务的输入。该方法通过重建任务引入显式几何监督，弥补了传统端到端训练缺乏3D几何约束的不足。

【实验结果 / Results】
在nuScenes和Argoverse数据集上进行的大量实验表明，Splat2BEV在BEV感知任务上达到了最先进的性能。实验结果验证了引入显式3D重建能够有效提升BEV表征的几何精度和语义丰富度，从而改善下游任务的感知效果。

【应用价值 / Applications】
该研究可直接应用于自动驾驶系统中的BEV感知模块，提升语义分割、3D目标检测和运动预测等关键任务的准确性和可靠性。通过显式几何重建增强可解释性，有助于自动驾驶系统在安全关键场景下的决策验证和故障诊断，推动更安全可靠的自动驾驶技术发展。
