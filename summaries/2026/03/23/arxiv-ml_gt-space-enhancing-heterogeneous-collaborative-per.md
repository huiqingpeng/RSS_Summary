---
title: "GT-Space: Enhancing Heterogeneous Collaborative Perception with Ground Truth Feature Space"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19308"
published: "2026-03-23"
summarized: "2026-03-24T07:16:25.761547"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GT-Space，一种面向异构多智能体协同感知的新型框架，用于解决自动驾驶中不同感知模态或模型架构带来的特征融合难题。该方法通过从真实标签（ground-truth）构建统一的公共特征空间，为异构特征对齐提供参考标准，使各智能体仅需单一适配器模块即可完成特征投影，无需与其他智能体进行成对交互。实验表明，GT-Space在仿真数据集（OPV2V、V2XSet）和真实数据集（RCooper）上均显著优于基线方法，实现了更高的检测精度和更强的鲁棒性。

【方法概述 / Method】
GT-Space的核心创新在于利用ground-truth标签构建"真实特征空间"作为异构特征对齐的统一参照系，替代传统方法中需要成对训练或设计解释器模块的做法。每个智能体只需配备一个轻量级适配器，将自身特征投影到该共享空间；同时，作者设计了基于对比学习的融合网络，通过跨多种模态组合的对比损失进行训练，增强特征表示的判别性和泛化能力。

【实验结果 / Results】
在OPV2V、V2XSet两个仿真数据集以及RCooper真实世界数据集上的大量实验表明，GT-Space在检测精度上持续超越现有基线方法。该框架展现出对多样化模态组合的强鲁棒性，验证了其在异构协同感知场景中的有效性和可扩展性。

【应用价值 / Applications】
GT-Space为自动驾驶中的车路协同、车车协同感知提供了可扩展的技术方案，能够灵活兼容不同厂商的传感器配置和模型架构，降低多智能体系统部署的复杂度和通信开销。该方法还可推广至其他需要异构数据融合的分布式感知场景，如智能交通系统和多机器人协作等。
