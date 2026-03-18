---
title: "Revisiting ASR Error Correction with Specialized Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2405.15216"
published: "2026-03-18"
summarized: "2026-03-18T16:16:21.155576"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文重新审视了自动语音识别（ASR）错误校正问题，提出使用紧凑的序列到序列（seq2seq）模型替代大型语言模型（LLM）进行ASR纠错。研究通过级联文本到语音（TTS）和ASR系统构建大规模合成训练数据，发现匹配真实错误分布的多样性是关键。所提模型参数量仅为LLM的1/15，在LibriSpeech上达到1.5%/3.3%的词错误率（WER），优于LLM，且能跨ASR架构和领域泛化。

【方法概述 / Method】
论文采用紧凑的seq2seq模型作为专门的ASR纠错模型，通过级联TTS和ASR系统生成包含真实ASR错误的合成语料库进行训练。提出"纠错优先解码"策略，即由纠错模型生成候选序列，再利用ASR声学模型分数进行重排序，以融合语义和声学信息。

【实验结果 / Results】
该专门化模型在LibriSpeech test-clean/test-other上分别达到1.5%和3.3%的WER，显著优于LLM基线。模型展现出强大的跨架构泛化能力，适用于CTC、Seq2seq和Transducer等多种ASR系统，并在低错误率场景下提供精确修正——这正是LLM表现不佳的区域。

【应用价值 / Applications】
该研究为实时ASR系统提供了一种低延迟、低幻觉风险的纠错方案，适用于对延迟敏感的语音交互应用（如实时会议转录、语音助手）。模型的小尺寸特性使其易于部署在边缘设备，同时跨领域和跨架构的泛化能力降低了系统集成成本。
