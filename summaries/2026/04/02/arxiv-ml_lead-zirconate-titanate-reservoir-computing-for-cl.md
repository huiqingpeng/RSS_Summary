---
title: "Lead Zirconate Titanate Reservoir Computing for Classification of Written and Spoken Digits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00207"
published: "2026-04-02"
summarized: "2026-04-03T07:18:36.447095"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究将物理储层计算（Reservoir Computing, RC）应用于手写数字和口语数字的分类任务，使用未极化的锆钛酸铅（PZT）立方体作为计算基底。PZT储层在MNIST手写数字数据集上达到89.0%的准确率，比逻辑回归基线提升2.4个百分点；但在AudioMNIST口语数字数据集上（88.2%准确率）与基线方法（88.1%）表现相当。研究表明，物理储层计算在中等难度任务中收益最大——即线性方法表现不佳但问题仍可学习的场景。

【方法概述 / Method】

研究采用未极化的PZT立方体作为物理储层计算基底，利用其固有的非线性动力学特性对输入数据进行高维映射和时序处理。系统通过将手写或语音数字信号转换为物理刺激作用于PZT材料，再读取其响应状态作为特征表示，最终结合数字算法完成分类。

【实验结果 / Results】

在MNIST手写数字分类任务中，PZT储层达到89.0%准确率，显著优于逻辑回归基线（86.6%）；在AudioMNIST口语数字任务中，储层系统（88.2%）与基线方法（88.1%）性能基本持平。结果表明储层计算的优势主要体现在中等复杂度任务上，而非过于简单或困难的问题。

【应用价值 / Applications】

PZT作为已广泛应用于半导体领域的成熟材料，为低功耗边缘计算提供了可与数字算法集成的物理计算基底。该研究为开发新型神经形态计算硬件、降低AI推理能耗提供了可行路径，特别适用于需要本地实时处理的物联网设备和嵌入式视觉/语音系统。
