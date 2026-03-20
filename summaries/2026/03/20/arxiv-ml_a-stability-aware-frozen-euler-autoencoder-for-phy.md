---
title: "A Stability-Aware Frozen Euler Autoencoder for Physics-Informed Tracking in Continuum Mechanics (SAFE-PIT-CM)"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.13280"
published: "2026-03-20"
summarized: "2026-03-20T14:13:25.091638"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SAFE-PIT-CM，一种用于连续介质力学中物理信息跟踪的稳定性感知冻结欧拉自编码器。该架构将冻结的可微分PDE求解器嵌入自编码器中，通过卷积编码器将视频帧映射到潜在场，利用SAFE算子通过子步进有限差分进行前向传播，再由解码器重建视频。通过冻结算子的反向传播获得梯度，直接监督基于注意力的扩散系数α估计器，无需真实标签。核心贡献的SAFE算子通过子步进恢复原始时间分辨率和数值稳定性，解决了粗粒度时间快照违反von Neumann稳定性条件导致α崩溃的问题。

【方法概述 / Method】
SAFE-PIT-CM采用编码器-解码器架构，中间嵌入冻结的可微分PDE求解器。SAFE算子通过子步进（sub-stepping）技术，在粗粒度观测间隔内执行多个小步长的前向欧拉步骤，确保满足von Neumann稳定性条件。注意力机制用于估计物理参数α，整个系统通过物理损失进行端到端训练。

【实验结果 / Results】
该方法在扩散方程上进行了验证，涵盖工程金属中的热扩散场景。实验表明，子步进技术能够在完整的物理相关范围内实现准确的参数恢复。此外，测试时训练（TTT）无需预训练即可从单条仿真中学习α，仅使用物理损失作为监督，其精度与预训练推理相当。

【应用价值 / Applications】
SAFE-PIT-CM可应用于工程材料热传导分析、流体动力学监测等连续介质力学场景，实现从视频观测中无标签地反演物理参数。该架构可推广到任何允许卷积有限差分离散的PDE，且具有内在可解释性——每个预测都可追溯到具体的物理系数和逐步的PDE传播过程，为科学计算和工业监测提供了可靠的物理信息机器学习方法。
