---
title: "AutothinkRAG: Complexity-Aware Control of Retrieval-Augmented Reasoning for Image-Text Interaction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.05551"
published: "2026-03-18"
summarized: "2026-03-18T19:07:15.647133"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了AutoThinkRAG，一种面向多模态文档问答的复杂度感知推理架构，旨在解决现有RAG系统静态检索忽略查询复杂度、以及端到端视觉语言模型将视觉感知与逻辑推理耦合导致的效率低下和生成不稳定问题。该架构通过查询复杂度路由器和感知-推理解耦设计，实现了自适应检索路径选择和高效的多模态推理。在DocBench和MMLongBench上的实验表明，该方法在分别达到82.13%和51.29%准确率的同时，显著降低了18.9%的token消耗和18.2%的货币成本。

【方法概述 / Method】
AutoThinkRAG包含两个核心组件：（1）查询复杂度路由器，用于分析查询难度和结构，自适应选择检索和推理路径；（2）感知-推理解耦架构，采用轻量级VLM作为高保真视觉解释器，将查询相关的视觉线索转换为文本表示，再由LLM进行逻辑推理和答案合成。

【实验结果 / Results】
在DocBench和MMLongBench基准测试中，AutoThinkRAG分别实现了82.13%和51.29%的整体准确率；相比基线方法，每查询token消耗减少18.9%，货币成本降低18.2%。进一步分析表明，该方法在需要自适应检索和多步推理的复杂查询上性能提升最为显著。

【应用价值 / Applications】
该研究适用于处理视觉丰富长文档的多模态问答场景，如金融报告分析、法律文档审查、学术论文解读等企业级知识管理应用。其复杂度感知机制和解耦架构设计为构建高效、可靠且成本可控的多模态RAG系统提供了可扩展的技术方案。
