---
title: "Generating from Discrete Distributions Using Diffusions: Insights from Random Constraint Satisfaction Problems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20589"
published: "2026-03-24"
summarized: "2026-03-25T07:12:10.116051"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了使用扩散模型从离散分布中生成数据的问题，以随机k-SAT和k-XORSAT问题为基准测试。作者发现随机约束满足问题的理论见解对生成技术的行为具有可观测的影响，有时与直觉相悖。主要发现包括：连续扩散模型优于掩码离散扩散模型、学习扩散模型可以达到理论上的"理想"准确率，以及智能变量排序策略能显著提升生成准确性。

【方法概述 / Method】
论文采用随机k-SAT和k-XORSAT公式作为合成基准，研究从中均匀随机采样解的生成问题。作者比较了连续扩散模型与离散扩散模型的性能，并探索了不同的变量排序启发式方法对生成质量的影响。

【实验结果 / Results】
实验表明连续扩散模型在离散分布生成任务上表现优于掩码离散扩散模型；经过训练的扩散模型能够达到理论上的理想准确率水平；此外，精心设计的变量排序策略可以显著提高生成准确性，但效果最佳的排序方式并不遵循流行的启发式方法。

【应用价值 / Applications】
该研究为文本、表格数据和基因组数据等离散分布生成领域提供了重要的方法指导。研究成果有助于改进离散数据生成模型的设计，特别是在需要高质量采样和可控生成的应用场景中，如药物分子设计、合成数据生成和组合优化问题求解等。
