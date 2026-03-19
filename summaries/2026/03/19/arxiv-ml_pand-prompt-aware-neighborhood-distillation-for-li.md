---
title: "PAND: Prompt-Aware Neighborhood Distillation for Lightweight Fine-Grained Visual Classification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.07768"
published: "2026-03-19"
summarized: "2026-03-19T14:18:42.090371"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出PAND（Prompt-Aware Neighborhood Distillation），一种面向细粒度视觉分类（FGVC）的两阶段知识蒸馏框架，旨在解决从大型视觉-语言模型（VLMs）向轻量网络蒸馏时固定提示和全局对齐的局限性。该方法通过提示感知语义校准生成自适应语义锚点，并引入邻域感知结构蒸馏策略约束学生网络的局部决策结构。实验表明，PAND在四个FGVC基准上持续超越最先进方法，其中ResNet-18学生在CUB-200数据集上达到76.09%的准确率，较强基线VL2Lite提升3.4%。

【方法概述 / Method】
PAND采用两阶段解耦设计：第一阶段通过Prompt-Aware Semantic Calibration动态生成与输入相关的自适应语义锚点，替代传统固定提示；第二阶段实施邻域感知的结构蒸馏，通过约束学生网络在特征空间中的局部邻域关系来保持教师模型的决策结构，而非仅进行全局特征对齐。

【实验结果 / Results】
PAND在四个FGVC基准数据集上取得一致的性能提升，ResNet-18作为学生网络在CUB-200上达到76.09%的分类准确率，显著超越VL2Lite基线3.4个百分点，证明了该方法在轻量模型上实现高效知识迁移的有效性。

【应用价值 / Applications】
该研究为资源受限场景下的细粒度视觉识别提供了高效解决方案，可广泛应用于移动端鸟类/车型/飞机型号识别、零售商品细分类、医学影像病灶分型等需要轻量模型部署且类别区分度高的实际任务，同时其提示自适应机制也为视觉-语言模型的领域适配提供了新思路。
