---
title: "Rethinking UMM Visual Generation: Masked Modeling for Efficient Image-Only Pre-training"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16139"
published: "2026-03-18"
summarized: "2026-03-18T18:06:37.451612"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对统一多模态模型（UMMs）视觉生成组件预训练效率低下的问题，提出了一种高效的数据节约型训练框架IOMM。该框架通过两阶段训练策略，第一阶段仅使用大量无标注图像数据进行视觉生成组件的预训练，第二阶段使用少量文本-图像对进行微调，从而摆脱了对稀缺配对数据的依赖。实验表明，IOMM不仅显著提升了训练效率，还在GenEval和WISE基准上取得了SOTA性能。

【方法概述 / Method】
IOMM采用掩码建模（Masked Modeling）作为核心预训练范式，在第一阶段完全基于图像自监督学习进行视觉生成能力建模，避免使用昂贵的文本-图像配对数据；第二阶段通过混合无标注图像和少量精选文本-图像对进行指令对齐微调，实现多模态生成能力。

【实验结果 / Results】
IOMM-B（3.6B参数）模型从头训练仅需约1050 H800 GPU小时，其中1000小时用于高效的图像预训练阶段。该模型在GenEval上达到0.89、在WISE上达到0.55，超越了BAGEL-7B（0.82/0.55）和BLIP3-o-4B（0.84/0.50）等强基线模型。

【应用价值 / Applications】
该方法大幅降低多模态视觉生成模型的训练成本，使学术界和工业界能够以更少的计算资源开发高性能视觉生成系统；同时减少对稀缺高质量配对数据的依赖，为数据受限场景下的视觉生成模型开发提供了可行路径。
