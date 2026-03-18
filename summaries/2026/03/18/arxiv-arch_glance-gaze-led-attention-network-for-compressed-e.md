---
title: "GLANCE: Gaze-Led Attention Network for Compressed Edge-inference"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.15717"
published: "2026-03-18"
summarized: "2026-03-18T14:52:32.945524"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出GLANCE（Gaze-Led Attention Network for Compressed Edge-inference），一种面向AR/VR系统的实时目标检测方法。该方法受生物中央凹视觉启发，采用两阶段流水线：首先通过可微分无权重神经网络实现超低功耗视线估计（仅需393次乘加运算和2.2 KiB内存），然后利用视线预测引导注意力区域的目标检测，将计算负担降低40-50%、能耗降低65%。在Arduino Nano 33 BLE上部署后，系统在COCO数据集上达到48.1% mAP（关注区域51.8%），延迟低于10毫秒，相比全局YOLOv12n基线，对小/中/大目标的检测精度分别从39.2%/63.4%/83.1%提升至51.3%/72.1%/88.1%。

【方法概述 / Method】

GLANCE采用"视线估计→注意力引导检测"的两阶段架构。视线估计阶段使用可微分无权重神经网络（weightless neural networks），通过内存查表替代传统的乘加运算实现超低功耗跟踪；目标检测阶段利用预测的视线位置定义感兴趣区域（ROI），仅对高分辨率关注区域进行精细检测，其余区域保持低分辨率处理。

【实验结果 / Results】

视线估计模块实现8.32°角误差，仅消耗393 MACs和2.2 KiB内存每帧。完整系统在Arduino Nano 33 BLE边缘设备上达到48.1% mAP（COCO），关注区域内提升至51.8%，同时保持亚10毫秒延迟。相比全局YOLOv12n，ROI方法将通信时间改善177倍，对小、中、大目标的检测精度分别提升12.1、8.7和5.0个百分点。

【应用价值 / Applications】

该研究为资源受限的可穿戴AR/VR设备提供了高效的实时目标检测解决方案，特别适用于需要低延迟（<10ms）、低功耗的沉浸式交互场景。内存中心架构与显式注意力建模的结合，为边缘智能设备上的视觉感知任务提供了新的设计范式，可扩展至智能眼镜、头戴显示器等移动平台。
