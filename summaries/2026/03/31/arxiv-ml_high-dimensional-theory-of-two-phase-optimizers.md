---
title: "High dimensional theory of two-phase optimizers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26954"
published: "2026-03-31"
summarized: "2026-04-01T07:20:46.822791"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了双阶段优化器（two-phase optimizers）的高维理论，特别是LA-DiLoCo算法在高维线性回归问题上的分析。研究发现单工作器版本的LA优化器在信号与噪声权衡方面与SGD存在差异，这种特性在多种场景下具有优势；同时，多工作器版本虽产生更多噪声，但可通过超参数选择来缓解。此外，论文还分析了带动量的SLA变体，发现双重动量算子可通过非线性变换"有效"Hessian谱实现加速，其中Nesterov动量效果最优。

【方法概述 / Method】
论文采用高维渐近分析框架，研究LA（Local Adaptation）及其分布式变体LA-DiLoCo在线性回归问题上的理论性质。通过随机矩阵理论和自由概率工具，作者推导了单工作器和多工作器设置下优化器的收敛动态，并进一步扩展分析带双重动量的SLA（Stochastic LA）算法。

【实验结果 / Results】
研究表明LA相比SGD提供了不同的偏差-方差权衡，在噪声较大或Hessian条件数较差的场景中表现更优。多工作器设置会引入额外的"共识噪声"，但该效应可通过调整本地步数和同步频率来控制。对于SLA，双重动量结构能够对有效Hessian谱进行非线性变换，Nesterov动量配置可实现接近最优的加速效果。

【应用价值 / Applications】
该研究为大规模分布式训练中的异步/半同步优化器设计提供了理论指导，特别适用于通信受限的多节点训练场景。LA-DiLoCo家族算法可作为传统SGD的有力替代方案，而SLA的动量加速机制为开发更高效的优化器开辟了新方向，对训练大型机器学习模型具有实际意义。
