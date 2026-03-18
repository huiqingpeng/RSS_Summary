---
title: "Zephyrus: An Agentic Framework for Weather Science"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.04017"
published: "2026-03-18"
summarized: "2026-03-18T17:12:07.597800"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了首个面向天气科学的智能体框架Zephyrus，旨在弥合天气基础模型与大型语言模型（LLMs）之间的能力鸿沟——前者擅长处理数值天气预报但缺乏语言推理能力，后者则相反。该框架包含一个Python代码交互环境ZephyrusWorld和多轮对话式天气智能体，并配套构建了基准测试集ZephyrusBench。实验表明，Zephyrus智能体相比纯文本基线模型正确率提升最高达44个百分点，但高难度任务对前沿LLMs仍具挑战性。

【方法概述 / Method】
Zephyrus框架的核心是ZephyrusWorld——一个基于Python代码的智能体环境，集成了WeatherBench 2数据集索引器、自然语言地理编码定位器、天气预报与气候模拟工具，以及多时间尺度气候统计查询模块。智能体采用多轮迭代机制，通过观察执行结果和对话反馈循环逐步优化分析策略。研究还设计了可扩展的数据生成流程，构建涵盖基础查询到高级推理的多样化评测任务。

【实验结果 / Results】
在ZephyrusBench基准测试上，Zephyrus智能体显著优于纯文本基线，正确率提升幅度高达44个百分点。然而，极端事件检测、反事实推理等困难任务即使使用前沿大语言模型仍表现不佳，表明该基准具有较高挑战性，同时也揭示了天气科学智能体领域的未来发展空间。

【应用价值 / Applications】
该框架为气象学家和气候研究人员提供了交互式科学工作流工具，支持从日常天气查询、极端气候事件分析到复杂反事实情景模拟的多样化任务。其模块化设计可扩展至农业规划、灾害预警、保险风险评估等需要结合数值预报与专家推理的实际应用场景，推动天气科学的智能化转型。
