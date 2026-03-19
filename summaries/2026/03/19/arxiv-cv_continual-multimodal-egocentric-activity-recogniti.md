---
title: "Continual Multimodal Egocentric Activity Recognition via Modality-Aware Novel Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16970"
published: "2026-03-19"
summarized: "2026-03-19T15:03:26.927622"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对多模态第一人称活动识别中的开放世界持续学习问题，提出了一种模态感知的新颖检测框架MAND。现有方法主要依赖主导模态（RGB）的logits进行新颖性评分，导致IMU等其他模态的互补线索未被充分利用，且在灾难性遗忘下问题加剧。MAND通过模态感知自适应评分（MoAS）和模态表示稳定化训练（MoRST），有效整合多模态证据并保持跨任务的模态特异性判别能力，显著提升了新颖活动检测和已知类别分类的性能。

【方法概述 / Method】
MAND框架包含两个核心组件：推理阶段的MoAS模块基于能量分数估计样本级模态可靠性，自适应地融合各模态logits以增强新颖检测；训练阶段的MoRST通过辅助头和模态级logit蒸馏，保持模态特异性表示的跨任务稳定性。该方法充分利用了RGB和IMU模态的互补信息，避免了单一模态主导导致的判别偏差。

【实验结果 / Results】
在公开的多模态第一人称基准数据集上，MAND相比最先进基线方法，新颖活动检测AUC提升高达10%，已知类别分类准确率提升达2.8%。实验结果表明，该框架有效缓解了灾难性遗忘，并显著改善了模态不平衡情况下的新颖检测性能。

【应用价值 / Applications】
该研究适用于智能眼镜、可穿戴设备等第一人称视角的开放世界活动识别场景，如健康监测、辅助生活和工业安全等领域。MAND能够在持续遇到新活动类型的动态环境中，可靠地检测未知行为并不断学习，为实际部署中的自适应人机交互系统提供了重要的技术支撑。
