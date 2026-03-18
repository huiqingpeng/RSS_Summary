---
title: "Improved Iterative Refinement for Chart-to-Code Generation via Structured Instruction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2506.14837"
published: "2026-03-18"
summarized: "2026-03-18T18:26:15.807924"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ChartIR方法，通过结构化指令实现图表到代码生成的迭代优化。该方法将视觉理解与代码翻译解耦，设计了描述指令和差异指令两种结构化指令来转化视觉特征，并将生成流程分解为初始代码生成和迭代优化两个阶段。实验表明，该方法在开源模型Qwen2-VL和闭源模型GPT-4o上均优于现有方法。

【方法概述 / Method】
ChartIR采用两阶段迭代优化框架：首先使用描述指令提取参考图表的视觉元素，再通过差异指令对比参考图表与生成图表的偏差，将视觉理解转化为语言表示；随后基于这些结构化指令进行代码翻译，通过多轮迭代逐步优化生成的代码。

【实验结果 / Results】
ChartIR在Qwen2-VL和GPT-4o两个多模态大语言模型上均取得最优性能，显著优于直接提示和其他对比方法。结构化指令有效提升了视觉理解的准确性，迭代优化机制逐步改进了代码生成质量。

【应用价值 / Applications】
该方法可应用于自动化图表生成、数据可视化工具开发等领域，帮助用户通过自然语言或示例图表快速生成可执行的可视化代码，降低数据可视化的技术门槛，提升开发效率。
