---
title: "CODMAS: A Dialectic Multi-Agent Collaborative Framework for Structured RTL Optimization"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.17204"
published: "2026-03-19"
summarized: "2026-03-19T12:03:52.460960"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CODMAS（辩证多智能体协作优化系统），一种结合结构化辩证推理、领域感知代码生成与确定性评估的自动化RTL优化框架。该框架通过两个辩证智能体（Articulator和Hypothesis Partner）引导领域特定编码智能体和代码评估智能体协同工作，实现Verilog代码的架构感知优化。在包含120个Verilog三元组的RTLOPT基准测试上，CODMAS在流水线优化中实现约25%的关键路径延迟降低，在时钟门控优化中实现约22%的功耗降低，同时显著减少功能错误和编译失败率。

【方法概述 / Method】
CODMAS采用四智能体协作架构：Articulator智能体借鉴"橡皮鸭调试"方法逐步阐述转换计划并暴露潜在假设；Hypothesis Partner智能体预测优化结果并协调预期与实际行为之间的偏差；领域特定编码智能体（DCA）生成架构感知的Verilog代码编辑；代码评估智能体（CEA）验证语法正确性、功能等价性和PPA指标。该框架通过结构化辩证推理循环实现迭代优化。

【实验结果 / Results】
研究构建了RTLOPT基准数据集，包含120个用于流水线化和时钟门控优化的Verilog三元组（未优化代码、优化代码、测试平台）。在专有和开源大语言模型上的实验表明，与强提示基线和现有智能体基线相比，CODMAS在流水线优化中实现约25%的关键路径延迟降低，在时钟门控优化中实现约22%的功耗降低，同时显著降低了功能错误率和编译失败率。

【应用价值 / Applications】
该研究为电子设计自动化（EDA）领域提供了可扩展的自动化RTL优化方案，可应用于数字集成电路设计中的功耗-性能-面积（PPA）优化任务，尤其适用于复杂设计的流水线化和时钟门控优化。该方法有望降低芯片设计周期和人力成本，推动大语言模型在硬件设计领域的实际落地。
