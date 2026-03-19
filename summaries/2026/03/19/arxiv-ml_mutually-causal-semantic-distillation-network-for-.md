---
title: "Mutually Causal Semantic Distillation Network for Zero-Shot Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17412"
published: "2026-03-19"
summarized: "2026-03-19T13:12:07.361040"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对零样本学习（ZSL）中视觉特征与属性特征之间潜在语义知识推断的关键挑战，提出了一种互因果语义蒸馏网络（MSDN++）。该方法通过双向因果注意力机制，分别学习基于属性的视觉特征和基于视觉的属性特征，有效克服了现有单向弱监督方法只能捕获虚假有限语义表示的缺陷。在CUB、SUN、AWA2和FLO等标准数据集上的实验表明，MSDN++显著优于强基线方法，达到了新的最优性能。

【方法概述 / Method】
MSDN++包含两个互因果注意力子网络：属性→视觉因果注意力子网络学习基于属性的视觉特征，视觉→属性因果注意力子网络学习基于视觉的属性特征。两个子网络通过因果注意力机制建立可靠的视觉-属性因果关联，并在语义蒸馏损失的指导下实现协同学习与相互教学。

【实验结果 / Results】
本文在四个广泛使用的基准数据集（CUB、SUN、AWA2、FLO）上进行了大量实验，结果表明MSDN++相比强基线方法取得了显著提升，达到了新的最优性能（state-of-the-art）。

【应用价值 / Applications】
该研究可应用于开放世界场景下的图像分类任务，如野生动物识别、细粒度物种分类等缺乏训练样本的领域，通过属性描述实现对新类别的有效识别，降低人工标注成本并提升模型的泛化能力。
