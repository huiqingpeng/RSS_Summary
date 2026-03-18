---
title: "EvoIQA - Explaining Image Distortions with Evolved White-Box Logic"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15887"
published: "2026-03-18"
summarized: "2026-03-18T17:19:16.999577"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出EvoIQA，一种基于遗传编程（Genetic Programming）的可解释符号回归框架，用于图像质量评估（IQA）。该框架能够进化出显式、人类可读的数学公式，弥合了传统手工设计模型与缺乏可解释性的深度学习黑盒模型之间的鸿沟。实验表明，进化得到的GP模型不仅优于传统手工指标，还能达到与最先进深度学习模型（如DB-CNN）相当的性能，证明了无需牺牲可解释性即可获得顶尖性能。

【方法概述 / Method】
EvoIQA采用遗传编程进行符号回归，从VSI、VIF、FSIM和HaarPSI等经典IQA指标的终端集合中自动搜索最优数学表达式。该方法将结构退化、色度变化和信息论损失等图像失真类型映射为可观测的数学方程，实现完全白盒化的质量评估。

【实验结果 / Results】
进化得到的GP模型在预测与人类视觉偏好之间表现出高度一致性，显著超越传统手工设计指标。在性能上，EvoIQA与复杂的深度学习模型DB-CNN达到同等水平，同时保持了完全的可解释性。

【应用价值 / Applications】
EvoIQA适用于需要透明决策过程的图像质量评估场景，如医学影像诊断、自动驾驶视觉系统验证、以及图像处理算法的质量监控。其可解释的数学公式有助于工程师理解失真机制、调试算法，并满足高风险应用中对AI可解释性的监管要求。
