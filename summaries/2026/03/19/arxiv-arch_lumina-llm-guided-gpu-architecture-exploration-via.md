---
title: "LUMINA: LLM-Guided GPU Architecture Exploration via Bottleneck Analysis"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.05904"
published: "2026-03-19"
summarized: "2026-03-19T12:04:26.969461"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了LUMINA，一个基于大语言模型（LLM）的GPU架构探索框架，旨在解决现代AI工作负载（如LLM推理）下GPU设计空间探索（DSE）面临的巨大设计空间、高仿真成本和复杂多目标优化等挑战。LUMINA通过从仿真器代码中提取架构知识，结合敏感性分析自动生成DSE规则，并在探索过程中进行自动修正。该框架还引入了DSE基准测试，系统评估和提升LLM在架构优化所需的三大核心能力。在包含470万可能样本的设计空间中，LUMINA仅用20步就识别出6个在性能和面积上均优于A100的设计，相比机器学习方法实现了17.5倍的探索效率提升和32.9%的更优设计质量（Pareto超体积）。

【方法概述 / Method】

LUMINA的核心方法是利用LLM进行瓶颈分析来指导GPU架构探索。具体而言，该框架首先从GPU仿真器代码中自动提取架构知识，然后通过敏感性研究生成DSE规则；这些规则在探索过程中由LLM进行自动修正和迭代优化。此外，LUMINA建立了专门的DSE基准测试，从三个维度（架构知识理解、瓶颈识别能力和设计决策推理）评估和筛选适合架构探索任务的LLM模型。

【实验结果 / Results】

在包含470万可能配置的大规模GPU设计空间中，LUMINA仅用20步探索就发现了6个在性能和面积上均优于NVIDIA A100的架构设计。与机器学习方法相比，LUMINA实现了17.5倍的DSE效率提升和32.9%的Pareto超体积改进，显著降低了高质量GPU设计所需的时间和计算成本。

【应用价值 / Applications】

LUMINA为GPU架构设计提供了一种高效、自动化的探索范式，可显著加速面向AI工作负载（尤其是大语言模型推理）的定制化GPU开发。该方法不仅适用于GPU设计，其LLM驱动的瓶颈分析和规则自动生成思路还可扩展至其他复杂计算机系统（如CPU、TPU、边缘AI加速器）的架构优化，为芯片设计自动化和智能化提供重要技术支撑。
