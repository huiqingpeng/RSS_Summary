---
title: "VLOD-TTA: Test-Time Adaptation of Vision-Language Object Detectors"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.00458"
published: "2026-03-18"
summarized: "2026-03-18T18:27:23.302284"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了VLOD-TTA，首个针对视觉-语言目标检测器（VLODs）的高效测试时自适应方法。现有VLODs（如YOLO-World和Grounding DINO）虽具备强大的零样本泛化能力，但在分布偏移下性能显著下降。VLOD-TTA通过IoU加权熵目标和图像条件提示选择机制，以低额外开销实现了对VLODs的在线自适应，在多种分布偏移场景（艺术风格、恶劣天气、低光照、常见损坏）下均优于现有基线和先前最优方法。

【方法概述 / Method】
VLOD-TTA包含两个核心组件：（1）IoU加权熵目标函数，利用密集提议框的重叠信息，强调空间连贯的提议聚类，同时缓解孤立框带来的确认偏差；（2）图像条件提示选择策略，通过图像级兼容性对提示进行排序，并聚合最具信息量的提示分数用于检测。该方法避免了先前mean-teacher框架带来的显著延迟和内存开销。

【实验结果 / Results】
实验在YOLO-World和Grounding DINO两种主流VLOD上展开，涵盖艺术领域、恶劣天气驾驶条件、低光照图像及常见图像损坏等多样化分布偏移场景。结果表明，VLOD-TTA在所有测试场景下均稳定超越标准TTA基线方法，并优于现有的最先进方法，同时保持了较低的计算开销。

【应用价值 / Applications】
VLOD-TTA可广泛应用于需要实时适应新环境的视觉-语言目标检测系统，如自动驾驶车辆在恶劣天气或夜间条件下的目标感知、艺术风格图像的内容理解、以及部署在边缘设备上需应对图像质量退化的智能监控系统，为实际部署提供了高效、低延迟的在线自适应解决方案。
