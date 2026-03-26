---
title: "IPatch: A Multi-Resolution Transformer Architecture for Robust Time-Series Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24207"
published: "2026-03-26"
summarized: "2026-03-27T07:21:55.775987"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了IPatch，一种多分辨率Transformer架构，用于解决多元时间序列预测中同时捕捉短期波动和长期依赖关系的挑战。该架构创新性地整合了点级（point-wise）和块级（patch-wise）两种表示方式，在多个时间尺度上建模时序信息。在7个基准数据集上的实验表明，IPatch在预测准确性、抗噪声鲁棒性和跨预测范围的泛化能力方面均优于单一表示的基线方法。

【方法概述 / Method】
IPatch采用多分辨率Transformer架构，通过并行使用点级token保留细粒度时间步信息和块级token捕获局部时序动态与长程依赖，实现不同时间尺度的信息融合。该方法在计算效率和细粒度建模之间取得平衡，克服了纯点级方法计算开销大、纯块级方法丢失细节信息的缺陷。

【实验结果 / Results】
在7个基准数据集上的全面实验验证了IPatch的有效性，模型在多种预测长度下均展现出稳定的性能提升。IPatch表现出对噪声的强鲁棒性，并在不同预测范围上具有良好的泛化能力，一致优于仅使用单一表示的对比基线模型。

【应用价值 / Applications】
IPatch适用于金融价格预测、能源负荷预测、交通流量预测等需要同时关注短期波动和长期趋势的复杂时序场景。其多分辨率设计使模型能够适应不同频率和复杂度的数据，为实际部署中面临噪声干扰和多变预测需求的时序预测任务提供了可靠解决方案。
