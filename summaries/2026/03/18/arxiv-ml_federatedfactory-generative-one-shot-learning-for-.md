---
title: "FederatedFactory: Generative One-Shot Learning for Extremely Non-IID Distributed Scenarios"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16370"
published: "2026-03-18"
summarized: "2026-03-18T15:43:23.321758"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出 FederatedFactory，一种面向极端非独立同分布（Non-IID）场景的联邦学习框架。该框架将联邦单元从判别式参数转变为生成式先验，通过单次通信轮次交换生成模块，实现从零合成类别均衡的全局数据集，彻底消除梯度冲突和外部先验偏差。在 MedMNIST、ISIC2019 等医学图像基准测试中，该方法恢复到了集中式学习的性能上限；在 CIFAR-10 的病态异构设置下，准确率从崩溃的 11.36% 提升至 90.57%，同时支持通过确定性删除特定生成模块实现精确的模块化遗忘。

【方法概述 / Method】

FederatedFactory 采用生成式一次性学习（Generative One-Shot Learning）范式，各客户端训练本地生成模型而非判别模型，仅上传生成模块至服务器。服务器聚合这些生成先验后，合成类别平衡的全局数据集用于训练统一分类器，整个联邦过程仅需单次通信轮次。该方法零依赖预训练基础模型，完全基于客户端本地数据学习生成先验。

【实验结果 / Results】

在极端 Non-IID 场景（标签分布互斥）下，FederatedFactory 在 CIFAR-10 上将基线准确率从 11.36% 提升至 90.57%，在 ISIC2019 皮肤病变分类任务上 AUROC 达到 90.57%，恢复至集中式学习性能水平。在多个 MedMNIST 医学图像数据集上同样达到中心化上界性能，验证了框架在高度异构数据分布下的鲁棒性。

【应用价值 / Applications】

该框架特别适用于数据高度敏感且分布极度不均的医学影像领域，如多医院联合诊断场景，可在保护患者隐私的同时解决数据孤岛问题。其单次通信特性大幅降低了带宽开销，模块化设计支持精确的模型遗忘，满足医疗数据的合规删除需求（如 GDPR 的"被遗忘权"），为隐私计算和联邦医疗 AI 提供了实用解决方案。
