---
title: "Frequency Autoregressive Image Generation with Continuous Tokens"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2503.05305"
published: "2026-03-19"
summarized: "2026-03-19T16:23:48.625305"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了频率渐进自回归（FAR）范式，用于图像生成任务。该范式采用连续分词器（continuous tokenizer），并以频谱依赖性作为回归方向——高频分量基于低频分量逐步构建完整图像。这种设计既满足自回归模型的因果性要求，又保留了图像数据独特的空间局部性。作者在ImageNet数据集上验证了FAR的有效性，并展示了其在文本到图像生成中的潜力。

【方法概述 / Method】

FAR范式包含两个核心创新：一是将回归方向从传统的光栅扫描（raster-scan）改为频谱渐进（frequency progressive），即按频率从低到高依次预测；二是采用连续分词器替代传统的向量量化（VQ）分词器。为应对优化挑战并提升训练推理效率，作者还引入了一系列配套技术。

【实验结果 / Results】

论文在ImageNet数据集上进行了全面实验，验证了FAR范式的有效性；同时展示了该方法在文本到图像生成任务中的潜在应用价值。具体定量指标（如FID、IS等）未在提供的摘要中披露。

【应用价值 / Applications】

FAR可应用于高质量图像合成领域，包括无条件图像生成和条件式文本到图像生成。连续分词器的使用避免了离散化带来的信息损失，频谱渐进的设计更符合图像数据的内在结构，有望提升生成质量与效率，适用于内容创作、设计辅助等实际场景。
