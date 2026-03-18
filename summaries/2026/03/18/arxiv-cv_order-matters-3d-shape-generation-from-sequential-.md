---
title: "Order Matters: 3D Shape Generation from Sequential VR Sketches"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.04761"
published: "2026-03-18"
summarized: "2026-03-18T18:30:10.251203"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了VRSketch2Shape，首个从序列化VR草图生成3D形状的框架及多类别数据集。研究指出现有草图到形状模型忽略了笔触的时间顺序，丢失了关于结构和设计意图的关键信息。该框架通过顺序感知编码器和扩散生成器，实现了比先前工作更高的几何保真度，并能从合成数据有效泛化到真实手绘草图，即使在部分草图情况下也表现良好。

【方法概述 / Method】
论文开发了自动化流水线从任意形状生成序列化VR草图，构建了包含2万多合成样本和900多手绘样本的四类别数据集。核心方法采用顺序感知的草图编码器（order-aware sketch encoder）结合基于扩散的3D生成器，显式建模笔触绘制的时间序列信息。

【实验结果 / Results】
该方法在几何保真度上超越现有方法，仅需少量监督即可从合成数据泛化到真实手绘草图，且在部分草图（partial sketches）条件下仍保持稳健性能。具体指标未在摘要中详述，但强调了跨域泛化能力和对不完整输入的鲁棒性。

【应用价值 / Applications】
该研究为VR环境下的快速3D概念设计和迭代提供了直观工具，可替代传统CAD工作流程，适用于产品设计、建筑草图、游戏资产创建等领域。开源的数据集和模型将促进VR草图理解与生成的进一步研究。
