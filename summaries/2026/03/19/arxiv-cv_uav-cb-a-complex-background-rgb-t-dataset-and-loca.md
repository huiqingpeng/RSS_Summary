---
title: "UAV-CB: A Complex-Background RGB-T Dataset and Local Frequency Bridge Network for UAV Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17492"
published: "2026-03-19"
summarized: "2026-03-19T15:11:57.318533"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对低空无人机检测中复杂背景、伪装和多模态干扰等挑战，构建了专门强调复杂低空背景和伪装特性的RGB-T数据集UAV-CB。同时提出了局部频率桥接网络（LFBNet），通过在局部频率空间建模特征来弥合频率-空间融合差距和跨模态差异差距。大量实验表明，LFBNet在伪装和杂乱条件下达到了最先进的检测性能和强鲁棒性。

【方法概述 / Method】

LFBNet核心在于局部频率空间特征建模，将RGB和热红外（T）模态的特征转换到频率域进行处理，再桥接回空间域。该方法同时解决了两个关键问题：频率域与空间域的特征融合鸿沟，以及RGB与热红外模态之间的跨模态差异，实现了更优的多模态特征对齐与融合。

【实验结果 / Results】

在UAV-CB数据集及多个公开基准测试上，LFBNet取得了当前最优的检测性能，尤其在伪装和复杂背景场景下展现出显著的鲁棒性优势。实验验证了频率感知方法对于多模态无人机感知的有效性，突破了传统空间域方法在边界模糊、纹理混淆场景下的局限。

【应用价值 / Applications】

该研究可直接应用于低空安防系统的无人机感知与防御，如机场、关键基础设施、军事区域的无人机监测。UAV-CB数据集填补了复杂背景和伪装场景的数据空白，LFBNet的频率感知框架为实际部署中面临光照变化、遮挡和背景干扰的可靠无人机检测提供了技术支撑，具有重要的国防和民用安全价值。
