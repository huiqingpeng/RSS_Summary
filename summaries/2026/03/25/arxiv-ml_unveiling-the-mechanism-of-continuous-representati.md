---
title: "Unveiling the Mechanism of Continuous Representation Full-Waveform Inversion: A Wave Based Neural Tangent Kernel Framework"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22362"
published: "2026-03-25"
summarized: "2026-03-26T07:13:35.184526"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究针对全波形反演（FWI）中连续表示方法（CR-FWI）的理论机制展开深入分析。通过扩展神经正切核（NTK）理论，建立了适用于FWI的波基NTK框架，揭示了CR-FWI减轻初始模型依赖性的根本原因——波基NTK的特征值衰减特性。基于该理论洞察，作者提出了多种具有定制化特征值衰减特性的CR-FWI方法，特别是结合隐式神经表示（INR）与多分辨率网格的混合表示方法IG-FWI，在多个标准地质模型上验证了其优越性能。

【方法概述 / Method】

作者将标准神经正切核（NTK）理论扩展至波动方程约束的优化问题，建立了波基NTK分析框架。该框架通过推导波基NTK在初始化和训练过程中的动态变化特性，定量刻画了不同网络表示（INR、多分辨率网格及其组合）对应的特征值衰减行为，并据此设计了具有可控收敛特性的混合表示架构IG-FWI。

【实验结果 / Results】

在Marmousi、2D SEG/EAGE Salt、Overthrust、2004 BP及2014 Chevron等多个地质勘探标准模型上的实验表明，所提出的IG-FWI方法相较于传统FWI和现有INR-based FWI方法具有更优的性能，实现了模型鲁棒性与高频收敛速度之间的更好平衡。理论分析准确预测了不同表示方法的收敛行为，与实验观测高度一致。

【应用价值 / Applications】

该研究为地震勘探、医学成像和无损检测等领域的FWI应用提供了系统的理论指导，特别是解决了传统FWI对初始模型敏感、INR-based方法高频收敛慢等关键瓶颈。所发展的波基NTK框架可推广至其他基于物理神经网络的逆问题求解，为物理信息机器学习（Physics-Informed ML）的理论分析和算法设计开辟了新途径。
