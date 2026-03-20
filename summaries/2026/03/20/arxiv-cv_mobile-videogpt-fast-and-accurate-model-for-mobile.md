---
title: "Mobile-VideoGPT: Fast and Accurate Model for Mobile Video Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2503.21782"
published: "2026-03-20"
summarized: "2026-03-20T16:11:18.311165"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了 Mobile-VideoGPT，一种高效的多模态视频理解框架，参数量不到10亿。该模型通过轻量级双视觉编码器、高效投影器和小型语言模型实现实时推理吞吐量，并引入基于注意力的帧评分机制选择关键帧以及高效的token投影器来剪枝冗余视觉token。实验表明，Mobile-VideoGPT-0.5B在六个视频理解基准上平均超越现有最优0.5B参数模型6个百分点，同时参数量减少40%，吞吐量提升2倍以上。

【方法概述 / Method】
Mobile-VideoGPT采用轻量级双视觉编码器、高效投影器和小型语言模型（SLM）的架构设计。核心创新包括：基于注意力的帧评分机制动态选择关键帧，以及高效token投影器在保留关键上下文线索的同时剪枝冗余视觉token，从而在极低参数量下实现高效的视频理解。

【实验结果 / Results】
在MVBench、EgoSchema、NextQA和PercepTest等六个视频理解基准上进行评估，Mobile-VideoGPT-0.5B平均超越现有最优0.5B参数模型6个百分点。该模型可实现每秒46个token的生成速度，参数量比同类模型减少40%，吞吐量提升超过2倍，实现了精度与效率的显著平衡。

【应用价值 / Applications】
Mobile-VideoGPT适用于移动端实时视频理解场景，如智能手机视频分析、AR/VR设备交互、边缘计算视频问答等。其低参数量（<1B）和高吞吐量的特性使其特别适合计算资源受限的移动设备和边缘部署，为普及化的视频智能应用提供了可行的技术方案。
