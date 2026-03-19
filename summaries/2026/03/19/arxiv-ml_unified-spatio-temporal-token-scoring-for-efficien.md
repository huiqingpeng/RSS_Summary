---
title: "Unified Spatio-Temporal Token Scoring for Efficient Video VLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18004"
published: "2026-03-19"
summarized: "2026-03-19T13:17:12.630078"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了时空Token评分机制（STTS），一种用于视频视觉语言模型（Video VLMs）的统一Token剪枝方法。STTS通过在ViT和LLM全架构中对视觉Token进行时空联合剪枝，无需文本条件或Token合并，实现了端到端训练兼容。该方法在13个短视频和长视频问答任务上剪枝50%的视觉Token，带来62%的效率提升，平均性能仅下降0.7%，且随着采样帧数增加效率增益进一步提升。

【方法概述 / Method】
STTS采用轻量级评分模块，通过辅助损失学习时间维度的重要性评分，同时利用LLM下游梯度学习空间维度的重要性评分。配合高效的Token打包算法，STTS实现了跨ViT和LLM的统一Token剪枝，无需依赖复杂的文本条件选择机制。

【实验结果 / Results】
实验表明，STTS在13个短/长视频问答任务上剪枝50%视觉Token后，训练推理效率提升62%，平均性能仅损失0.7%。采样帧数越多，效率增益越显著。此外，在长视频问答任务中应用测试时缩放（test-time scaling）可额外获得0.5-1%的性能提升。

【应用价值 / Applications】
STTS适用于需要高效处理长视频内容的视觉语言理解场景，如视频问答、视频摘要和跨模态检索等。该方法可显著降低Video VLMs的计算成本，使其更适合部署于资源受限环境，同时保持模型性能，为实时视频理解和规模化视频处理提供了实用解决方案。
