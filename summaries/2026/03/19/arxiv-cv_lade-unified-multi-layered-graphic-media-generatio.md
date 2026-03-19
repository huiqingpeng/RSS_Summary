---
title: "LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17965"
published: "2026-03-19"
summarized: "2026-03-19T16:19:24.915835"
ai_provider: "openai"
---

【论文摘要 / Abstract】
LaDe提出了一种统一的多层图形媒体生成与分解框架，解决了现有方法在层数固定或要求空间连续性方面的限制。该框架通过LLM提示扩展器、4D RoPE位置编码的潜在扩散Transformer以及RGBA VAE三个核心组件，实现了灵活数量的语义有意义层生成。实验表明，LaDe在Crello测试集上的文本到层生成任务中优于Qwen-Image-Layered，并通过GPT-4o mini和Qwen3-VL两个VLM评判器验证了其文本-层对齐性能的显著提升。

【方法概述 / Method】
LaDe采用潜在扩散架构，包含三个关键组件：基于大语言模型的提示扩展器将用户短提示转换为结构化的逐层描述；潜在扩散Transformer配备4D RoPE位置编码机制，联合生成完整媒体设计及其RGBA层；RGBA VAE解码器支持完整alpha通道的层解码。训练时通过层采样条件化，使统一框架能够同时支持三种任务。

【实验结果 / Results】
在Crello测试集上，LaDe与Qwen-Image-Layered进行对比评估，在文本到层生成任务中表现更优。评估采用GPT-4o mini和Qwen3-VL作为VLM评判器，验证了LaDe在文本-层对齐方面的改进。框架还支持图像到层的分解任务，展现了统一架构在多任务上的有效性。

【应用价值 / Applications】
LaDe可广泛应用于海报、传单、Logo等可编辑分层设计文档的自动化生成，显著降低专业设计门槛。其统一的生成-分解能力支持从文本描述创建设计、以及现有设计的层分解编辑，适用于平面设计、营销内容创作和数字资产管理等场景，为创意产业提供高效的AI辅助设计工具。
