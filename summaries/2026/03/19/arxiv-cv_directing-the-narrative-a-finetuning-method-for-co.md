---
title: "Directing the Narrative: A Finetuning Method for Controlling Coherence and Style in Story Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17295"
published: "2026-03-19"
summarized: "2026-03-19T15:07:38.052157"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种用于故事生成的两阶段微调框架，旨在解决现有方法在角色身份一致性和视觉风格连贯性方面的不足。核心创新包括Group-Shared Attention（GSA）机制，通过注意力层内的无损跨样本信息流动实现内在一致性；以及Direct Preference Optimization（DPO），利用人类偏好数据同步提升视觉保真度和身份保持。在ViStoryBench基准测试中，该方法在角色身份（CIDS）和风格一致性（CSD）指标上分别取得+10.0和+18.7的显著提升，达到新的最优水平。

【方法概述 / Method】
论文采用两阶段技术方案：第一阶段引入Group-Shared Attention机制，在注意力层中实现跨样本信息的无损流动，使模型能够结构化编码跨帧的身份对应关系，无需依赖外部编码器；第二阶段运用Direct Preference Optimization，通过整体偏好数据进行学习，替代传统的冲突辅助损失，同时优化视觉质量和叙事连贯性。

【实验结果 / Results】
在ViStoryBench基准测试上的广泛评估表明，该方法显著超越强基线模型，在角色身份一致性指标（CIDS）上提升10.0分，在风格一致性指标（CSD）上提升18.7分，同时保持高保真生成能力，确立了新的最优性能标准。

【应用价值 / Applications】
该研究可应用于自动化故事可视化、漫画/动画生成、电影分镜创作等领域，为需要长序列视觉叙事一致性的内容生产提供技术支撑。其无需外部编码器的特性降低了部署复杂度，偏好优化机制也更贴合人类审美标准，具有较好的实际落地潜力。
