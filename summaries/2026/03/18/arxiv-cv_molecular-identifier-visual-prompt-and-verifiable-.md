---
title: "Molecular Identifier Visual Prompt and Verifiable Reinforcement Learning for Chemical Reaction Diagram Parsing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15011"
published: "2026-03-18"
summarized: "2026-03-18T19:04:48.600603"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究针对化学反应图解析（RxnDP）任务，提出了两种互补的技术创新来解决视觉语言模型（VLMs）在该领域的核心瓶颈：视觉化学实体与预训练知识的对齐困难，以及token级训练与反应级评估之间的差异。研究提出了分子标识符视觉提示（IdtVP）方法，利用反应图中自然存在的分子标识符（如粗体数字1a）激活VLM的化学知识，实现强大的零样本和分布外泛化能力；同时设计了Re3-DAPO强化学习算法，通过可验证奖励直接优化反应级指标，在微调范式下持续超越标准监督微调。此外，研究还发布了包含真实世界扫描图像的ScannedRxn基准数据集。

【方法概述 / Method】

IdtVP方法将分子标识符作为视觉提示，通过显式标注反应图中的化学实体编号，桥接视觉感知与VLM预训练阶段获得的化学知识，无需额外训练即可提升模型对化学结构的识别能力。Re3-DAPO（Reaction-level Direct Preference Optimization）是一种基于可验证奖励的强化学习算法，它将反应级评估指标（如产物预测准确性）转化为可计算的奖励信号，直接优化整个化学反应的解析正确性，而非传统的token级损失。

【实验结果 / Results】

IdtVP在零样本和分布外场景下显著优于现有提示策略，展现出强大的泛化能力；Re3-DAPO在微调设置下相比标准监督微调获得一致的性能提升。在ScannedRxn基准上的评估验证了模型对真实世界扫描图像（含噪声、畸变等实际伪影）的鲁棒性，证明该方法在具有挑战性的实际应用场景中仍能保持较高准确性。

【应用价值 / Applications】

该技术可自动化从化学文献中提取合成反应信息，加速药物研发、材料科学等领域的知识挖掘流程，减少人工标注成本。ScannedRxn基准支持对历史文献数字化档案的自动解析，有助于构建大规模可搜索的化学反应数据库。整体方案提升了VLM在专业科学文献理解中的实用性和可靠性，为科学智能（AI for Science）应用提供了可推广的技术范式。
