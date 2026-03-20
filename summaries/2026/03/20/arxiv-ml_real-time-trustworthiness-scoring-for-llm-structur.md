---
title: "Real-Time Trustworthiness Scoring for LLM Structured Outputs and Data Extraction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18014"
published: "2026-03-20"
summarized: "2026-03-20T13:07:12.087847"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CONSTRUCT方法，用于实时评估LLM结构化输出的可信度，使低分输出更可能包含错误，从而优化有限的人工审核资源。该方法还能对结构化输出中的每个字段进行可信度评分，帮助审核者快速定位错误位置。CONSTRUCT适用于任何LLM（包括无logprobs的黑盒API如推理模型和Anthropic模型），无需标注训练数据或自定义模型部署，可处理复杂的多字段嵌套JSON模式。研究还构建了一个可靠的公开基准测试，结果显示CONSTRUCT在检测Gemini 3和GPT-5等模型的错误时，精度/召回率显著优于其他评分方法。

【方法概述 / Method】
CONSTRUCT通过实时评分机制评估LLM结构化输出的整体可信度及每个字段的可信度，无需访问模型内部概率分布或额外训练。该方法采用与模型无关的设计，仅基于输出本身的特征进行可信度估计，使其能够兼容黑盒API和复杂嵌套数据结构。

【实验结果 / Results】
研究在四个数据集的新基准上评估了CONSTRUCT，该基准提供了可靠的ground-truth标注。实验表明，CONSTRUCT在检测多种LLM（包括Gemini 3和GPT-5）的结构化输出错误方面，相比其他评分方法具有显著更高的精度和召回率，能有效识别需要人工审核的高风险输出。

【应用价值 / Applications】
CONSTRUCT可广泛应用于企业AI系统中的自动化数据提取、文档解析和结构化信息生成等场景，通过优先级排序优化人工审核流程，降低运营成本。该方法特别适用于金融、医疗、法律等对输出准确性要求严格且需要人工复核的领域，助力企业安全部署LLM应用。
