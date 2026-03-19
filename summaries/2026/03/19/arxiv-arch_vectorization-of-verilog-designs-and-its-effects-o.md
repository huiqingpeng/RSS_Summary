---
title: "Vectorization of Verilog Designs and its Effects on Verification and Synthesis"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.17099"
published: "2026-03-19"
summarized: "2026-03-19T12:03:45.755369"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文探讨了向量化优化在Verilog硬件设计中的应用，指出尽管Verilog支持向量表示，但缺乏语义保证使其在硬件生态中不常见。作者基于CIRCT编译基础设施开发了一个Verilog向量化器，实验表明该工具能显著降低形式化验证的符号复杂度，在Cadence Jasper工具上对1,157个ChiBench设计实现了28.12%的精化时间提升和51.30%的内存消耗降低。

【方法概述 / Method】
作者基于MLIR/CIRCT编译基础设施构建了一个Verilog向量化器，能够识别多种向量化模式，包括反向赋值、涉及复杂表达式的赋值以及跨模块赋值。该工具在不改变底层硬件结构的前提下，将多个标量操作替换为单个向量操作，使形式化验证工具能够将总线视为单一符号实体进行处理。

【实验结果 / Results】
在ChiBench基准测试集的1,157个设计上，使用Cadence Jasper形式化验证工具进行实验，向量化后的设计相比原始设计平均精化时间减少28.12%，内存消耗降低51.30%。这些改进源于符号复杂度的降低，使得验证工具能更高效地处理布尔函数和状态转移。

【应用价值 / Applications】
该研究主要应用于硬件形式化验证领域，可显著提升大规模数字电路设计的验证效率，缩短芯片设计周期。此外，向量化优化还可扩展至其他电子设计自动化（EDA）工具链，为复杂SoC和处理器设计的验证与综合流程提供性能优化支持。
