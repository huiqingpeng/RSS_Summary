---
title: "VISER: Visually-Informed System for Enhanced Robustness in Open-Set Iris Presentation Attack Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17859"
published: "2026-03-19"
summarized: "2026-03-19T16:17:38.729856"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了人类感知先验在开放集虹膜呈现攻击检测（PAD）中的应用，比较了多种显著性引导方法（包括手工标注、眼动追踪热图、分割掩码和DINOv2嵌入）与深度学习基线方法的性能。实验结果表明，去噪后的眼动追踪热图在开放集PAD任务中展现出最佳的泛化能力，在AUROC和APCER@BPCER=1%指标上均优于交叉熵基线。研究还提供了训练好的模型、代码和显著性图以促进后续研究。

【方法概述 / Method】
论文系统性地比较了四种人类显著性信息形式：手工鼠标点击标注、眼动追踪热图、分割掩码以及自监督视觉模型DINOv2的嵌入特征，并将其用于指导深度神经网络的训练。研究采用留一攻击类型（leave-one-attack-type-out）的开放集评估范式，测试模型对未见攻击类型的泛化能力。

【实验结果 / Results】
去噪眼动追踪热图在开放集虹膜PAD任务中表现最优，相比标准交叉熵训练在AUROC和APCER@BPCER=1%指标上均取得显著提升。相比之下，手工标注和DINOv2嵌入的效果较弱，而分割掩码的表现介于中间。结果表明，人类视觉注意力的连续分布信息比离散标注更适合引导模型学习对攻击检测关键的区域特征。

【应用价值 / Applications】
该研究为虹膜生物识别系统的安全性提升提供了新思路，特别是在应对未知类型呈现攻击（如新型隐形眼镜、打印攻击等）的场景中具有重要价值。所提出的显著性引导训练方法可增强虹膜PAD模型在实际部署中的鲁棒性，适用于高安全需求的应用场景如边境管控、金融身份认证等，且研究开源资源有助于推动该领域的标准化和可重复性研究。
