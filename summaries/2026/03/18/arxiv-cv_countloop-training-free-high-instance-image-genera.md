---
title: "CountLoop: Training-Free High-Instance Image Generation via Iterative Agent Guidance"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2508.16644"
published: "2026-03-18"
summarized: "2026-03-18T18:26:56.650924"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了COUNTLOOP，一种无需训练的迭代式高实例图像生成框架，解决了扩散模型在精确控制物体数量（尤其是高密度场景）方面的难题。该方法通过视觉语言模型（VLM）驱动的规划器生成结构化场景布局，并由VLM评判器对物体数量、空间排列和视觉质量提供显式反馈以迭代优化。实验表明，COUNTLOOP在多个基准测试上将计数误差降低高达57%，同时保持最高的空间质量分数和照片级真实感。

【方法概述 / Method】
COUNTLOOP采用"合成-评估"交替的迭代架构：VLM规划器根据文本提示生成包含物体数量、位置和类别的结构化布局，VLM评判器则分析生成图像并输出具体改进建议。为增强控制精度，该方法引入实例驱动的注意力掩码和累积注意力组合机制，有效避免语义泄露并确保密集遮挡场景中的物体分离。

【实验结果 / Results】
在COCO-Count、T2I-CompBench及两个新建的高实例基准测试中，COUNTLOOP将计数误差最高降低57%，并在所有基准上取得最高或可比的空间质量得分。该方法在保持照片级真实感的同时，显著优于现有无需训练的方法，且性能接近甚至超过部分需要训练的方法。

【应用价值 / Applications】
COUNTLOOP可广泛应用于需要精确物体控制的图像生成场景，如电商产品展示、建筑可视化、数据增强和机器人仿真环境生成等。其无需训练的特性使其能够快速部署到现有扩散模型上，降低了实际应用门槛，为自动化内容创作提供了可靠的实例级控制能力。
