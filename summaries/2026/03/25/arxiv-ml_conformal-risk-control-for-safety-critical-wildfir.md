---
title: "Conformal Risk Control for Safety-Critical Wildfire Evacuation Mapping: A Comparative Study of Tabular, Spatial, and Graph-Based Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22331"
published: "2026-03-25"
summarized: "2026-03-26T07:12:15.272473"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究首次将共形风险控制（CRC）应用于野火蔓延预测领域，为假阴性率（FNR ≤ 0.05）提供有限样本保证。研究发现，尽管深度学习模型（Tiny U-Net AUROC 0.969，Hybrid ResGNN-UNet AUROC 0.964）在标准阈值下表现优异，但仅能捕获7-72%的真实火蔓延区域；而CRC能够统一消除这一缺陷。核心发现表明：模型架构决定疏散效率，CRC决定安全性——空间模型配合CRC可在标记约15%像素的情况下实现约95%的火区覆盖，效率比LightGBM高4.2倍，而图神经网络的额外复杂性并未带来显著效率提升。

【方法概述 / Method】

研究采用共形风险控制（CRC）框架，为三种不同复杂度的模型家族提供分布无关的安全保证：表格模型（LightGBM）、卷积模型（Tiny U-Net）和图模型（Hybrid ResGNN-UNet）。作者进一步提出"位移感知三方CRC框架"，将预测区域划分为SAFE/MONITOR/EVACUATE三个操作区域，以支持分级疏散决策。

【实验结果 / Results】

标准概率阈值方法在三种模型上表现严重不佳，火区覆盖率仅7-72%；而应用CRC后，所有模型均达到95%的火区覆盖率保证。空间模型（Tiny U-Net和ResGNN-UNet）配合CRC仅需标记约15%的总像素即可满足安全保证，而LightGBM需标记约63%的像素。研究还揭示了在极端类别不平衡（火区 prevalence ≈ 5%）下，基于流行率加权的边界存在根本性局限。

【应用价值 / Applications】

该研究为野火疏散规划提供了首个具有形式化安全保证的决策工具，可直接应用于应急管理系统的实时疏散地图生成。提出的三方分区框架（安全/监测/疏散）支持操作层面的分级响应策略，在保障生命安全的同时优化疏散资源调配效率。所有模型、校准代码和评估流程均已开源，便于实际部署和进一步研究。
