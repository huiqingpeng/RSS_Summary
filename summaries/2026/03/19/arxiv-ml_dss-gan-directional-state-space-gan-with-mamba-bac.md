---
title: "DSS-GAN: Directional State Space GAN with Mamba backbone for Class-Conditional Image Synthesis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17637"
published: "2026-03-19"
summarized: "2026-03-19T12:15:14.239420"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DSS-GAN，首个采用Mamba作为分层生成器骨干网络的生成对抗网络，用于噪声到图像的合成任务。核心贡献是方向性潜在路由（DLR）机制，该机制将潜在向量分解为方向特定的子向量，每个子向量与类别嵌入联合投影，以产生对应Mamba扫描的特征级仿射调制。与注入全局信号的传统类别条件化不同，DLR将类别身份和潜在结构沿着特征图的不同空间轴耦合，并在所有生成尺度上一致应用。实验表明，DSS-GAN在多个测试数据集上的FID、KID和精确率-召回率分数均优于StyleGAN2-ADA。潜在空间分析显示，方向性子向量表现出可测量的专业化特征：沿单个分量的扰动会在合成图像中产生结构化、方向相关的变化。

【方法概述 / Method】
DSS-GAN采用Mamba状态空间模型作为生成器的分层骨干网络，替代传统的卷积或Transformer架构。关键创新是方向性潜在路由（DLR）条件化机制，通过将潜在向量分解为多个方向特定子向量，并与类别嵌入联合投影，实现对Mamba扫描的特征级仿射调制，从而在特征图的不同空间轴上解耦类别身份与潜在结构信息。

【实验结果 / Results】
DSS-GAN在多个数据集上的定量评估中，FID（Fréchet Inception Distance）、KID（Kernel Inception Distance）以及精确率-召回率指标均优于StyleGAN2-ADA这一强基线方法。定性分析表明，DLR机制使方向性子向量具有可解释的专业化特性，对特定方向子向量的扰动能产生对应方向的结构化图像变化。

【应用价值 / Applications】
该研究为类别条件图像合成提供了新的架构范式，Mamba骨干的高效线性复杂度特性使其适用于高分辨率图像生成场景。方向性潜在路由机制带来的可解释潜在空间结构，有助于实现更精细的图像编辑和控制，可应用于数字内容创作、虚拟现实、数据增强等需要可控生成能力的领域。
