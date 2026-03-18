---
title: "EPOFusion: Exposure aware Progressive Optimization Method for Infrared and Visible Image Fusion"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16130"
published: "2026-03-18"
summarized: "2026-03-18T18:06:20.213573"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种曝光感知的红外与可见光图像融合方法EPOFusion，旨在解决过曝区域信息丢失的问题。该方法通过引入引导模块帮助编码器从过曝区域提取细粒度红外特征，并设计了迭代解码器逐步增强融合图像质量。此外，研究还构建了首个红外-可见光过曝数据集IVOE，实验表明EPOFusion在过曝和非过曝区域均实现了优异的融合效果。

【方法概述 / Method】

EPOFusion采用三阶段架构：首先利用引导模块辅助编码器提取过曝区域的红外特征；然后通过多尺度上下文融合模块的迭代解码器逐步优化融合结果；最后采用自适应损失函数动态约束融合过程，实现不同曝光条件下模态间的有效平衡。

【实验结果 / Results】

实验结果表明EPOFusion在过曝区域保持了红外线索，同时在非过曝区域实现了视觉保真的融合效果。该方法在视觉质量和下游任务性能上均优于现有方法，相关代码、融合结果及IVOE数据集将公开发布。

【应用价值 / Applications】

该研究适用于自动驾驶、夜间监控、军事侦察等存在强光或过曝场景的视觉感知系统。通过有效融合红外热信息与可见光细节，可提升复杂光照环境下的目标检测与场景理解能力，为实际应用提供更鲁棒的感知解决方案。
