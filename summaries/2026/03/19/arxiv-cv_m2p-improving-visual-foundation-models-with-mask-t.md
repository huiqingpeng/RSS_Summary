---
title: "M2P: Improving Visual Foundation Models with Mask-to-Point Weakly-Supervised Learning for Dense Point Tracking"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17813"
published: "2026-03-19"
summarized: "2026-03-19T15:18:21.313853"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出 Mask-to-Point (M2P) 弱监督学习方法，利用视频对象分割（VOS）掩码标注来提升视觉基础模型（VFMs）在密集点跟踪任务中的性能。M2P 引入三种基于掩码的约束损失：局部结构一致性损失、掩码标签一致性损失和掩码边界约束，有效解决静态图像预训练模型难以捕捉视频时序对应关系的问题。实验表明，仅用 3.6K 个 VOS 训练视频，M2P 在 TAP-Vid-DAVIS 基准上相比 DINOv2-B/14 和 DINOv3-B/16 分别提升 12.8% 和 14.6%，并可作为通用预训练模型服务于多种点跟踪任务。

【方法概述 / Method】

M2P 采用弱监督表示学习框架，将视频对象分割掩码转化为点级别的监督信号。具体而言，通过 Procrustes 分析的局部结构一致性损失建模局部区域内点的协同运动，掩码标签一致性（MLC）损失确保采样前景点跨帧匹配前景区以稳定训练，掩码边界约束则显式监督边界点。该方法仅需掩码标注，无需人工标注的密集点轨迹。

【实验结果 / Results】

M2P 在 TAP-Vid-DAVIS 基准上取得显著性能提升：相比 DINOv2-B/14 提升 12.8%，相比 DINOv3-B/16 提升 14.6%。仅用 3.6K 个 VOS 训练视频即可高效完成训练，且预训练后的模型可同时支持测试时优化和离线微调的 TAP 任务，展现出良好的通用性。

【应用价值 / Applications】

M2P 为视频理解领域提供了高效的视觉基础模型增强方案，可广泛应用于运动分析、视频编辑、机器人导航、增强现实等需要密集点跟踪的场景。其弱监督特性降低了对昂贵点轨迹标注的依赖，使得利用现有大规模 VOS 数据集提升模型性能成为可能，具有较强的实用性和可扩展性。
