---
title: "STELLAR: Structure-guided LLM Assertion Retrieval and Generation for Formal Verification"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2601.19903"
published: "2026-03-20"
summarized: "2026-03-20T12:04:53.740673"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了STELLAR，首个利用结构相似性引导大语言模型（LLM）生成SystemVerilog断言（SVA）的框架，以解决形式化验证中手动编写断言效率低、易出错的问题。该框架通过将RTL模块表示为AST结构指纹，从知识库中检索结构相关的（RTL, SVA）样本对，并整合到结构引导的提示中。实验结果表明，STELLAR在语法正确性、风格一致性和功能正确性方面均显著优于现有方法，证明了结构感知检索在工业形式化验证中的巨大潜力。

【方法概述 / Method】
STELLAR采用基于抽象语法树（AST）的结构指纹技术对RTL硬件设计进行编码，通过结构相似性匹配从知识库中检索最相关的专家编写断言样本。检索到的（RTL, SVA）样本对被嵌入到LLM的提示模板中，形成结构感知的上下文学习示例，从而引导模型生成高质量断言。

【实验结果 / Results】
STELLAR在多个硬件设计基准上实现了最优的语法正确率，生成的断言风格与专家编写样本高度一致，并在功能正确性验证中显著超越从零生成或无视结构模式的基线方法。实验结果凸显了结构引导检索对提升LLM生成断言质量的关键作用。

【应用价值 / Applications】
该框架可直接应用于集成电路设计中的形式化验证流程，大幅缩短断言开发周期并降低人为错误风险，提升验证效率。其结构感知检索思想可推广至其他硬件设计自动化任务，为工业级芯片验证提供可扩展的智能化解决方案。
