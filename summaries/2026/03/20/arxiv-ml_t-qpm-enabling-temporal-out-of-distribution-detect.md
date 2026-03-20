---
title: "T-QPM: Enabling Temporal Out-Of-Distribution Detection and Domain Generalization for Vision-Language Models in Open-World"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18481"
published: "2026-03-20"
summarized: "2026-03-20T13:13:21.997655"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对开放世界学习中视觉语言模型（VLMs）的分布外（OOD）检测问题，提出了一种时序四重模式匹配框架T-QPM。现有方法依赖固定融合规则且假设环境静态，难以应对时序漂移和协变量偏移。T-QPM通过引入跨模态一致性模式和轻量级融合权重学习，显著提升了动态环境下的OOD检测性能和领域泛化能力，并在时序划分的基准数据集上验证了其有效性。

【方法概述 / Method】
T-QPM采用两步框架扩展传统的双重模式匹配（DPM）：首先，通过将OOD图像与文本描述配对，建立ID与OOD信号之间的跨模态一致性模式，利用联合图像-文本推理优化决策边界；其次，通过学习轻量级融合权重动态组合语义匹配和视觉典型性评分，并引入基于平均阈值置信度（ATC）的显式正则化约束，确保模型在分布演变过程中的稳定性。

【实验结果 / Results】
实验在时序划分的基准数据集上进行，结果表明T-QPM显著优于静态基线方法，在动态非平稳环境中实现了更鲁棒、时序一致的OOD检测性能，有效缓解了时序分布漂移和协变量偏移带来的性能退化问题。

【应用价值 / Applications】
该研究适用于需要持续适应开放世界动态环境的实际场景，如自动驾驶、智能监控和机器人感知系统，这些场景中数据分布随时间演变且存在不可预见的OOD样本。T-QPM为部署VLMs的安全关键应用提供了可靠的分布外检测与领域泛化解决方案。
