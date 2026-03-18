---
title: "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15618"
published: "2026-03-18"
summarized: "2026-03-18T19:05:35.970664"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文系统分析了视觉-语言-动作（VLA）模型在动作生成过程中视觉token敏感性随层深递减的问题，发现深层网络对视觉信息的利用不足。基于此观察，作者提出DeepVision-VLA框架，通过Vision-Language Mixture-of-Transformers（VL-MoT）实现视觉基础模型与VLA骨干网络的共享注意力机制，并将多级视觉特征注入深层网络；同时引入Action-Guided Visual Pruning（AGVP）技术，利用浅层注意力剪枝无关视觉token。该模型在模拟和真实世界任务上分别超越先前最优方法9.0%和7.5%。

【方法概述 / Method】

论文采用Vision-Language Mixture-of-Transformers（VL-MoT）架构，使视觉基础模型与VLA骨干网络共享注意力机制，从而将视觉专家的多层级特征注入VLA网络的深层。此外，设计Action-Guided Visual Pruning（AGVP）模块，利用浅层注意力分数识别并保留任务相关的视觉token，剪除无关区域，以最小计算开销强化关键视觉线索。

【实验结果 / Results】

DeepVision-VLA在模拟机器人操作任务上较先前最优方法提升9.0%，在真实世界任务上提升7.5%，显著改善了复杂精细操作任务的性能。实验验证了深层视觉特征注入和注意力引导剪枝策略的有效性，表明增强深层网络视觉表征对VLA模型至关重要。

【应用价值 / Applications】

该研究为机器人灵巧操作、家庭服务机器人及工业自动化等需要精确视觉-动作协调的场景提供了更可靠的VLA模型设计范式。通过揭示视觉信息在VLA网络中的传播机制并提出针对性增强方案，为开发高效、鲁棒的具身智能系统提供了理论指导和实践参考。
