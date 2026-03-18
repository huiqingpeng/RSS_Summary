---
title: "USIS-PGM: Photometric Gaussian Mixtures for Underwater Salient Instance Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.13961"
published: "2026-03-18"
summarized: "2026-03-18T19:04:04.225227"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了USIS-PGM，一种用于水下显著实例分割（USIS）的单阶段框架，以解决水下图像退化带来的挑战。该方法通过频率感知模块增强边界线索，利用动态加权模块进行内容自适应特征重加权，并采用基于Transformer的实例激活模块区分显著实例。此外，论文引入光度高斯混合（PGM）生成多尺度高斯热图来监督中间解码器特征，从而提升显著实例定位精度并生成结构更连贯的分割掩码。

【方法概述 / Method】
USIS-PGM采用编码器-解码器架构，编码器包含频率感知模块和动态加权模块以增强特征表示；解码器集成Transformer-based实例激活模块实现实例级区分。核心创新在于PGM机制，该机制从真实掩码生成多尺度高斯热图，作为中间监督信号引导网络学习更精确的空间定位和结构信息。

【实验结果 / Results】
实验结果表明USIS-PGM模型具有优越性能和实际应用价值（注：原文摘要未提供具体量化指标，完整实验结果需参考论文正文）。

【应用价值 / Applications】
该研究对海洋机器人系统具有重要价值，可实现水下显著目标检测与实例级掩码预测，支持水下视觉场景理解。潜在应用包括水下自主导航、海洋生物监测、海底资源勘探及水下机器人抓取等任务。
