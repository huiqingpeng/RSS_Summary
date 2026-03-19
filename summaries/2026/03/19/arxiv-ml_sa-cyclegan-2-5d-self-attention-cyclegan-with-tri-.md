---
title: "SA-CycleGAN-2.5D: Self-Attention CycleGAN with Tri-Planar Context for Multi-Site MRI Harmonization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17219"
published: "2026-03-19"
summarized: "2026-03-19T13:10:31.989954"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出SA-CycleGAN-2.5D，一种用于多中心MRI影像协调（harmonization）的域自适应框架，旨在解决不同扫描仪协议导致的强度分布偏移问题。该方法通过三重架构创新——2.5D三平面流形注入、U-ResNet生成器结合密集体素自注意力机制、以及谱归一化判别器——实现了全局强度相关性的建模。在654例胶质瘤患者的跨机构数据集（BraTS和UPenn-GBM）上，该方法将最大均值差异（MMD）降低99.1%，并使域分类器准确率降至接近随机水平（59.7%），同时保留了肿瘤病理生理学特征。

【方法概述 / Method】
SA-CycleGAN-2.5D基于Ben-David等人的HΔH散度边界理论，采用三种核心技术：（1）2.5D三平面流形注入，以O(HW)复杂度保留z轴梯度信息；（2）U-ResNet生成器配备密集体素自注意力机制，突破CNN的O(√L)有效感受野限制以建模全局扫描仪场偏差；（3）谱归一化判别器约束Lipschitz常数（K_D ≤ 1）以实现稳定的对抗优化。

【实验结果 / Results】
在BraTS和UPenn-GBM两个机构域的654例胶质瘤患者数据上，该方法将最大均值差异（MMD）从1.729降至0.015（降低99.1%），域分类器准确率降至59.7%（接近随机猜测）。消融实验表明，全局注意力机制对于异构到均质翻译方向具有统计学显著性（Cohen's d = 1.32, p < 0.001）。

【应用价值 / Applications】
该研究可实现体素级别的影像协调，在保留肿瘤病理生理学特征的同时消除扫描仪相关偏差，为多中心放射组学分析提供可重复的影像数据基础。其2.5D设计在计算效率与3D空间一致性之间取得平衡，适用于大规模多中心神经影像研究和临床放射组学应用的影像标准化预处理。
