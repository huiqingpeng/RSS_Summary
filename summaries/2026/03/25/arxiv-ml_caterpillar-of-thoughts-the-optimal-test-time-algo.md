---
title: "Caterpillar of Thoughts: The Optimal Test-Time Algorithm for Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22784"
published: "2026-03-25"
summarized: "2026-03-26T07:17:15.431020"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了大型语言模型（LLM）测试时计算的最优结构化问题，将其建模为与马尔可夫链交互的算法，允许算法随时回溯到任何先前观察到的状态。作者理论证明了最优算法总是生成"毛毛虫树"结构——即移除叶子节点后得到一条路径，并基于此提出了Caterpillar of Thoughts（CaT）算法。实验表明，CaT相比Tree-of-Thoughts（ToT）在获得更高成功率的同时，显著减少了token生成数量。

【方法概述 / Method】
论文将测试时计算形式化为一个与马尔可夫链交互的算法框架，其中算法可以主动选择从任意历史状态恢复生成，而非被动地沿单一路径采样。通过理论分析，作者证明了最优回溯策略具有严格的结构特征：只需保留一条主干路径和直接连接的叶子节点，形成"毛毛虫树"拓扑结构，从而将指数级的搜索空间压缩到线性复杂度。

【实验结果 / Results】
Caterpillar of Thoughts（CaT）在实证评估中展现出优于Tree-of-Thoughts（ToT）的综合性能：在实现更高任务成功率的同时，显著降低了token/状态生成数量。这一结果验证了理论分析的核心结论——受限的回溯形式即可达到最优性能，无需复杂的任意树形搜索结构。

【应用价值 / Applications】
该研究为LLM推理时的计算资源优化提供了理论指导和实用算法，特别适用于需要平衡推理成本与输出质量的场景，如复杂数学问题求解、代码生成和多步决策任务。CaT算法可直接替代现有的CoT、ToT等测试时增强方法，在保持或提升性能的同时降低推理开销，对API调用成本和实时响应要求高的应用具有重要价值。
