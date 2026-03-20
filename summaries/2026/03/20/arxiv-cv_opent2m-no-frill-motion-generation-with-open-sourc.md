---
title: "OpenT2M: No-frill Motion Generation with Open-source,Large-scale, High-quality Data"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18623"
published: "2026-03-20"
summarized: "2026-03-20T15:13:16.802426"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了OpenT2M，一个百万级、高质量、开源的人体动作数据集，包含超过2800小时的人体运动数据，并通过物理可行性验证和多粒度过滤进行严格质量控制，同时配有详细的逐秒文本标注。基于该数据集，作者开发了MonoFrill预训练动作模型，其核心组件2D-PRQ是一种新颖的动作分词器，通过将人体划分为生物学部位来捕捉时空依赖关系。实验表明，OpenT2M显著提升了现有文本到动作生成模型的泛化能力，而2D-PRQ在重建质量和零样本性能方面表现优异。

【方法概述 / Method】
作者构建了自动化数据管道，包括物理可行性验证、多粒度质量过滤以及长时序序列生成流程，以创建大规模高质量动作数据集。MonoFrill模型采用2D-PRQ（2D Part-Reconstruction Quantization）作为核心分词器，将人体按生物学结构划分为多个部位，以有效建模空间和时间依赖关系，整体设计简洁无复杂技巧。

【实验结果 / Results】
OpenT2M数据集显著增强了现有文本到动作生成模型在未见文本描述上的泛化能力。2D-PRQ分词器在动作重建任务中实现了优越性能，并展现出强大的零样本学习能力，证明了简单设计配合高质量数据的有效性。

【应用价值 / Applications】
该研究为动画制作和机器人控制等领域提供了高质量开源数据资源和简洁有效的预训练模型，降低了文本到动作生成技术的开发门槛。OpenT2M有望解决该领域长期存在的数据质量和基准测试挑战，推动相关技术的标准化和产业化应用。
