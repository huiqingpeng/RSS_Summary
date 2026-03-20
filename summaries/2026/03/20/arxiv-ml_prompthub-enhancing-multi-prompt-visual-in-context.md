---
title: "PromptHub: Enhancing Multi-Prompt Visual In-Context Learning with Locality-Aware Fusion, Concentration and Alignment"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18891"
published: "2026-03-20"
summarized: "2026-03-20T13:17:33.849953"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了PromptHub框架，通过局部感知融合、集中和对齐机制来增强多提示视觉上下文学习（VICL）。该框架利用空间先验捕获更丰富的上下文信息，采用互补的集中、对齐和预测目标相互指导训练，并结合数据增强强化监督。在三个基础视觉任务上的大量实验表明，PromptHub在分布外设置和多种检索场景下均展现出优越性、通用性和鲁棒性，建立了超越先前逐块方法的可靠局部感知范式。

【方法概述 / Method】
PromptHub采用局部感知融合策略替代传统的逐块融合框架，通过挖掘空间先验信息实现更精细的上下文建模。训练过程中引入三种互补目标：集中目标（concentration）增强特征判别性，对齐目标（alignment）保证语义一致性，预测目标（prediction）确保任务性能，三者协同优化以克服模型无关监督的局限性。

【实验结果 / Results】
PromptHub在三个基础视觉任务（如语义分割、深度估计等）上显著优于现有基线方法，验证了多提示融合的有效性。实验还表明该方法具有良好的跨域迁移能力，在分布外（out-of-distribution）数据和多样化检索场景下保持稳健性能，证明了其通用性和鲁棒性。

【应用价值 / Applications】
该研究为视觉上下文学习提供了更高效的提示融合范式，可广泛应用于需要少样本或零样本视觉推理的场景，如医学影像分析、自动驾驶感知和机器人视觉等。其局部感知机制和对训练策略的改进也为其他视觉基础模型的多模态融合研究提供了可借鉴的技术路线。
