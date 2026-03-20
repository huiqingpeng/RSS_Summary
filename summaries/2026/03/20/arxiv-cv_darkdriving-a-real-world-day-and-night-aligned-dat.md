---
title: "DarkDriving: A Real-World Day and Night Aligned Dataset for Autonomous Driving in the Dark Environment"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18067"
published: "2026-03-20"
summarized: "2026-03-20T15:05:44.955722"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了首个面向自动驾驶暗光环境的真实世界昼夜对齐数据集DarkDriving，解决了现有低光增强数据集无法覆盖动态驾驶场景且缺乏精确对齐日间对应图像的问题。该数据集包含9,538对精确对齐（误差仅数厘米）的昼夜图像，并标注了2D目标边界框，支持低光增强、泛化低光增强以及面向2D/3D检测的暗光增强四项感知任务。实验表明，DarkDriving为评估自动驾驶低光增强提供了全面基准，并可泛化至nuScenes等其他低光驾驶场景。

【方法概述 / Method】
作者提出了一种基于自动昼夜轨迹跟踪的位姿匹配方法（TTPM），在占地69英亩的大型真实封闭驾驶测试场中采集数据。该方法通过轨迹跟踪实现动态驾驶场景下昼夜图像的精确空间对齐，克服了传统静态场景小范围曝光控制的局限性。

【实验结果 / Results】
DarkDriving实现了昼夜图像对在位置和内容上的高精度对齐，对齐误差仅为数厘米量级；数据集支持四项感知任务的基准评估，实验验证了其在低光图像增强和暗光目标检测方面的有效性，并展现出对nuScenes等其他低光驾驶数据集的泛化能力。

【应用价值 / Applications】
该研究为自动驾驶系统在夜间低光环境下的视觉感知提供了关键的数据支撑和评估基准，可直接用于提升夜间行车安全性；其TTPM采集方法可扩展至其他动态场景的跨时相对齐数据采集，泛化能力使其能适配多种自动驾驶数据集和实际部署场景。
