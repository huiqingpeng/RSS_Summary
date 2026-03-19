---
title: "Beyond Outliers: A Data-Free Layer-wise Mixed-Precision Quantization Approach Driven by Numerical and Structural Dual-Sensitivity"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17354"
published: "2026-03-19"
summarized: "2026-03-19T12:10:22.454252"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种名为NSDS的新型无校准层间混合精度量化（LMPQ）框架，通过数值与结构双重敏感性驱动，解决了现有方法仅依赖单一数值特性且忽视层内不同操作模块结构差异的问题。该框架将每层分解为不同的操作角色，从数值和结构两个维度量化敏感性，并通过MAD-Sigmoid和Soft-OR聚合方案生成统一的层间度量指标以指导比特分配。大量实验表明，NSDS在多种模型和下游任务上均优于各类基线方法，且无需任何校准数据。

【方法概述 / Method】

NSDS首先将神经网络层机械性地分解为具有不同操作角色的模块（如投影矩阵、门控机制等），然后分别从数值角度（权重分布特性）和结构角度（模块在网络中的功能重要性）计算敏感性分数。这些双维度分数通过基于MAD-Sigmoid和Soft-OR的鲁棒聚合方案融合为层级别的统一敏感性度量，最终据此进行自适应的混合精度比特分配。

【实验结果 / Results】

实验结果显示，NSDS在多种模型架构和下游任务上 consistently 超越了现有无数据量化基线方法，在极低比特设置（如W2A4、W3A4等）下实现了更优的精度-压缩权衡。该方法无需校准数据即可达到甚至超过部分需要数据依赖的方法性能，验证了双重敏感性建模和鲁棒聚合策略的有效性。

【应用价值 / Applications】

NSDS特别适用于数据隐私敏感场景（如医疗、金融）中的模型部署，因其完全无需校准数据即可实现高效量化压缩。该方法可广泛应用于边缘设备、移动端等计算资源受限环境下的深度学习模型加速，同时保持模型性能，为大规模语言模型和视觉Transformer等复杂架构的实用化部署提供了有效的轻量化解决方案。
