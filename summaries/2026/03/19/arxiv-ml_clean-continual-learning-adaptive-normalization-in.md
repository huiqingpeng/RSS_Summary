---
title: "CLeAN: Continual Learning Adaptive Normalization in Dynamic Environments"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17548"
published: "2026-03-19"
summarized: "2026-03-19T12:13:31.885816"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CLeAN（Continual Learning Adaptive Normalization），一种专为动态环境中表格数据持续学习设计的新型自适应归一化技术。该方法通过可学习参数估计全局特征尺度，并利用指数移动平均（EMA）模块进行更新，使模型能够适应不断演变的数据分布。实验表明，CLeAN在多种持续学习策略下不仅提升了模型在新数据上的性能，还有效缓解了灾难性遗忘问题，强调了自适应归一化在动态学习环境中保持知识稳定性的重要作用。

【方法概述 / Method】
CLeAN的核心方法是通过可学习参数动态估计全局特征尺度，而非依赖传统归一化方法中对完整数据集的静态假设。该方法采用指数移动平均（EMA）模块在线更新这些参数，使其能够随数据流的顺序到达而持续适应分布变化，从而与持续学习的序列特性相兼容。

【实验结果 / Results】
研究在两个数据集上结合多种持续学习策略（包括Reservoir Experience Replay、A-GEM和EwC）进行了全面评估。结果表明，CLeAN在提升模型对新任务的学习能力的同时，显著减轻了灾难性遗忘现象，验证了自适应归一化对于增强表格数据持续学习稳定性与有效性的关键作用。

【应用价值 / Applications】
CLeAN可广泛应用于数据分布动态变化的实际场景，如网络安全威胁检测、自动驾驶交通系统以及金融风控等领域。该技术为需要在不断流入的新数据上持续更新模型、同时保持历史知识不丢失的实时决策系统提供了重要的技术支撑，尤其适用于以表格数据为主的工业应用环境。
