---
title: "Fine-Grained Post-Training Quantization for Large Vision Language Models with Quantization-Aware Integrated Gradients"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17809"
published: "2026-03-19"
summarized: "2026-03-19T15:18:09.519139"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对大型视觉语言模型（LVLMs）部署中的计算与内存瓶颈问题，提出了一种细粒度的后训练量化方法。现有方法通常在模态级别衡量token敏感性，无法捕捉复杂的跨token交互；作者受机械可解释性中公理化归因的启发，引入量化感知积分梯度（QIG），将敏感性评估粒度从模态级推进到token级。实验表明，该方法在W4A8和W3A16设置下显著提升多个LVLM的精度，且延迟开销可忽略不计，例如LLaVA-onevision-7B在3-bit权重量化下平均精度提升1.60%，与全精度模型的差距缩小至仅1.33%。

【方法概述 / Method】
本文核心方法是**量化感知积分梯度（Quantization-Aware Integrated Gradients, QIG）**，利用积分梯度定量评估token级别的敏感性，同时反映模态间和模态内的动态交互。该方法将校准粒度从粗粒度的模态级细化为细粒度的token级，以更精确地衡量量化误差并指导量化过程。

【实验结果 / Results】
在多个LVLM和基准测试上的广泛实验表明，QIG方法在W4A8和W3A16量化设置下均实现了精度提升。具体而言，LLaVA-onevision-7B在3-bit权重量化下平均精度提升1.60%，与全精度版本的性能差距仅1.33%；同时该方法引入的延迟开销可忽略不计，兼顾了效率与精度。

【应用价值 / Applications】
该方法适用于需要高效部署大型视觉语言模型的场景，如边缘设备推理、实时多模态交互应用及资源受限环境下的视觉问答、图像描述等任务。通过大幅降低内存占用和加速推理，同时保持接近全精度的性能，QIG为LVLMs的实际落地提供了可行的量化解决方案。
