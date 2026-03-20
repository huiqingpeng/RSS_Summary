---
title: "Benchmarking PDF Parsers on Table Extraction with LLM-based Semantic Evaluation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18652"
published: "2026-03-20"
summarized: "2026-03-20T15:14:25.523071"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对PDF表格提取任务，提出了一种基于大语言模型（LLM）的语义评估方法，解决了传统基于规则的指标（如TEDS和GriTS）无法捕捉表格内容语义等价性的问题。研究构建了基于arXiv表格的合成PDF基准数据集，并通过1500多个人工质量判断验证，证明LLM评估与人类判断的相关性（Pearson r=0.93）显著优于传统方法。对21个当代PDF解析器的评估揭示了显著的性能差异，为表格数据提取的解析器选择提供了实用指导。

【方法概述 / Method】
研究采用LaTeX生成包含精确真值的合成PDF文档，确保表格的复杂性和多样性贴近真实学术论文。核心方法是将"LLM-as-a-judge"集成到匹配流程中，通过语义理解来评估提取表格与真值之间的等价性，同时容忍解析器输出的不一致性（如行列顺序差异、格式变化等）。

【实验结果 / Results】
人工验证研究表明，基于LLM的评估与人工判断的Pearson相关系数达0.93，明显优于TEDS（r=0.68）和GriTS（r=0.70）。在包含451个表格的100份合成文档上，21个PDF解析器的评估结果显示性能差距显著，最佳与最差解析器之间存在实质性差异。

【应用价值 / Applications】
该研究为大规模科学数据挖掘和知识库构建中的PDF表格提取任务提供了可复现、可扩展的评估方法论，帮助研究人员和从业者根据具体需求选择合适的解析器。LLM-based语义评估框架可推广至其他结构化数据提取任务，推动文档智能领域从语法匹配向语义理解转变。
