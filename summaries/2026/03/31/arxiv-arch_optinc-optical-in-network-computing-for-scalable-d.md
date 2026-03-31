---
title: "OptINC: Optical In-Network-Computing for Scalable Distributed Learning"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.28290"
published: "2026-03-31"
summarized: "2026-04-01T07:17:07.645330"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了OptINC（光网络内计算）架构，通过将分布式学习中的梯度聚合和量化计算卸载到光互连中，显著降低服务器间的通信开销。该方案利用马赫-曾德尔干涉仪（MZIs）等光学器件构建光学神经网络（ONN），并设计了硬件感知训练算法和光域预处理算法来降低硬件成本同时保持精度。在ResNet50和LLaMA等真实任务上的评估表明，该方法在保持与环形全归约基线相当训练精度的同时，完全消除了通信开销。

【方法概述 / Method】
OptINC通过在光互连中集成MZIs等光学器件，将梯度平均和量化操作直接在光域执行，形成光学神经网络。为降低训练复杂度，提出了光域预处理算法；为减少硬件成本，采用酉矩阵和对角矩阵近似权重矩阵，并通过硬件感知训练算法补偿精度损失。

【实验结果 / Results】
该框架在CIFAR-100上的ResNet50训练和Wikipedia-1B上的LLaMA网络训练任务中进行了评估，结果表明OptINC能够达到与环形全归约基线相当的训练精度，同时彻底消除了分布式训练中的通信开销瓶颈。

【应用价值 / Applications】
OptINC可应用于大规模分布式深度学习训练场景，特别是需要频繁梯度同步的大模型训练（如GPT类LLM），通过光计算原生支持聚合操作，有望突破传统电互连的带宽和延迟限制，为下一代AI基础设施提供高能效、低延迟的通信计算融合方案。
