---
title: "ICLAD: In-Context Learning for Unified Tabular Anomaly Detection Across Supervision Regimes"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19497"
published: "2026-03-23"
summarized: "2026-03-24T07:19:05.588002"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ICLAD，一种基于上下文学习（In-Context Learning）的表格异常检测基础模型，能够同时处理单类、无监督和半监督三种监督场景。该模型通过元学习在合成表格异常检测任务上进行训练，推理时仅需基于训练集进行条件推断而无需更新模型权重。在ADBench的57个表格数据集上的实验表明，ICLAD在三种监督场景下均达到了最先进的性能，为表格异常检测建立了统一框架。

【方法概述 / Method】
ICLAD采用元学习范式，在大量合成的表格异常检测任务上进行训练，使模型学会"如何学习"异常检测任务。推理阶段，模型将训练集作为上下文（in-context examples），通过注意力机制直接计算异常分数，实现了跨数据集和跨监督范式的零样本泛化能力。

【实验结果 / Results】
在ADBench基准的57个真实表格数据集上，ICLAD在单类、无监督和半监督三种设置下均取得最优或接近最优的性能。实验显示该统一模型能够匹配甚至超越为特定监督场景专门设计的传统方法，证明了其在多样化数据分布和异常模式下的强大泛化能力。

【应用价值 / Applications】
ICLAD为实际业务场景中的表格异常检测提供了即插即用的解决方案，无需为每个新数据集重新训练模型或根据标注情况选择不同算法。该框架特别适用于数据标注稀缺、异常模式多变的企业风控、金融欺诈检测、工业设备监控等领域，显著降低了模型部署和维护成本。
