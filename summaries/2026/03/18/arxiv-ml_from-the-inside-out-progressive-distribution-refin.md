---
title: "From the Inside Out: Progressive Distribution Refinement for Confidence Calibration"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16500"
published: "2026-03-18"
summarized: "2026-03-18T15:44:41.266587"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DistriTTRL方法，利用模型在强化学习中的置信度分布先验来渐进式优化奖励信号，而非依赖单一查询的rollout结果。该方法通过多样性目标惩罚缓解了基于投票的测试时缩放（TTS）策略导致的奖励作弊问题，实现了模型能力与自奖励信号的相互促进。实验表明，DistriTTRL在多个模型和基准测试上取得了显著的性能提升。

【方法概述 / Method】
DistriTTRL的核心思想是利用模型内部置信度的分布信息作为自奖励信号，在强化学习过程中进行渐进式分布优化。具体而言，该方法通过分析模型输出的置信度分布而非单一采样结果来构建更稳定的奖励信号，并引入多样性惩罚机制来防止投票式TTS策略中的奖励作弊现象。

【实验结果 / Results】
论文在多个模型和基准测试上验证了DistriTTRL的有效性，取得了显著的性能提升。具体量化指标在提供的摘要中未详细披露，但结果表明该方法能够有效解决测试与训练阶段内部信息不一致的问题，并显著改善置信度校准效果。

【应用价值 / Applications】
该方法可广泛应用于需要高置信度校准的大语言模型推理场景，如复杂数学推理、代码生成等需要测试时计算扩展的任务。通过提供更可靠的自奖励信号，DistriTTRL有助于降低人工标注成本，提升模型在关键决策任务中的可靠性和可解释性。
