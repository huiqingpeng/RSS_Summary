---
title: "Deformation-Invariant Neural Network and Its Applications in Distorted Image Restoration and Analysis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2310.02641"
published: "2026-03-18"
summarized: "2026-03-18T18:24:14.080654"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了形变不变神经网络（Deformation-Invariant Neural Network, DINN），用于解决几何形变图像的成像任务挑战。DINN通过引入拟共形变换网络（QCTN）组件，能够为几何形变但内容相同的图像输出一致的潜在特征。该框架在图像分类、大气湍流和水下湍流图像恢复以及人脸识别验证等任务中均取得了优于现有GAN方法的性能。

【方法概述 / Method】
DINN的核心是拟共形变换网络（QCTN），该网络输出一个拟共形映射，可将几何形变图像转换为接近自然图像分布的改进版本。QCTN首先输出Beltrami系数来衡量输出变形映射的拟共形性，通过控制该系数实现对局部几何形变的调控。QCTN结构轻量简洁，可方便地集成到现有深度神经网络中。

【实验结果 / Results】
在大气湍流和水下湍流图像恢复任务中，DINN优于现有的基于GAN的恢复方法。在几何形变图像分类任务中，DINN实现了对形变图像的准确分类。此外，在大气湍流下的人脸1:1验证任务中，DINN也取得了令人满意的性能，验证了该框架的有效性。

【应用价值 / Applications】
该研究可应用于恶劣成像环境下的图像恢复与分析，如大气光学湍流导致的远距离成像退化、水下成像中的水流扰动等场景。其人脸识别验证能力可拓展至安防监控、遥感观测等领域。DINN的模块化设计使其能够增强现有深度学习模型对几何形变的鲁棒性，具有广泛的工程应用潜力。
