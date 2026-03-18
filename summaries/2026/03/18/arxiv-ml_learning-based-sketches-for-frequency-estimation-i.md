---
title: "Learning-based Sketches for Frequency Estimation in Data Streams without Ground Truth"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2412.03611"
published: "2026-03-18"
summarized: "2026-03-18T16:16:51.164307"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了UCL-sketch，一种无需真实标签的在线学习式草图方法，用于数据流中的频率估计。该方法通过等价学习机制实现无监督在线训练，并结合压缩感知技术与逻辑结构化的估计桶设计，在保证处理速度的同时显著降低估计误差。实验表明，UCL-sketch在极低内存预算下的精度接近全知预言机，且解码速度比现有基于方程的草图快近500倍。

【方法概述 / Method】
UCL-sketch采用基于等价学习的在线训练机制，无需依赖真实频率或标签即可学习；其核心架构利用逻辑结构化的估计桶实现高度可扩展性，并通过压缩感知理论保证收敛性和误差界。该方法将机器学习与经典草图数据结构相结合，在更新过程中持续优化估计器。

【实验结果 / Results】
在真实世界和合成数据集上的广泛实验表明，UCL-sketch在单键精度和分布估计上均优于现有方法；在极端内存受限条件下，其估计质量几乎达到理论最优的全知预言机水平。此外，相比现有基于方程的草图方法，UCL-sketch实现了平均近500倍的解码加速。

【应用价值 / Applications】
UCL-sketch适用于高吞吐量、低延迟的数据流场景，如数据库查询优化、网络流量测量和实时监控系统等。其无需 ground truth 的特性使其在真实标签难以获取的生产环境中极具实用价值，而高可扩展性和快速处理能力满足了实时大数据处理的需求。
