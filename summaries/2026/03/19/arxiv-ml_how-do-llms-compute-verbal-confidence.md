---
title: "How do LLMs Compute Verbal Confidence"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17839"
published: "2026-03-19"
summarized: "2026-03-19T13:16:27.086180"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究揭示了大型语言模型（LLM）如何内部生成口头置信度（verbal confidence）的机制。通过针对 Gemma 3 27B 和 Qwen 2.5 7B 的系列实验，作者发现置信度并非即时计算，而是在答案生成过程中自动计算并缓存，后续再被提取输出。更重要的是，口头置信度反映的是对答案质量的复杂自我评估，而非简单的 token 对数概率或流畅性读数，这为理解 LLM 的元认知能力提供了重要证据。

【方法概述 / Method】
研究采用多种因果干预技术，包括激活引导（activation steering）、神经元修补（patching）、噪声注入（noising）和 token 交换实验，结合注意力阻断（attention blocking）来追踪信息流动路径。同时运用线性探测（linear probing）和方差分解（variance partitioning）量化不同表征对口头置信度的解释力。

【实验结果 / Results】
实验证据一致表明置信度采用缓存检索机制：置信度表征在答案相邻位置提前出现，随后才在 verbalization 位置显现；注意力阻断确认信息从答案 token 流向首个答案后位置进行缓存，再被提取输出。线性探测显示，这些缓存表征能解释口头置信度中超出 token 对数概率的显著方差，表明其包含更丰富的答案质量评估信息。

【应用价值 / Applications】
该发现对改进 LLM 校准（calibration）和不确定性量化具有直接意义，有助于开发更可靠的置信度估计方法。同时，揭示 LLM 自动、复杂的自我评估机制为人工智能元认知研究提供了理论基础，可指导未来设计更具自我意识和可解释性的模型架构。
