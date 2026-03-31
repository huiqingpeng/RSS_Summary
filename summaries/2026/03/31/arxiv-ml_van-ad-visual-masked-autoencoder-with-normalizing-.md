---
title: "VAN-AD: Visual Masked Autoencoder with Normalizing Flow For Time Series Anomaly Detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26842"
published: "2026-03-31"
summarized: "2026-04-01T07:20:03.723269"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了VAN-AD，一种基于视觉掩码自编码器（MAE）的时间序列异常检测基础模型，通过迁移ImageNet预训练的视觉模型解决现有方法泛化能力差的问题。针对直接迁移MAE带来的过度泛化和局部感知受限两大挑战，作者设计了自适应分布映射模块（ADMM）和归一化流模块（NFM）。在9个真实数据集上的实验表明，VAN-AD在少样本场景下 consistently 优于现有最先进方法。

【方法概述 / Method】
VAN-AD将时间序列转换为图像表示后输入预训练MAE进行重构，通过ADMM将重构前后的结果映射到统一统计空间以放大异常差异，同时利用NFM结合归一化流估计当前窗口在全局分布下的概率密度，增强局部异常感知能力。

【实验结果 / Results】
在9个真实世界数据集上的大量实验显示，VAN-AD在多种评估指标下 consistently 超越现有SOTA方法，尤其在训练数据稀缺的跨场景泛化任务中表现突出，验证了视觉基础模型迁移至时间序列异常检测的有效性。

【应用价值 / Applications】
VAN-AD可广泛应用于IoT服务系统的实时监控与故障预警，如工业设备异常检测、网络流量监控和智能运维等场景，其强泛化能力特别适合标注数据稀缺或需快速部署到新领域的实际应用需求。
