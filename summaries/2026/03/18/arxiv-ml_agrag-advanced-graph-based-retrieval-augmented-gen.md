---
title: "AGRAG: Advanced Graph-based Retrieval-Augmented Generation for LLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.05549"
published: "2026-03-18"
summarized: "2026-03-18T16:20:27.996594"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了AGRAG（Advanced Graph-based Retrieval-Augmented Generation），一种先进的基于图的检索增强生成框架，旨在解决现有Graph-based RAG方法面临的三大核心挑战：LLM幻觉导致的图构建不准确、缺乏显式推理路径导致的推理能力不足、以及LLM推理不充分导致的不完整回答。AGRAG通过统计方法替代LLM实体提取以避免幻觉，并将图推理形式化为最小成本最大影响（MCMI）子图生成问题，生成可作为显式推理路径的复杂图结构，从而显著提升LLM的推理能力和回答质量。

【方法概述 / Method】
AGRAG采用两阶段创新方法：在图构建阶段，使用基于统计的方法替代传统的LLM实体提取，从根本上消除LLM幻觉带来的错误传播；在检索阶段，将图推理重新定义为NP-hard的MCMI（Minimum Cost Maximum Influence）子图生成问题，并设计贪心算法求解，以高影响力节点和低边成本为目标生成综合推理路径。该方法支持循环等复杂图结构，相比简单树状路径具有更强的表达能力。

【实验结果 / Results】
论文通过理论分析证明了MCMI问题的NP-hard性质，并验证了贪心算法的有效性；实验表明AGRAG在多个基准任务上超越了NaiveRAG和现有Graph-based RAG方法，特别是在需要复杂推理和多跳推理的查询场景下，其生成的MCMI子图作为显式推理路径能够有效减少噪声干扰，提升LLM对检索内容相关部分的关注度，从而实现更全面准确的回答。

【应用价值 / Applications】
AGRAG可广泛应用于需要结构化知识检索与复杂推理的企业级问答系统、法律文献分析、医学知识库查询、科研文献综述生成等场景，其显式推理路径生成能力增强了结果可解释性，满足高风险决策领域对AI透明度的要求；同时，该方法的开源实现为工业界构建更可靠的RAG系统提供了可直接部署的技术方案。
