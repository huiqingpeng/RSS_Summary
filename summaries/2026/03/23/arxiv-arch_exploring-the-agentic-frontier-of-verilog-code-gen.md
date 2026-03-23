---
title: "Exploring the Agentic Frontier of Verilog Code Generation"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.19347"
published: "2026-03-23"
summarized: "2026-03-24T07:14:10.691154"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文首次对基于Agent的LLM在Verilog代码生成任务上进行了系统性评估，使用CVDP基准测试发现：简单地将Agent框架套用于前沿模型反而会降低性能，但经过结构化设计的Agent工具链能够匹配甚至超越非Agent基线。研究还揭示了开源与闭源模型在Agent任务中的性能差距主要源于更高的崩溃率和工具输出理解能力不足。

【方法概述 / Method】
论文构建了多个开源的硬件设计Agent工具链（harnesses），通过结构化提示工程和领域相关工具（如仿真器、Linter等）与LLM结合；采用控制实验对比不同前沿模型（包括开源和闭源）在相同Agent框架下的表现，并分析工具调用模式和失败案例。

【实验结果 / Results】
实验表明，未经优化的朴素Agent封装会使性能低于优化提示的标准前向推理；而精心设计的结构化Agent工具链在部分场景下可超越非Agent基线。开源模型相比闭源模型表现出更高的执行崩溃率和较弱的工具输出解析能力，这是两者性能差距的主要来源。

【应用价值 / Applications】
该研究为硬件设计自动化领域提供了首个Agent化Verilog生成的开源基准和模型无关框架，可指导EDA工具开发商和芯片设计团队构建更可靠的智能辅助设计系统；同时揭示了当前LLM Agent在硬件特定领域的局限性，为未来专用硬件设计Agent的研发指明了优化方向。
