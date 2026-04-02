---
title: "Scheduling LLM Inference with Uncertainty-Aware Output Length Predictions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00499"
published: "2026-04-02"
summarized: "2026-04-03T07:21:54.679336"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对大语言模型（LLM）推理调度问题，指出传统方法使用单点估计预测输出长度与LLM随机解码过程的本质不确定性不匹配。作者发现输出长度服从重尾分布，可用对数t分布拟合，并据此提出"尾部膨胀期望"（TIE）调度指标。实验表明，TIE调度器在在线推理场景下将每token延迟降低2.31倍，在离线数据生成场景下吞吐量提升1.42倍。

【方法概述 / Method】
本研究首先通过实证数据分析LLM输出长度的统计特性，确定其服从对数t分布（log-t distribution）。基于该分布特性，提出Tail Inflated Expectation（TIE）指标——一种结合期望值与尾部概率的调度度量，用于替代传统最短作业优先（SJF）调度中的单点长度估计，以量化请求生成长输出的风险。

【实验结果 / Results】
TIE调度器与三个强基线方法对比显示：在在线推理场景中，每token延迟降低2.31倍；在离线数据生成场景中，吞吐量提升1.42倍。这些结果表明考虑输出长度不确定性能够显著改善LLM推理的调度效率。

【应用价值 / Applications】
该研究适用于大规模LLM服务部署场景，包括实时对话系统、API推理服务等在线应用，以及大规模数据合成、模型蒸馏等离线批处理任务。通过更精准地预测和调度变长输出请求，可有效缓解队头阻塞问题，提升GPU利用率和用户体验。
