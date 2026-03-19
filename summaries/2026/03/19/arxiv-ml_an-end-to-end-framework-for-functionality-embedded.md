---
title: "An End-to-End Framework for Functionality-Embedded Provenance Graph Construction and Threat Interpretation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17100"
published: "2026-03-19"
summarized: "2026-03-19T13:08:59.191336"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Auto-Prov，一个端到端的自适应框架，利用大语言模型（LLM）自动从异构且不断演化的日志中构建溯源图，并将系统级功能属性嵌入图中。该框架通过自动生成规则提取溯源边和实体信息，结合LLM推理与行为估计推断系统实体的功能上下文，最终生成自然语言攻击摘要。实验表明，Auto-Prov能持续增强检测性能，跨异构日志格式泛化，并在系统演化下保持稳定的可解释输出。

【方法概述 / Method】
Auto-Prov采用聚类方法处理未知日志类型，通过自动生成规则高效提取溯源边和实体级信息；利用LLM推理与行为估计相结合的技术为已知和未知系统实体推断功能上下文；最后将检测到的攻击自动总结为自然语言文本，辅助分析师调查。

【实验结果 / Results】
研究使用四种最先进的溯源图检测器在多样化日志上进行评估，结果表明Auto-Prov持续提升了检测性能，能够跨异构日志格式泛化，并生成稳定、可解释的攻击摘要，且在系统演化下保持鲁棒性。

【应用价值 / Applications】
Auto-Prov可应用于企业安全运营中心（SOC）的自动化威胁检测与调查，显著降低分析师手动分析日志和溯源攻击链的工作量；其自适应特性使其特别适合云原生、容器化等快速演化的IT环境，为实时安全监控和事件响应提供智能化支持。
