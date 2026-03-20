---
title: "Cross-Modal Rationale Transfer for Explainable Humanitarian Classification on Social Media"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18611"
published: "2026-03-20"
summarized: "2026-03-20T16:09:02.321618"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种可解释的多模态分类框架，用于社交媒体的人道主义危机信息分类。该方法通过视觉语言Transformer学习文本和图像的联合表示，并创新性地实现跨模态推理迁移——从文本推理中提取图像推理，从而减少标注成本。实验表明，该方法在CrisisMMD数据集上将分类Macro-F1提升2-35%，且人类评估显示其检索的图像推理块质量提高12%，在零样本场景下对新数据集也能达到80%的准确率。

【方法概述 / Method】
论文采用"可解释设计"的多模态框架：首先利用视觉语言Transformer（如CLIP）编码文本-图像联合表示并提取文本推理（关键token），然后通过跨模态映射将文本推理迁移为图像推理（关键patches），最后基于提取的双模态推理进行分类决策。核心创新在于通过文本-图像关联实现单模态到多模态的推理知识迁移。

【实验结果 / Results】
在CrisisMMD基准数据集上，该方法相比基线将Macro-F1分数提升2-35%，同时准确提取文本token和图像patch作为推理依据；人类评估显示其图像推理块的质量比对比方法高12%；零样本迁移实验中，模型在未见过的新数据集上仍能达到80%的分类准确率，展现出良好的泛化能力。

【应用价值 / Applications】
该方法适用于灾害响应、人道主义救援等实时危机监测场景，帮助救援人员快速理解模型决策依据（如为何某条推文被标记为"基础设施损坏"），提升AI系统的透明度和可信度；跨模态推理迁移机制可扩展至其他缺乏图像标注资源的领域，降低多模态可解释模型的开发成本。
