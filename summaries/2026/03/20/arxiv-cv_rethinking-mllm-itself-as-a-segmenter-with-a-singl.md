---
title: "Rethinking MLLM Itself as a Segmenter with a Single Segmentation Token"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19026"
published: "2026-03-20"
summarized: "2026-03-20T15:18:19.152303"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为SELF1E的新方法，首次实现了无需外部专业掩码解码器的多模态大语言模型（MLLM）分割。通过仅使用单个分割token，该研究解决了MLLM中像素重排图像特征分辨率降低的根本问题，在多个分割任务上取得了与基于专业解码器方法相竞争的性能，证明了MLLM本身即可作为分割器的可行性。

【方法概述 / Method】
该方法通过保留图像特征的原始未压缩分辨率，并用从MLLM处理后的压缩特征中提取的残差特征进行填充，从而提升特征精度。同时，结合像素反重排操作和重新设计的双感知路径注意力掩码（图像到图像和图像到分割），实现了像素与分割token之间的丰富特征交互。

【实验结果 / Results】
在多个分割任务上的综合实验表明，SELF1E能够达到与依赖专业掩码解码器的方法相竞争的性能水平。该方法成功验证了仅使用单个分割embedding即可实现高质量分割，无需额外的解码器模块或多个辅助token。

【应用价值 / Applications】
该研究为MLLM的轻量化分割应用提供了新思路，可广泛应用于需要高效图像理解的场景，如医学图像分割、自动驾驶中的场景解析、机器人视觉导航等。消除对外部解码器的依赖有助于简化模型架构，降低部署成本，推动端侧设备上的实时多模态分割应用。
