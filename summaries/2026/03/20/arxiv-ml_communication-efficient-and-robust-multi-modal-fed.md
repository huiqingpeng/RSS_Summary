---
title: "Communication-Efficient and Robust Multi-Modal Federated Learning via Latent-Space Consensus"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19067"
published: "2026-03-20"
summarized: "2026-03-20T12:18:35.788487"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CoMFed框架，用于解决多模态联邦学习中的异构性和通信效率问题。该框架通过可学习的投影矩阵生成压缩的潜在表示，并引入潜在空间正则化器来对齐不同客户端的表示，从而提升跨模态一致性和对异常值的鲁棒性。在人体活动识别基准测试上的实验表明，CoMFed在保持竞争精度的同时显著降低了通信开销。

【方法概述 / Method】
CoMFed采用可学习的投影矩阵将各客户端的异构模态特征映射到共享的压缩潜在空间，实现跨架构的特征对齐。通过潜在空间共识正则化项约束不同客户端的潜在表示保持一致，同时利用压缩表示减少通信传输量。

【实验结果 / Results】
在人体活动识别基准数据集上的实验表明，CoMFed在准确率方面达到了与集中式训练相当的竞争性能。该方法显著降低了通信开销，实现了高效的模型聚合，并对数据异常值表现出较强的鲁棒性。

【应用价值 / Applications】
CoMFed适用于分布式多模态感知场景，如智能手机、可穿戴设备和物联网传感器网络中的协同健康监测与活动识别。该框架在保护用户隐私的前提下，实现了跨设备的异构数据高效协作建模，对边缘智能和联邦医疗AI具有重要应用价值。
