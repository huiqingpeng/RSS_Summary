---
title: "SemanticFace: Semantic Facial Action Estimation via Semantic Distillation in Interpretable Space"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.14827"
published: "2026-03-19"
summarized: "2026-03-19T17:04:08.628310"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SemanticFace框架，用于在可解释的ARKit blendshape空间中估计面部表情动作，将系数预测重新表述为结构化语义推理问题。该框架采用两阶段语义蒸馏范式：首先从真实ARKit系数中提取结构化语义监督信号，然后将这些知识蒸馏到多模态大语言模型中以预测可解释的面部动作系数。实验表明，语言对齐的语义监督不仅提高了系数准确性和感知一致性，还实现了强大的跨身份泛化能力，并对包括卡通人脸在内的显著域迁移具有鲁棒性。

【方法概述 / Method】
SemanticFace采用两阶段语义蒸馏方法：第一阶段从真实ARKit blendshape系数中派生结构化语义监督，第二阶段将这些语义知识蒸馏到多模态大语言模型（MLLM）中。该方法将传统的直接系数预测转化为基于语义推理的预测过程，利用语言模型的语义理解能力来增强面部动作估计的可解释性。

【实验结果 / Results】
实验结果显示，引入语言对齐的语义监督显著提升了系数预测准确性和感知一致性。该方法展现出优异的跨身份泛化性能，即使在面对大幅域迁移（如卡通风格人脸）时仍保持鲁棒性，证明了语义蒸馏策略在提升模型泛化能力方面的有效性。

【应用价值 / Applications】
该研究可直接应用于虚拟形象（avatar）控制和自然人机交互系统，为需要精确、可解释面部动作表示的场景提供解决方案。由于ARKit blendshape是业界广泛采用的面部动画标准，该方法具有良好的实用性和兼容性，可支持从真实人脸到风格化卡通角色的跨域面部动画生成。
