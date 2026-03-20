---
title: "Benchmarking State Space Models, Transformers, and Recurrent Networks for US Grid Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.21415"
published: "2026-03-20"
summarized: "2026-03-20T14:11:24.453037"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本论文对美国电网预测任务中的五种现代神经网络架构进行了全面基准测试，包括两种状态空间模型（PowerMamba、S-Mamba）、两种Transformer（iTransformer、PatchTST）以及传统LSTM。研究发现不存在单一最优模型：仅使用历史负荷数据时，PatchTST和状态空间模型精度最高；而引入天气协变量后，iTransformer的效率提升显著优于其他模型。此外，不同预测任务（太阳能、风电、电价）的最优模型选择也各不相同，为电网运营商提供了基于具体数据环境的模型选型指导。

【方法概述 / Method】

研究在六个美国电网的小时级电力需求数据上，对24至168小时预测窗口进行跨模型比较。为确保公平性，作者为每个模型适配了专门的时间处理模块，并设计了模块化层以统一整合天气协变量。通过控制模型规模，研究进一步区分了架构本身的信息混合能力与参数量带来的性能差异。

【实验结果 / Results】

实验表明，iTransformer在加入天气数据后准确率提升效率是PatchTST的三倍，这源于其跨变量信息混合的架构优势；PatchTST在太阳能等强周期性信号上表现最佳，而状态空间模型更适用于风电和电价等混沌波动信号。状态空间模型与PatchTST在历史负荷单变量预测中精度相当。

【应用价值 / Applications】

该基准测试为电力系统运营商提供了可操作的模型选择指南，使其能根据可用数据类型（历史负荷 vs. 天气协变量）和预测目标（需求、可再生能源出力、电价）匹配最优深度学习架构，从而提升电网调度、能源交易和可再生能源整合的预测可靠性。
