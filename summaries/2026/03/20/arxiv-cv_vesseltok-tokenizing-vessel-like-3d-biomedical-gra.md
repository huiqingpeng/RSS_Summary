---
title: "VesselTok: Tokenizing Vessel-like 3D Biomedical Graph Representations for Reconstruction and Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18797"
published: "2026-03-20"
summarized: "2026-03-20T15:16:48.022075"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了VesselTok框架，用于学习血管状3D生物医学空间图的潜在表示（token）。该方法从参数化形状视角出发，利用中心线点与伪半径编码管状几何结构，学习基于中心线点的神经隐式表示。实验表明，VesselTok在肺气道、肺血管和脑血管等多种解剖结构上表现稳健，其学习的潜在表示能够泛化到未见解剖结构、支持生成合理的解剖图，并可有效迁移到链接预测等下游逆问题。

【方法概述 / Method】
VesselTok将高分辨率空间密集图视为参数化形状，通过中心线点配合伪半径来编码管状几何结构，并学习以中心线点为条件的神经隐式表示作为新颖的潜在表示（token）。

【实验结果 / Results】
VesselTok在肺气道、肺血管和脑血管等多种复杂拓扑结构上验证了有效性，证明其学习的潜在表示具有三方面能力：（i）泛化到未见解剖结构，（ii）支持解剖图的生成建模，（iii）有效迁移至链接预测等下游逆问题。

【应用价值 / Applications】
该研究可应用于临床和生物医学研究中的管状解剖结构（如血管、气道、神经元网络）建模，支持医学图像重建、解剖结构生成以及缺失连接预测等任务，为大规模高分辨率生物网络分析提供计算高效的表示学习方法。
