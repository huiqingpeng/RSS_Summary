---
title: "UCAgent: An End-to-End Agent for Block-Level Functional Verification"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.25768"
published: "2026-03-30"
summarized: "2026-03-31T07:17:10.057390"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了UCAgent，一个端到端的智能体系统，用于自动化硬件模块级功能验证。针对现有大语言模型在Verilog/SystemVerilog验证代码生成准确性低、复杂多步骤验证工作流脆弱性高、以及验证一致性难以维持等挑战，UCAgent通过纯Python验证环境、31阶段细粒度验证工作流和验证一致性标注机制，实现了UART、FPU和整数除法器等模块的端到端自动化验证，代码覆盖率高达98.5%，功能覆盖率达100%，并发现了真实设计中此前未被识别的缺陷。

【方法概述 / Method】
UCAgent采用三项核心机制：首先，利用Picker和Toffee工具链构建纯Python验证环境，规避LLM生成SystemVerilog验证代码的准确性问题；其次，设计可配置的31阶段细粒度验证工作流，每个阶段均配备自动化检查器进行验证；最后，提出验证一致性标注机制（VCLM），为LLM生成的各类产物分配层级化标签，确保规范、覆盖模型与测试用例之间的可追溯性和一致性。

【实验结果 / Results】
实验表明，UCAgent可在UART、浮点运算单元（FPU）和整数除法器等多个硬件模块上完成端到端自动化验证，最高实现98.5%的代码覆盖率和100%的功能覆盖率。此外，该系统在真实设计中发现了一些此前未被识别的设计缺陷，验证了其检测实际问题的能力。

【应用价值 / Applications】
UCAgent可显著缩短现代IC开发周期中占比约70%的功能验证时间，降低对专业验证工程师的依赖，提升验证效率和可靠性。其端到端自动化能力适用于各类数字IP模块的快速验证迭代，对加速芯片设计流程、降低验证成本具有重要的工业应用价值，尤其在敏捷开发和开源硬件生态中具有广阔前景。
