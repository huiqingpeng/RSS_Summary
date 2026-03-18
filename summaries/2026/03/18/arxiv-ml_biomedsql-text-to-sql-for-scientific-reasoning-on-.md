---
title: "BiomedSQL: Text-to-SQL for Scientific Reasoning on Biomedical Knowledge Bases"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.20321"
published: "2026-03-18"
summarized: "2026-03-18T17:10:37.763118"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了BiomedSQL，首个专门用于评估生物医学知识库上科学推理能力的Text-to-SQL基准测试。该基准包含68,000个问题/SQL查询/答案三元组，要求模型进行领域特定的推理（如基因组显著性阈值、效应方向性、试验阶段筛选等），而非仅依赖语法转换。研究发现当前LLM存在显著性能差距：最佳模型Gemini-3-Pro执行准确率为58.1%，定制多步智能体BMSQL达62.6%，远低于90.0%的专家基线。

【方法概述 / Method】
作者基于 harmonized BigQuery 知识库构建数据集，整合基因-疾病关联、组学数据因果推断和药物审批记录；通过模板生成问题-SQL-答案三元组，确保每个问题都需要隐式领域推理。评估涵盖多种开源与闭源LLM，测试不同提示策略和交互范式，并开发了专门的多步推理智能体BMSQL进行对比。

【实验结果 / Results】
实验显示所有模型在科学推理型Text-to-SQL任务上表现不佳：Gemini-3-Pro以58.1%执行准确率领先，GPT-4系列模型紧随其后，开源模型差距更大；作者提出的BMSQL多步智能体通过迭代推理将性能提升至62.6%，但仍显著低于90.0%的专家水平，揭示了当前方法在复杂生物医学推理中的根本局限。

【应用价值 / Applications】
BiomedSQL为开发能够支持科学发现的Text-to-SQL系统提供了重要基础，可直接应用于生物医学研究中的大规模结构化数据库查询，帮助研究人员高效获取基因-疾病关联、药物开发状态等复杂信息。该基准推动AI系统从简单语法翻译向真正的科学推理能力演进，对精准医学和药物研发具有重要实用价值。
