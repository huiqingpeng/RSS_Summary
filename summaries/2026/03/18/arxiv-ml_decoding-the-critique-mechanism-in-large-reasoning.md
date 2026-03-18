---
title: "Decoding the Critique Mechanism in Large Reasoning Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16331"
published: "2026-03-18"
summarized: "2026-03-18T15:42:45.302106"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文系统研究了大型推理模型（LRMs）如何从错误中恢复，发现即使错误通过思维链传播并导致中间结论错误，模型仍能得出正确答案，揭示了其隐藏的"批判能力"。研究团队通过特征空间分析识别出一个高度可解释的"批判向量"，该向量代表模型的自我纠错机制。实验表明，利用该向量调控潜在表征可显著提升模型的错误检测能力和测试时扩展性能，且无需额外训练成本。

【方法概述 / Method】
研究者在LRMs的中间推理步骤中人为插入算术错误，观察模型的恢复行为；通过特征空间分析（feature space analysis）方法，从模型的隐藏状态中提取并识别出代表批判能力的可解释向量。基于该发现，提出通过潜在表征操控（steering latent representations）来增强模型性能的方法。

【实验结果 / Results】
实验在多个模型规模和系列上验证了批判向量的有效性，证明使用该向量进行潜在表征调控能够提升模型的错误检测能力；同时，该方法在测试时扩展（test-time scaling）场景下增强了模型性能，且无需任何额外训练。

【应用价值 / Applications】
该研究为理解和控制LRMs的自我验证机制提供了理论基础，有助于开发更可靠的推理系统；所提出的批判向量操控方法可直接应用于提升现有模型的自我纠错能力，为构建更鲁棒、可解释的大型推理模型开辟了新方向。
