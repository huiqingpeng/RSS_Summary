---
title: "Dual Stream Independence Decoupling for True Emotion Recognition under Masked Expressions"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16760"
published: "2026-03-18"
summarized: "2026-03-18T18:20:20.950846"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对从伪装表情中识别真实情感的难题，提出了一种基于apex帧的新范式——从达到稳定伪装状态的apex帧中分类真实情感，而非使用传统 onset 帧范式。同时，作者设计了双流独立解耦框架，通过解耦损失组（包含两个分类损失和一个Hilbert-Schmidt独立性损失）实现真实情感特征与伪装表情特征的独立学习。实验表明，apex帧范式更具挑战性，且所提解耦框架显著提升了识别性能。

【方法概述 / Method】
论文采用双流网络架构，分别学习真实情感特征和伪装表情特征，并通过设计的解耦损失组进行优化：两个分类损失分别监督真实情感和伪装表情的学习，Hilbert-Schmidt独立性损失（HSIC）则强制两类特征相互独立，避免伪装表情对真实情感的干扰。

【实验结果 / Results】
实验验证了apex帧范式相比传统onset帧范式更具挑战性，更能反映实际伪装场景；所提双流独立解耦框架在该范式下有效提升了真实情感识别性能，证明了特征解耦策略在抑制伪装干扰方面的有效性。

【应用价值 / Applications】
该研究可应用于安全监控、司法审讯、心理评估等需要识别被掩饰真实情感的场景，为智能情感计算系统提供了更鲁棒的伪装表情分析技术，有助于提升人机交互中的情感理解准确性和可信度。
