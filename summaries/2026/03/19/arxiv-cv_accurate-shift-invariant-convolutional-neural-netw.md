---
title: "Accurate Shift Invariant Convolutional Neural Networks Using Gaussian-Hermite Moments"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17098"
published: "2026-03-19"
summarized: "2026-03-19T15:05:06.935773"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为Gaussian-Hermite Sampling (GHS)的新型下采样策略，旨在解决卷积神经网络(CNN)缺乏平移不变性的问题。GHS利用高斯-埃尔米特多项式实现平移一致性采样，使CNN层在训练前就能对任意空间平移保持不变性。实验表明，该方法在CIFAR-10、CIFAR-100和MNIST-rot数据集上实现了100%的分类一致性，同时提升了分类准确率。

【方法概述 / Method】
GHS基于高斯-埃尔米特多项式构建平移一致的采样核，替代传统CNN中的标准下采样操作（如最大池化或步长卷积）。该方法可直接嵌入现有CNN架构的层级别，无需修改网络结构或增加额外的训练流程。

【实验结果 / Results】
在CIFAR-10、CIFAR-100和MNIST-rot数据集上的评估显示，GHS实现了100%的平移分类一致性，显著优于基线CNN模型。同时，GHS在保持计算效率的同时，还提升了模型的分类准确率。

【应用价值 / Applications】
该研究适用于需要严格平移不变性的计算机视觉任务，如医学图像分析、卫星图像处理和自动驾驶中的目标检测。GHS可直接部署到现有CNN架构中，为安全关键型应用提供更可靠的预测一致性保障。
