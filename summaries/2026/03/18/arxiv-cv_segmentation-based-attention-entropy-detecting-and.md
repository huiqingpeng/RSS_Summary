---
title: "Segmentation-Based Attention Entropy: Detecting and Mitigating Object Hallucinations in Large Vision-Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16558"
published: "2026-03-18"
summarized: "2026-03-18T18:15:01.420347"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种基于分割的注意力熵（Segmentation-based Attention Entropy, SAE）方法，用于检测和缓解大型视觉语言模型（LVLMs）中的物体幻觉问题。与传统研究关注文本模态不同，作者发现视觉模态中的异常注意力模式同样会导致幻觉现象。SAE利用语义分割在物体级语义空间中量化视觉注意力不确定性，并基于此设计了幻觉检测的可靠性分数以及SAE引导的注意力调整方法，在无需额外训练的情况下显著降低物体幻觉，提升LVLM驱动的感知与决策可信度。

【方法概述 / Method】

该方法首先通过语义分割将图像划分为物体级别的语义区域，然后计算视觉注意力在这些区域上的分布熵（即SAE），以量化模型对特定物体的注意力不确定性。基于SAE，论文设计了双重机制：一是可靠性评分用于幻觉检测，二是推理时的注意力调整策略，通过修改视觉注意力分布来缓解幻觉。

【实验结果 / Results】

实验在公开基准测试和真实具身多模态场景（四足机器人）中验证了该方法的有效性。结果表明，SAE能够在零额外训练成本的情况下显著减少物体幻觉，提升LVLM输出可靠性，且在真实机器人感知与决策任务中展现出良好的泛化能力。

【应用价值 / Applications】

该方法可直接部署于现有的LVLM推理流程中，无需重新训练模型，适用于需要高可靠性的视觉理解场景，如自动驾驶感知、机器人导航与操作、医疗影像分析等。特别是在具身智能领域，SAE为四足机器人等平台的可信视觉语言交互提供了实用解决方案，降低了幻觉导致的决策风险。
