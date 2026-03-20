---
title: "6Bit-Diffusion: Inference-Time Mixed-Precision Quantization for Video Diffusion Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18742"
published: "2026-03-20"
summarized: "2026-03-20T15:15:31.858475"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了6Bit-Diffusion，一种面向视频扩散Transformer（Video DiTs）的推理时混合精度量化框架。研究发现Transformer块的输入输出差异与其内部线性层的量化敏感度存在强线性相关性，据此设计了轻量级预测器，动态分配NVFP4（4位浮点）给时序稳定层以最大化内存压缩，同时对波动层保留INT8精度以确保鲁棒性。此外，利用残差的高时序一致性提出时序差分缓存（TDC）跳过不变块的计算。实验表明该方法实现1.92倍端到端加速和3.32倍内存降低，为高效视频扩散推理建立了新基准。

【方法概述 / Method】
核心方法包含两个组件：（1）基于输入输出差异预测量化敏感度的动态混合精度分配策略，在低敏感层使用NVFP4、高敏感层使用INT8；（2）Temporal Delta Cache机制，利用跨时间步的残差一致性缓存并复用稳定块的计算结果，避免重复推理。

【实验结果 / Results】
在视频扩散模型上，该方法取得1.92×端到端推理加速和3.32×内存压缩比，在激进量化下仍保持生成质量不下降，显著优于静态位宽分配的基线方法。

【应用价值 / Applications】
该技术可直接部署于云端视频生成服务、实时视频编辑工具及边缘设备上的视频合成应用，解决视频扩散模型高显存占用和慢推理速度的关键瓶颈，使高质量视频生成在资源受限环境下成为可能。
