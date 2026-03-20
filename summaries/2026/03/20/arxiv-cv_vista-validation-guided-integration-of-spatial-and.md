---
title: "VISTA: Validation-Guided Integration of Spatial and Temporal Foundation Models with Anatomical Decoding for Rare-Pathology VCE Event Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18343"
published: "2026-03-20"
summarized: "2026-03-20T15:07:39.275139"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了VISTA框架，用于解决胶囊内窥镜（VCE）中罕见病理事件检测的挑战。作者将RARE-VISION任务重新定义为度量对齐的事件检测问题，而非单纯的逐帧分类任务。该框架整合了EndoFM-LV（局部时序上下文）和DINOv3 ViT-L/16（帧级视觉语义）两种互补骨干网络，并通过验证引导的分层融合与解剖感知时序事件解码，在隐藏测试集上取得了temporal mAP@0.5为0.3530、temporal mAP@0.95为0.3235的优异性能。

【方法概述 / Method】
VISTA采用双骨干架构：EndoFM-LV捕获局部时序信息，DINOv3提取强视觉语义特征。方法核心包括三部分：（1）多样化头集成（Diverse Head Ensemble）生成多视角预测；（2）验证引导的分层融合（Validation-Guided Hierarchical Fusion），利用验证集数据实现类别级模型加权、骨干网络加权和概率校准；（3）解剖感知时序事件解码（Anatomy-Aware Temporal Event Decoding），通过时序平滑、解剖约束、阈值优化和逐标签事件生成获得稳定的事件级预测。

【实验结果 / Results】
消融实验表明，互补双骨干设计、验证引导融合策略以及解剖感知时序解码均对事件级性能有显著贡献。在官方隐藏测试集上，该方法达到temporal mAP@0.5 = 0.3530和temporal mAP@0.95 = 0.3235，在严格的事件级评估指标下展现出较强的检测能力，验证了框架各组件的有效性。

【应用价值 / Applications】
该研究直接应用于胶囊内窥镜视频的自动化罕见病理事件检测，可辅助胃肠科医生快速定位关键诊断片段，减少阅片时间和漏诊风险。验证引导的融合策略和解剖感知解码机制具有良好的可迁移性，可推广至其他长视频医学影像分析任务，为稀疏、异质性医学事件的智能检测提供通用技术框架。
