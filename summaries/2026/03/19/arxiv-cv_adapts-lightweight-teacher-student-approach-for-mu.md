---
title: "AdapTS: Lightweight Teacher-Student Approach for Multi-Class and Continual Visual Anomaly Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17530"
published: "2026-03-19"
summarized: "2026-03-19T15:12:58.576743"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了AdapTS，首个面向多类别和持续学习场景的统一Teacher-Student视觉异常检测框架，专为边缘设备部署优化。该方法通过单一共享冻结主干网络结合轻量级可训练适配器，消除了传统方法需要两种架构的限制，并引入分割引导目标和合成Perlin噪声增强训练，配合基于原型的任务识别机制实现99%的适配器动态选择准确率。实验表明，AdapTS在保持性能的同时显著降低内存开销，最轻量版本仅需8MB额外内存，相比现有方法减少13-149倍。

【方法概述 / Method】
AdapTS采用Teacher-Student架构，教师网络为冻结的预训练编码器，学生网络通过注入轻量级可训练适配器（adapters）学习多任务知识，避免存储多个完整网络。训练阶段使用分割引导损失函数和合成Perlin噪声生成异常样本，推理阶段则通过基于特征原型的任务识别模块动态选择对应任务的适配器参数。

【实验结果 / Results】
在MVTec AD和VisA数据集上的实验显示，AdapTS在多类别和持续学习场景下达到与现有Teacher-Student方法相当的检测性能。内存效率方面，AdapTS-S仅需8MB额外存储，相比STFPM（95MB）、RD4AD（360MB）和DeSTSeg（1120MB）分别减少13倍、48倍和149倍，同时任务识别准确率高达99%。

【应用价值 / Applications】
AdapTS特别适用于工业质检等需要同时检测多种产品类型且需持续学习新类别的复杂场景，其超低内存占用使其能够部署于计算资源受限的边缘设备。该框架解决了实际生产环境中模型频繁切换和增量学习的痛点，为大规模工业自动化提供了可扩展的智能化解决方案。
