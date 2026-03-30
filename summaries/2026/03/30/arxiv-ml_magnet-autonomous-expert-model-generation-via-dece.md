---
title: "MAGNET: Autonomous Expert Model Generation via Decentralized Autoresearch and BitNet Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25813"
published: "2026-03-30"
summarized: "2026-03-31T07:18:01.336558"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出MAGNET（Model Autonomously Growing Network），一个去中心化的自主系统，用于在通用硬件上自动生成、训练和服务领域专家语言模型。该系统整合了自主机器学习研究流程、BitNet三值训练、分布式模型聚合和区块链贡献追踪四大核心组件，并通过三个案例研究验证了效果：视频安全分类准确率从0.9287提升至0.9851，加密货币方向预测命中率从41%提升至54.9%，以及BitNet超参数优化使验证损失降低16.7%。

【方法概述 / Method】
MAGNET采用四层架构实现自主模型进化：（1）autoresearch模块自动化完成数据集生成、超参数探索、评估和错误驱动的迭代优化；（2）基于BitNet b1.58的三值量化训练，实现无需GPU的CPU原生推理；（3）采用DiLoCo算法进行通信高效的分布式模型聚合，融合各领域专家模型；（4）在HOOTi EVM链上实现贡献的链上追踪与激励。

【实验结果 / Results】
三项案例研究验证了系统有效性：视频安全分类任务中平衡准确率提升6.1个百分点（0.9287→0.9851）；加密货币价格方向预测命中率提升13.9个百分点（41%→54.9%）；BitNet超参数经过10阶段扫描优化后，验证损失降低16.7%。这些结果表明自主研究流程能够持续发现并应用更优的模型配置。

【应用价值 / Applications】
MAGNET使低成本、去中心化的专家模型开发成为可能，特别适用于GPU资源受限的场景和需要快速适配特定垂直领域的应用，如内容安全审核、金融预测分析等。该系统通过区块链激励机制可构建开放的协作研究网络，降低AI研发的中心化门槛，推动边缘计算和联邦学习场景下的民主化AI发展。
