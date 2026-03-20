---
title: "Training-Free Sparse Attention for Fast Video Generation via Offline Layer-Wise Sparsity Profiling and Online Bidirectional Co-Clustering"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18636"
published: "2026-03-20"
summarized: "2026-03-20T15:13:41.588706"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SVOO，一种无需训练的高效视频生成稀疏注意力框架，通过离线逐层稀疏性分析和在线双向协同聚类来解决现有方法忽视层间异质性和查询-键耦合的问题。研究发现注意力稀疏性是各层的内在属性，在不同输入间变化较小。在七个主流视频生成模型上的实验表明，SVOO在Wan2.1上实现了最高1.93倍加速，同时保持高达29 dB的PSNR，取得了质量与速度的最优平衡。

【方法概述 / Method】
SVOO采用两阶段范式：离线阶段通过逐层敏感性分析确定各层固有的剪枝比例，在线阶段通过新颖的双向协同聚类算法实现块级稀疏注意力。该方法无需重新训练模型，可直接应用于预训练的扩散Transformer视频生成模型。

【实验结果 / Results】
在七个广泛使用的视频生成模型上进行大量实验，SVOO相比现有最优方法取得了更优的质量-速度权衡。具体而言，在Wan2.1模型上实现了1.93倍的推理加速，同时保持29 dB的峰值信噪比（PSNR），表明在显著提升效率的同时几乎无损生成质量。

【应用价值 / Applications】
该研究可直接部署于现有的视频生成服务（如Runway、Pika等），大幅降低推理成本和延迟，支持实时或低延迟视频生成应用。对于资源受限的边缘设备和云端部署场景，SVOO提供了一种即插即用的加速方案，无需昂贵的模型重训练即可提升DiT视频生成模型的实用性。
