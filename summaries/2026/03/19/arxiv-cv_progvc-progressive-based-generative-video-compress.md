---
title: "ProGVC: Progressive-based Generative Video Compression via Auto-Regressive Context Modeling"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17546"
published: "2026-03-19"
summarized: "2026-03-19T15:13:41.434956"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了ProGVC，一种基于渐进式的生成式视频压缩框架，通过自回归上下文建模实现高效的视频压缩。该框架将视频编码为分层多尺度残差token图，支持通过由粗到精的尺度子集进行渐进式传输以实现灵活的码率自适应。同时，基于Transformer的多尺度自回归上下文模型用于估计token概率，既服务于传输token的高效熵编码，又能在解码端预测被截断的精细尺度token以恢复感知细节。实验表明，ProGVC在低码率下实现了有前景的感知压缩性能，同时具备良好的可扩展性。

【方法概述 / Method】

ProGVC借鉴视觉自回归（VAR）模型的下一尺度预测机制，将视频压缩统一在渐进传输、高效熵编码和细节合成的单一框架中。核心方法是将视频编码为分层多尺度残差token图，并采用Transformer-based多尺度自回归上下文模型对token概率进行估计，该概率同时用于熵编码和生成式细节重建。

【实验结果 / Results】

论文通过大量实验验证了ProGVC作为一种新型编码范式的有效性，表明该框架在低码率条件下能够提供优异的感知压缩性能，同时兼具实用的可扩展性。具体量化指标未在提供的摘要中详述，但强调了其在感知质量和码率灵活性方面的综合优势。

【应用价值 / Applications】

ProGVC适用于需要低码率高质量视频传输的场景，如流媒体服务、实时视频通信和带宽受限的移动视频应用。其渐进式传输特性特别适合网络条件动态变化的环境，能够实现自适应码率调整和渐进式质量提升，为下一代感知视频编码标准提供了新的技术路径。
