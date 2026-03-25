---
title: "MCLR: Improving Conditional Modeling in Visual Generative Models via Inter-Class Likelihood-Ratio Maximization and Establishing the Equivalence between Classifier-Free Guidance and Alignment Objectives"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22364"
published: "2026-03-25"
summarized: "2026-03-26T07:13:42.329793"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出MCLR（最大类间似然比）方法，通过显式最大化类间似然比来改进条件扩散模型的训练目标，使标准采样无需推理时引导即可达到与分类器自由引导（CFG）相当的效果。研究还建立了CFG与对齐目标之间的形式化等价关系，证明CFG引导的分数恰好是加权MCLR目标的最优解，为CFG提供了机制性解释。该工作从理论上回答了为何标准去噪分数匹配（DSM）需要推理时引导的问题，并提出了原则性的改进方案。

【方法概述 / Method】
MCLR通过在训练阶段显式最大化不同条件类之间的似然比，增强模型对条件信息的区分能力，从而替代推理时的启发式引导。该方法将传统DSM目标与类间对齐目标相结合，使模型学习到的条件分数天然具备类间分离特性。

【实验结果 / Results】
经MCLR微调的模型在标准采样下展现出与CFG相当的定性和定量性能提升，无需依赖推理时的引导系数调节。实验验证了该方法在视觉生成任务中能有效改善条件建模质量，同时保持采样过程的简洁性。

【应用价值 / Applications】
MCLR可广泛应用于文本到图像生成、条件图像合成等视觉生成任务，简化部署流程并消除CFG的调参负担。该理论框架还为理解和改进扩散模型的条件生成机制提供了新视角，有助于开发更高效的生成模型训练范式。
