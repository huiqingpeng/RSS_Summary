---
title: "GeoBridge: A Semantic-Anchored Multi-View Foundation Model Bridging Images and Text for Geo-Localization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.02697"
published: "2026-03-18"
summarized: "2026-03-18T18:30:04.258469"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出GeoBridge，一种语义锚定的多视角基础模型，突破了传统以卫星为中心的地理定位范式，实现了跨视角（无人机、街景、卫星）和跨模态（图像与文本）的双向匹配与语言到图像的检索。为支持该研究，作者构建了首个大规模跨模态多视角对齐数据集GeoLoc，包含超过50,000对来自36个国家的图像-文本对。实验表明，GeoLoc预训练显著提升了GeoBridge的地理定位精度，并促进了跨域泛化和跨模态知识迁移。

【方法概述 / Method】
GeoBridge的核心创新在于**语义锚定机制（semantic-anchor mechanism）**，该机制通过文本描述作为桥梁来对齐多视角图像特征，而非直接学习视角间的视觉映射。模型采用多视角编码器分别处理无人机、街景全景和卫星图像，并利用文本编码器将自然语言描述嵌入到统一的语义空间，从而实现灵活的跨模态检索与定位。

【实验结果 / Results】
实验表明，在GeoLoc数据集上的预训练使GeoBridge在多个地理定位任务中取得显著提升，包括跨视角图像检索和文本到图像的地理定位。模型展现出强大的跨域泛化能力，能够适应不同地理区域的分布差异，同时实现了有效的跨模态知识迁移，证明了文本语义作为多视角对齐桥梁的有效性。

【应用价值 / Applications】
GeoBridge可应用于缺乏高分辨率或最新卫星图像的场景，如灾害应急响应、导航定位和城市计算等实际任务。其支持自然语言查询的能力使非专业用户也能通过描述性文本进行地理位置检索，为智能交通、增强现实导航和地理信息检索系统提供了更灵活、鲁棒的解决方案。
