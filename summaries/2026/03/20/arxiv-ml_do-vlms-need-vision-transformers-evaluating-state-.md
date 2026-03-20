---
title: "Do VLMs Need Vision Transformers? Evaluating State Space Models as Vision Encoders"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19209"
published: "2026-03-20"
summarized: "2026-03-20T13:21:18.797086"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文探讨了状态空间模型（SSM）作为视觉编码器在视觉-语言模型（VLMs）中的应用潜力。研究发现，在ImageNet-1K初始化条件下，SSM视觉骨干网络在视觉问答（VQA）和定位任务上取得了最强的整体性能。经过检测或分割任务的密集调优后，SSM骨干网络在更小的模型规模下仍保持竞争力。此外，研究揭示了ImageNet准确率与VLM性能之间的不一致关系，以及某些视觉骨干网络在定位任务中的不稳定性，并提出了相应的稳定化策略。

【方法概述 / Method】
研究采用系统化的控制实验设置，在相同的ImageNet-1K预训练初始化条件下，对比评估SSM与基于Transformer的ViT系列视觉骨干网络。通过引入检测或分割等密集任务的微调策略，对两类骨干网络进行适应性改进，并在多模态任务中统一使用轻量级连接器将视觉特征映射到大语言模型中。

【实验结果 / Results】
实验表明，SSM骨干网络在VQA和grounding/localization任务上综合表现最优；密集任务调优普遍提升了两个骨干网络家族的性能；SSM在显著更小的模型规模下仍能与ViT竞争。研究还发现，更高的ImageNet准确率或更大的骨干网络并不必然带来更好的VLM性能，且部分视觉骨干网络在定位任务中存在不稳定性问题。

【应用价值 / Applications】
该研究为视觉-语言模型的视觉编码器设计提供了新的选择，证明了SSM可作为Transformer的有力替代方案，有助于开发更高效、轻量级的多模态系统。提出的稳定化策略可提升视觉骨干网络的鲁棒性，对需要精确定位能力的视觉-语言应用（如机器人导航、医疗影像分析）具有重要参考价值。
