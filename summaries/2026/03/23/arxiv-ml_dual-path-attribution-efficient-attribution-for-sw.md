---
title: "Dual Path Attribution: Efficient Attribution for SwiGLU-Transformers through Layer-Wise Target Propagation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19742"
published: "2026-03-23"
summarized: "2026-03-24T07:22:00.844529"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Dual Path Attribution (DPA)，一种用于SwiGLU Transformer模型的新型归因框架，通过单次前向和单次反向传播即可忠实地追踪信息流，无需反事实样本。DPA将SwiGLU Transformer的计算结构解析分解并线性化为独立路径，沿这些路径传播目标解嵌向量以获取每个残差位置的有效表示。该方法在组件数量上达到O(1)时间复杂度，实现了对长输入序列和密集组件归因的可扩展性，在标准可解释性基准测试中达到了最先进的忠实度和前所未有的计算效率。

【方法概述 / Method】
DPA采用目标中心的层间传播策略，通过分析性地将SwiGLU激活函数的计算结构分解为两个独立路径（线性门控路径和SiLU激活路径），将目标解嵌向量从输出层反向传播至各残差位置。该方法仅需一次完整的前向传播计算中间激活，配合一次定制的反向传播即可同时获得所有模型组件的归因分数，避免了传统方法中逐组件评估的高昂计算开销。

【实验结果 / Results】
在标准可解释性基准测试中，DPA在归因忠实度指标上达到了当前最优水平，同时计算效率显著优于现有基线方法。该方法成功实现了对长输入序列的密集组件归因，时间复杂度与模型组件数量无关（O(1)），突破了传统归因方法在大型语言模型上的可扩展性瓶颈。

【应用价值 / Applications】
DPA可广泛应用于大型语言模型的可解释性分析、模型调试与审计、以及AI安全研究，帮助研究人员和工程师理解模型内部决策机制而无需承担高昂计算成本。该方法特别适用于需要分析长文档或进行细粒度神经元级别归因的实际场景，为LLM的可靠部署和有效运营提供了高效的工具支撑。
