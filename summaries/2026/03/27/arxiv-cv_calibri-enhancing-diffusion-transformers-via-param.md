---
title: "Calibri: Enhancing Diffusion Transformers via Parameter-Efficient Calibration"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24800"
published: "2026-03-27"
summarized: "2026-03-28T07:16:51.685590"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文揭示了扩散Transformer（DiTs）在生成任务中被隐藏的优化潜力，通过深入分析去噪过程发现，仅需引入单个可学习的缩放参数即可显著提升DiT块的性能。基于此，作者提出Calibri方法——一种参数高效的校准方案，仅修改约100个参数即可优化DiT组件，并通过进化算法高效求解黑盒奖励优化问题。实验表明，Calibri在多种文本到图像模型上持续改进生成质量，同时减少推理步数并保持高输出质量。

【方法概述 / Method】
Calibri将DiT校准建模为黑盒奖励优化问题，采用进化算法进行高效求解；该方法通过为DiT块引入可学习的缩放参数实现参数高效的微调，仅修改约100个参数即可完成对模型组件的优化校准。

【实验结果 / Results】
Calibri在多种文本到图像DiT模型上均实现一致的性能提升；该方法能够显著减少图像生成所需的推理步数，同时在低参数修改量（~100参数）的条件下维持高质量的生成输出。

【应用价值 / Applications】
Calibri可广泛应用于现有文本到图像生成系统的快速优化与部署，特别适合计算资源受限场景下的模型增强；其参数高效特性使其易于集成到各类DiT架构中，为生成式AI的工业化落地提供轻量化、低成本的性能提升方案。
