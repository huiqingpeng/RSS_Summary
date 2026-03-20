---
title: "LucidNFT: LR-Anchored Multi-Reward Preference Optimization for Generative Real-World Super-Resolution"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.05947"
published: "2026-03-20"
summarized: "2026-03-20T16:18:17.312500"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了LucidNFT，一种用于真实世界图像超分辨率（Real-ISR）的多奖励强化学习框架。针对生成式Real-ISR中存在的语义/结构幻觉问题（输出看似清晰但与低分辨率输入证据不符），该研究设计了LucidConsistency评估器来实现无需高分辨率真值的LR锚定保真度度量，并提出解耦优势归一化策略解决多目标优化中的优势崩溃问题，同时构建了大规模真实退化数据集LucidLR。实验表明，LucidNFT在多样真实场景下实现了更优的感知质量-保真度权衡，且优化动态稳定。

【方法概述 / Method】

LucidNFT基于流匹配（flow-matching）Real-ISR模型，采用多奖励偏好优化框架进行微调。核心组件包括：（1）LucidConsistency——一种退化鲁棒的语义评估器，通过对比学习从LR输入提取语义特征，实现无需HR真值的LR锚定保真度评估；（2）解耦优势归一化策略——先在每个目标维度内独立归一化保留目标间对比度，再融合多奖励，避免传统标量化归一化导致的优势崩溃；（3）利用LucidLR数据集扩展真实退化覆盖范围以增强rollout多样性。

【实验结果 / Results】

LucidNFT在多个强流式Real-ISR基线模型上实现了一致性提升，在感知质量与LR保真度的帕累托前沿上取得更优权衡。消融实验验证了LucidConsistency对退化鲁棒性的关键作用，以及解耦归一化相比naive标量化方法在稳定优化动态、防止优势崩溃方面的有效性。在多样真实世界场景下的测试表明该方法具有良好的泛化能力。

【应用价值 / Applications】

该研究适用于智能手机摄影、安防监控、医学影像、卫星遥感等真实世界低质量图像增强场景，可在缺乏高分辨率参考的情况下生成既视觉自然又忠实于原始证据的重建结果。LucidConsistency评估器及LucidLR数据集为Real-ISR的自动化质量评估和模型训练提供了可复用的基础设施，推动生成式图像复原技术向实用化部署迈进。
