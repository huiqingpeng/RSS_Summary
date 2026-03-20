---
title: "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18034"
published: "2026-03-20"
summarized: "2026-03-20T13:07:44.149294"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了针对检索增强生成（RAG）系统的语料库投毒攻击及其防御机制。作者提出了一种基于梯度引导的双文档投毒攻击方法，在Security Stack Exchange语料库上实现了38%的共检索成功率。研究发现，将BM25稀疏检索与向量相似度检索相结合的混合检索架构，能够在不修改底层大语言模型的情况下，将攻击成功率降至0%，显著提升了RAG系统的安全性。

【方法概述 / Method】
论文采用Greedy Coordinate Gradient（GCG）优化算法，设计了一种双文档投毒攻击：包含一个"休眠文档"和一个"触发文档"，两者协同优化以操纵检索结果。攻击针对现代RAG管道的检索层，通过梯度引导的方式优化恶意文档的嵌入表示，使其在特定查询下被优先检索。

【实验结果 / Results】
在Security Stack Exchange语料库（67,941篇文档）的50次攻击尝试中，纯向量检索下的梯度引导攻击成功率达38.0%；混合检索（BM25+向量相似度）将其降至0%。当攻击者联合优化稀疏和密集检索信号时，混合检索仍可将成功率限制在20-44%。跨五个LLM家族（GPT-5.3、GPT-4o、Claude Sonnet 4.6、Llama 4、GPT-4o-mini）的评估显示攻击成功率为46.7%-93.3%；而在FEVER Wikipedia数据集上的25次攻击全部失败（0%成功率）。

【应用价值 / Applications】
该研究为部署RAG系统的企业提供了即插即用的安全加固方案——混合检索架构无需模型微调或重新训练即可部署。研究揭示了RAG系统在外部知识源管理中的关键风险点，对金融、医疗、法律等依赖检索增强生成的高风险应用领域具有重要安全指导意义，同时提出的防御策略可直接集成到现有RAG基础设施中。
