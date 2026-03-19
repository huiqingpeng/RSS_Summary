---
title: "Revisiting Cross-Attention Mechanisms: Leveraging Beneficial Noise for Domain-Adaptive Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17474"
published: "2026-03-19"
summarized: "2026-03-19T15:11:36.398727"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对无监督域适应（UDA）中存在的域差异和尺度差异问题，提出了"有益噪声"（beneficial noise）的概念，通过向交叉注意力机制注入受控扰动来增强模型对内容语义的保持能力。作者构建了Domain-Adaptive Cross-Scale Matching（DACSM）框架，包含Domain-Adaptive Transformer（DAT）和Cross-Scale Matching（CSM）两个核心模块。实验表明，DACSM在VisDA-2017、Office-Home和DomainNet数据集上达到最优性能，相比CDTrans提升达2.3%，在处理尺度差异较大的"truck"类别时提升高达5.9%。

【方法概述 / Method】
DACSM框架由两个关键组件构成：Domain-Adaptive Transformer（DAT）通过向交叉注意力注入有益噪声，实现渐进式域迁移并解耦域共享内容与域特定风格；Cross-Scale Matching（CSM）模块则在多分辨率层面自适应对齐特征，确保尺度变化下的语义一致性。有益噪声作为一种正则化手段，迫使模型忽略风格干扰、聚焦核心内容。

【实验结果 / Results】
在VisDA-2017、Office-Home和DomainNet三个标准UDA基准数据集上，DACSM均取得最优性能。具体而言，相比当前先进的CDTrans方法，DACSM在VisDA-2017上整体提升2.3%；在处理大尺度差异的"truck"类别时，性能提升显著达到5.9%，充分验证了有益噪声对尺度差异的鲁棒性。

【应用价值 / Applications】
该研究为计算机视觉中的跨域迁移学习提供了新思路，可广泛应用于自动驾驶（如不同天气/光照条件下的目标识别）、医学影像分析（如跨设备、跨医院的诊断模型迁移）以及工业质检等场景，有效降低模型在新域部署时对大量标注数据的依赖，提升模型在复杂环境下的泛化能力。
