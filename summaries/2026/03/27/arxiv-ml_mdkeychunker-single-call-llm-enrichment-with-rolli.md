---
title: "MDKeyChunker: Single-Call LLM Enrichment with Rolling Keys and Key-Based Restructuring for High-Accuracy RAG"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23533"
published: "2026-03-27"
summarized: "2026-03-28T07:13:11.911304"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出MDKeyChunker，一种针对Markdown文档的三阶段RAG优化流程，通过结构感知分块、单调用LLM元数据富集和基于语义键的重构，解决了传统固定大小分块忽略文档结构、语义单元碎片化及多轮LLM调用开销高的问题。核心创新包括一次性提取7种元数据字段的单调用设计，以及通过滚动键字典传播实现文档级上下文维护的LLM原生语义匹配机制。实验表明，BM25检索在结构分块上达到Recall@5=1.000和MRR=0.911，完整流程的稠密检索达到Recall@5=0.867。

【方法概述 / Method】

MDKeyChunker采用三阶段架构：（1）结构感知分块，将标题、代码块、表格和列表视为不可分割的原子单元；（2）单调用LLM富集，通过一次LLM调用并行提取标题、摘要、关键词、类型化实体、假设问题及语义键，同时传播滚动键字典以维护跨块文档上下文；（3）基于键的重构，通过语义键匹配和装箱算法合并相关块，实现语义相关内容的共置。该方法用LLM原生语义匹配替代手工调优的评分机制，显著降低计算开销。

【实验结果 / Results】

在18份Markdown文档、30个查询的评估中，配置D（BM25+结构分块）取得最优性能，Recall@5达1.000，MRR达0.911；完整流程配置C（稠密检索+全管道）Recall@5为0.867。结果表明结构感知分块本身即可显著提升检索精度，而完整管道在保持较高召回的同时实现了语义层面的块重组优化。

【应用价值 / Applications】

MDKeyChunker适用于技术文档、API文档、学术论文等结构化Markdown内容的RAG系统构建，可显著提升检索增强生成的准确性和效率。其单调用设计和轻量依赖（仅4个Python库）使其易于部署至任何OpenAI兼容端点，为企业知识库、开发者文档问答等场景提供低成本、高精度的解决方案，特别适合需要维护长文档上下文关联的复杂查询场景。
