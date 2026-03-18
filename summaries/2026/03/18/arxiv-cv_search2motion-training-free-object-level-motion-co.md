---
title: "Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16711"
published: "2026-03-18"
summarized: "2026-03-18T18:18:07.782787"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出 Search2Motion，一种无需训练的对象级运动编辑框架，用于图像到视频生成。与需要轨迹、边界框、掩码或运动场等先验方法不同，该框架采用基于目标帧的控制方式，利用首末帧运动先验实现对象重定位，同时保持场景稳定性且无需微调。作者进一步发现早期自注意力图可预测对象和相机动态，并据此提出 ACE-Seed 轻量级搜索策略以提升运动保真度，同时构建了专门分离对象与相机运动的评估基准和指标。

【方法概述 / Method】

Search2Motion 的核心方法包括：通过语义引导的对象插入和鲁棒背景修复构建可靠的目标帧；利用早期步骤的自注意力图预测对象与相机动态，为用户提供可解释的反馈；提出 ACE-Seed（Attention Consensus for Early-step Seed selection）搜索策略，通过注意力共识机制选择最优种子，无需前瞻采样或外部评估器即可提升运动保真度。

【实验结果 / Results】

该研究在 FLF2V-obj 和 VBench 基准上持续超越基线方法；提出的 S2M-DAVIS 和 S2M-OMB 基准专门用于稳定相机、仅对象运动的评估；FLF2V-obj 指标能够在无需真实轨迹的情况下隔离对象伪影，实现了更精准的对象级运动质量评估。

【应用价值 / Applications】

Search2Motion 可广泛应用于视频内容创作、影视后期制作和交互式媒体生成等领域，使创作者能够通过简单的目标帧指定实现精确的对象运动控制，无需复杂的标注或模型微调，显著降低专业视频编辑的技术门槛，提升创作效率和灵活性。
