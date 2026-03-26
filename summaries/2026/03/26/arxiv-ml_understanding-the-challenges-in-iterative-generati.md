---
title: "Understanding the Challenges in Iterative Generative Optimization with LLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23994"
published: "2026-03-26"
summarized: "2026-03-27T07:19:36.840715"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文揭示了基于大语言模型的迭代生成式优化（Generative Optimization）在实际应用中脆弱性的根本原因：工程师必须做出多个"隐性"设计选择，包括优化器可编辑的范围以及每次更新时提供的"正确"学习证据。通过对MLAgentBench、Atari和BigBench Extra Hard的案例研究，作者发现起始工件、执行轨迹的信用跨度以及试验错误的批处理方式这三个因素会显著影响优化成败，但前人研究很少明确讨论这些决策。研究指出，目前缺乏跨领域通用的简单方法来设置学习循环，这是阻碍该技术生产化和普及的主要障碍。

【方法概述 / Method】
本研究采用系统性案例分析方法，在三个不同领域（机器学习智能体基准MLAgentBench、经典强化学习环境Atari、以及复杂推理任务BigBench Extra Hard）中，分别操控三个关键设计变量：起始工件的选择、执行反馈的信用分配时间跨度（credit horizon）、以及批量试验数据的聚合策略，以量化这些因素对生成式优化性能的影响。

【实验结果 / Results】
研究发现：在MLAgentBench中，不同的起始工件决定了哪些最终解决方案可达；在Atari环境中，即使截断的执行轨迹仍能有效改进智能体表现；在BBEH任务上，更大的小批量数据并不单调提升泛化性能。这些结果表明，设计选择的效果具有领域依赖性，不存在放之四海而皆准的最优配置。

【应用价值 / Applications】
该研究为构建自改进型LLM智能体提供了实用的设计指导，帮助工程师在代码生成、工作流优化、提示工程等领域做出更明智的隐性决策。通过明确这些常被忽视的设计维度，研究有望降低生成式优化的部署门槛，推动其从研究原型向生产系统的转化，促进自动化智能体在软件工程、科学发现和复杂决策支持等场景的实际应用。
