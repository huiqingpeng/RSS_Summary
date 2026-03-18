---
title: "IMAIA: Interactive Maps AI Assistant for Travel Planning and Geo-Spatial Intelligence"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2507.06993"
published: "2026-03-18"
summarized: "2026-03-18T19:06:07.495333"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了IMAIA（Interactive Maps AI Assistant），一个支持自然语言交互的地图AI助手，能够同时处理矢量地图、卫星影像和相机输入，实现地理空间智能问答。该系统包含两个核心组件：Maps Plus通过将地图解析为网格对齐表示来支持语言模型查询，PAISA则融合图像-地点嵌入与地理空间信号实现相机感知的位置理解。实验表明，IMAIA在地图中心问答和相机到地点定位任务上显著优于强基线模型，同时保持了低延迟和可解释性。

【方法概述 / Method】
IMAIA采用轻量级多智能体架构，包含两个互补组件：Maps Plus将平铺的矢量/卫星视图解析为网格对齐表示，使语言模型能够解析指示性引用（如"右上角公园旁的花形建筑"）；PAISA通过融合图像-地点嵌入与地理空间信号（位置、朝向、邻近度）实现场景定位和属性提取。该设计通过暴露可解释的中间决策来保持低延迟。

【实验结果 / Results】
在地图中心问答和相机到地点定位任务中，IMAIA相比强基线模型在准确性和响应速度上均有提升，同时保持了对用户部署的实用性。系统成功实现了自然语言与地图、地理空间线索的统一，支持对话式空间交互。

【应用价值 / Applications】
IMAIA可广泛应用于智能旅行规划、增强现实导航、位置感知信息检索等场景，帮助用户通过自然语言理解周围环境。该系统突破了传统地图应用的点击交互限制，为移动设备上的实时地理空间智能服务提供了可行方案，具有显著的商业化和用户体验提升潜力。
