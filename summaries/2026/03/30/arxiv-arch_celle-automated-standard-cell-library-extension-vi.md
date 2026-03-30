---
title: "CellE: Automated Standard Cell Library Extension via Equality Saturation"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.12797"
published: "2026-03-30"
summarized: "2026-03-31T07:17:27.151807"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CellE，一种基于形式化方法的标准单元库自动扩展框架，通过等式饱和（equality saturation）技术对映射后的网表进行穷尽式功能等效子电路发现。CellE构建e-graph来聚类所有功能等效的实现，并采用高效的模式挖掘算法选择面积最优的标准单元。实验结果表明，该方法平均可减少15.41%的芯片面积（最高达23.64%），并在商用流程中实现了8.00%的平均延迟降低。

【方法概述 / Method】
CellE的核心方法是将等式饱和技术应用于VLSI设计的后映射网表，生成e-graph作为功能等效实现的规范表示。基于这一规范表示，设计了一种高效的模式挖掘算法，用于识别和选择面积最优的标准单元组合，从而实现标准单元库的自动化扩展。

【实验结果 / Results】
实验结果显示，CellE相比现有方法平均实现了15.41%的面积缩减，最优情况下可达23.64%。在商业EDA流程中进行完整表征后，进一步获得了8.00%的平均延迟降低，验证了该方法在QoR优化方面的显著优势。

【应用价值 / Applications】
CellE可直接集成到现代VLSI设计流程中，用于自动化优化标准单元库，帮助芯片设计团队在物理实现阶段获得更优的面积-时序权衡。该技术特别适用于先进工艺节点下的高性能、低功耗芯片设计，能够降低对人工设计经验的依赖，提升设计效率和芯片竞争力。
