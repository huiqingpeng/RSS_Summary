---
title: "HopChain: Multi-Hop Data Synthesis for Generalizable Vision-Language Reasoning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17024"
published: "2026-03-19"
summarized: "2026-03-19T15:03:54.330576"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了HopChain，一个可扩展的多跳视觉-语言推理数据合成框架，专门用于视觉语言模型（VLMs）的强化学习验证奖励（RLVR）训练。研究发现，现有的视觉-语言数据缺乏依赖视觉证据的复杂推理链，导致模型在感知、推理、知识和幻觉等错误模式上存在缺陷。通过将HopChain合成的多跳数据添加到Qwen3.5模型的RLVR训练中，在24个跨领域基准测试中，有20个取得提升，展现出广泛的泛化增益，特别是在超长思维链推理中提升超过50个百分点。

【方法概述 / Method】
HopChain通过构建逻辑依赖的多跳查询链来合成数据，其中早期跳步建立实例、集合或条件，为后续跳步提供基础，最终答案为可验证的具体数值。每个查询都基于实例 grounding，确保视觉证据贯穿整个推理过程，适用于可验证奖励的强化学习训练。

【实验结果 / Results】
在Qwen3.5-35B-A3B和Qwen3.5-397B-A17B模型上，添加HopChain多跳数据后，24个基准中有20个获得提升；用半多跳或单跳变体替代完整链式查询，平均准确率分别下降5.3和7.0个百分点。多跳训练在超长思维链（ultra-long-CoT）场景下效果尤为显著，准确率提升峰值超过50个百分点。

【应用价值 / Applications】
HopChain可广泛应用于需要复杂视觉推理的场景，如STEM教育、谜题解答、文档理解、视频分析和通用视觉问答等。该框架提供了一种可扩展的数据合成方法，能够系统性提升视觉语言模型的细粒度推理能力和泛化性能，为构建更可靠的视觉-语言智能系统奠定基础。
