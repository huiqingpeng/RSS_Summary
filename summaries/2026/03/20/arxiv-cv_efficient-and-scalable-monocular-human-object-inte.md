---
title: "Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.00960"
published: "2026-03-20"
summarized: "2026-03-20T16:15:38.828288"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一个高效可扩展的单目人体-物体交互（HOI）运动重建框架，通过稀疏接触标注范式和多模态预测器InterPoint突破标注瓶颈，并开发了4DHOISolver优化框架以确保时空一致性和物理合理性。基于该方法构建了大规模数据集Open4DHOI，涵盖135种物体类型和133种动作，并成功应用于强化学习智能体的运动模仿任务。

【方法概述 / Method】
论文采用"人在回路"数据引擎，以InterPoint多模态预测器为核心驱动，仅需稀疏接触标注即可高效获取训练数据；随后通过4DHOISolver优化框架，将4D HOI重建这一病态问题约束为具有时空连贯性和物理合理性的解。

【实验结果 / Results】
所构建的Open4DHOI数据集在规模和多样性上达到新水平；重建的4D交互数据能够有效支持基于强化学习的智能体完成运动模仿任务，验证了重建质量对下游机器人学习任务的实用价值。

【应用价值 / Applications】
该方法可从海量单目网络视频中自动提取大规模4D交互数据，为通用机器人学习提供丰富的训练资源；重建的物理合理运动可直接用于机器人模仿学习和技能迁移，推动真实场景中的机器人操作能力发展。
