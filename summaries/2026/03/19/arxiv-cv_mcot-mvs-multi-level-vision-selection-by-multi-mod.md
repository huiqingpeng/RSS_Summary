---
title: "MCoT-MVS: Multi-level Vision Selection by Multi-modal Chain-of-Thought Reasoning for Composed Image Retrieval"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17360"
published: "2026-03-19"
summarized: "2026-03-19T15:09:01.671514"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对组合图像检索（CIR）任务中现有方法难以从参考图像中提取与文本修改意图相匹配的语义线索、易受无关视觉噪声干扰的问题，提出了基于多模态思维链推理的多层次视觉选择方法（MCoT-MVS）。该方法利用多模态大语言模型（MLLM）进行思维链推理，生成保留、移除和目标推断文本作为指导信号，并设计了两个参考视觉注意力选择模块分别提取判别性的块级和实例级语义，最终通过加权层次组合模块实现多粒度视觉线索与文本的融合对齐。在CIRR和FashionIQ两个基准数据集上的实验表明，该方法取得了新的最优性能。

【方法概述 / Method】
MCoT-MVS的核心方法包括三个组件：首先利用MLLM对多模态组合输入进行思维链推理，输出结构化的推理文本（retained/removed/target-inferred texts）；随后设计两个并行的视觉注意力选择模块，分别以推理文本为指导，从参考图像中选择性提取块级（patch-level）和实例级（instance-level）的视觉特征；最后通过加权层次组合模块将多粒度视觉特征与修改文本及目标描述进行融合，在统一嵌入空间中实现对齐。

【实验结果 / Results】
在CIRR和FashionIQ两个主流CIR基准数据集上的大量实验表明，MCoT-MVS一致优于现有方法并达到新的最优性能（state-of-the-art）。论文未提供具体数值指标，但强调了方法的有效性和泛化能力，相关代码和训练模型已公开发布。

【应用价值 / Applications】
该研究在电商时尚检索（如根据参考商品图和文本描述查找目标商品）、智能图像编辑与搜索、以及多模态内容推荐等场景具有重要应用价值。通过引入MLLM的推理能力和多层次视觉选择机制，该方法能够更准确地理解用户的复杂修改意图，提升检索系统的精度和用户体验。
