---
title: "Efficient Video Diffusion with Sparse Information Transmission for Video Compression"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18501"
published: "2026-03-20"
summarized: "2026-03-20T15:10:24.718441"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Diff-SIT，一种用于视频压缩的高效扩散模型，通过稀疏信息传输机制在超低比特率下实现高质量重建。该方法包含稀疏时序编码模块（STEM）和单步视频扩散模型（ODFTE），前者将原始帧序列稀疏编码为信息丰富的中间序列以节省比特率，后者利用帧类型嵌入器（FTE）进行自适应重建。实验表明，Diff-SIT在感知质量和时序一致性方面达到了新的最先进水平，尤其在超低比特率场景下表现突出。

【方法概述 / Method】
Diff-SIT采用两阶段架构：STEM模块通过稀疏编码策略将输入视频帧压缩为信息密集的中间表示，显著降低传输比特率；ODFTE模块则以单步扩散方式整体处理中间序列，并引入帧类型嵌入器（FTE）根据I帧/P帧等不同类型进行自适应重建，充分利用时序相关性。

【实验结果 / Results】
在多个标准数据集上的大量实验验证，Diff-SIT在感知质量和时序一致性指标上均达到当前最优水平，特别是在极具挑战性的超低比特率条件下，相比传统端到端压缩模型和现有生成式压缩方法，有效解决了图像模糊和时序不连贯问题。

【应用价值 / Applications】
该研究适用于带宽受限场景下的视频传输与存储，如移动流媒体、实时监控和视频会议等超低比特率应用，能够在有限带宽条件下提供高感知质量和流畅时序体验，具有重要的实际部署价值。
