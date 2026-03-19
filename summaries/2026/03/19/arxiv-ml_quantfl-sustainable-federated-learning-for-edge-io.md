---
title: "QuantFL: Sustainable Federated Learning for Edge IoT via Pre-Trained Model Quantisation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17507"
published: "2026-03-19"
summarized: "2026-03-19T12:12:33.537163"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出 QuantFL，一种面向边缘物联网的可持续联邦学习框架，通过利用预训练模型初始化实现激进的轻量级量化。研究发现预训练自然集中了更新统计量，从而无需能耗高昂的错误反馈机制即可使用内存高效的桶量化。实验表明，QuantFL 在严格带宽限制下将总通信量降低 40%，同时达到或超越未压缩基线，为电池受限的物联网网络提供了实用的"绿色"训练方案。

【方法概述 / Method】
QuantFL 的核心方法是利用预训练模型初始化来启用激进的计算轻量级量化，具体采用内存高效的桶量化（bucket quantisation）策略。该方法避免了传统量化中需要复杂错误反馈机制的高能耗开销，通过预训练带来的更新统计量集中特性，实现了无需复杂补偿的量化压缩。

【实验结果 / Results】
在 MNIST 和 CIFAR-100 数据集上，QuantFL 实现了 40% 的总通信量降低（全精度下行时约 40% 总比特减少，上行或下行量化时 ≥80%）。在严格带宽预算下，QuantFL 匹配或超越了未压缩基线，其中 BU（桶量化）配置在 MNIST 上达到 89.00% 测试准确率，在 CIFAR-100 上达到 66.89%，同时使用的比特数减少数个数量级。

【应用价值 / Applications】
QuantFL 适用于电池受限、带宽有限的边缘物联网场景，如智能家居传感器、工业监测设备和可穿戴健康设备等。该框架通过显著降低通信能耗，延长了设备续航时间，同时保持模型性能，为实现大规模、可持续的分布式边缘智能提供了实用解决方案，具有重要的环境和经济效益。
