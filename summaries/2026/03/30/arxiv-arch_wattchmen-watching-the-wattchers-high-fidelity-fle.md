---
title: "Wattchmen: Watching the Wattchers -- High Fidelity, Flexible GPU Energy Modeling"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.26435"
published: "2026-03-30"
summarized: "2026-03-31T07:16:50.041696"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Wattchmen，一种灵活的GPU能耗测量、归因与预测方法，旨在解决现有GPU能耗分析技术不准确、不灵活或过时的问题。通过构建基于微基准测试的逐指令能耗模型，Wattchmen实现了更细粒度的能耗预测和应用能耗分解。在16个主流GPGPU、图分析、HPC和机器学习工作负载上，Wattchmen将平均绝对百分比误差（MAPE）降至14%，显著优于AccelWattch（32%）和Guser（25%），并成功扩展至V100（水冷15%）、A100（11%）和H100（12%）等多种GPU架构。

【方法概述 / Method】
Wattchmen采用多样化的微基准测试系统量化GPU指令的能耗消耗，构建逐指令能耗模型。该方法通过细粒度测量GPU各指令类型的能量特征，实现对应用能耗的高保真建模与分解，支持跨不同冷却方式和GPU架构的灵活扩展。

【实验结果 / Results】
在V100 GPU上，Wattchmen的MAPE为14%，相比AccelWattch（32%）和Guser（25%）分别降低56%和44%；该方法对水冷V100（15%）、A100（11%）和H100（12%）同样保持高精度。在Backprop和QMCPACK等实际应用中，Wattchmen的能耗洞察帮助实现了最高35%的能耗降低。

【应用价值 / Applications】
Wattchmen可广泛应用于高性能计算（HPC）系统的能耗优化、数据中心GPU集群的能效管理，以及机器学习工作负载的能耗分析与调优。其高保真、跨架构的能耗建模能力为GPU架构设计、冷却系统优化和绿色计算策略制定提供了重要工具支持。
