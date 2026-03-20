---
title: "ITKIT: Feasible CT Image Analysis based on SimpleITK and MMEngine"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.14255"
published: "2026-03-20"
summarized: "2026-03-20T17:04:56.060156"
ai_provider: "openai"
---

【论文摘要 / Abstract】

ITKIT是一个基于SimpleITK和MMEngine开发的CT图像分析框架，旨在平衡易用性与可配置性。该框架提供了从DICOM数据到3D分割推理的完整流程，既支持计算资源有限的用户通过CLI快速上手，也为高级用户提供基于OneDL-MMEngine的灵活模型配置方案。研究通过12组典型实验验证了ITKIT在基础场景下的适用性。

【方法概述 / Method】

ITKIT整合SimpleITK进行医学图像处理，并基于MMEngine深度学习框架构建可扩展的训练与推理管道。框架采用分层设计：基础层封装DICOM读取、预处理等必要步骤；高级层通过OneDL-MMEngine支持模块化模型配置与自定义部署。

【实验结果 / Results】

论文完成了12组典型实验验证，涵盖常见CT分析场景，结果表明ITKIT能够有效满足基础临床与研究需求。框架在简化操作的同时保持了足够的灵活性，实现了低门槛入门与高级定制的平衡。

【应用价值 / Applications】

ITKIT适用于医疗资源不均衡场景，帮助基层医疗机构或计算资源受限的研究者快速开展CT图像分析。其模块化架构也支持进阶用户进行算法开发与临床部署，有望促进医学影像AI技术的普及与标准化应用。
