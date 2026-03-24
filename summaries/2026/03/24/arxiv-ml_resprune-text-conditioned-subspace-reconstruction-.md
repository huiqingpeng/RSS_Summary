---
title: "ResPrune: Text-Conditioned Subspace Reconstruction for Visual Token Pruning in Large Vision-Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.21105"
published: "2026-03-24"
summarized: "2026-03-25T07:19:00.862887"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ResPrune，一种无需训练的视觉token剪枝框架，用于提升大型视觉-语言模型（LVLMs）的推理效率。该方法将视觉token剪枝建模为子空间重建问题，采用基于残差能量的贪心子空间扩展策略，并结合文本条件引导选择信息丰富且与指令相关的token。实验表明，ResPrune在LLaVA-1.5、LLaVA-NeXT和Qwen2.5-VL等多个LVLM骨干网络上均优于现有剪枝方法，同时显著降低了计算量、内存消耗和推理延迟。

【方法概述 / Method】
ResPrune将视觉token剪枝形式化为子空间重建问题，通过贪心策略逐步扩展子空间，以最小化重建残差能量来保留原始视觉token空间的几何结构。此外，该方法引入文本条件机制，使token选择过程能够感知跨模态对齐，优先保留与文本指令语义相关的视觉token。整个框架无需重新训练或修改模型架构，具有轻量级和模型无关的特性。

【实验结果 / Results】
ResPrune在多个主流LVLM架构（LLaVA-1.5、LLaVA-NeXT、Qwen2.5-VL）和广泛基准测试上均一致优于现有剪枝方法。该方法在实现有效计算、内存和推理延迟削减的同时，保持了模型性能，证明了其在实际部署中的优越性。

【应用价值 / Applications】
ResPrune可无缝集成到现有LVLM推理流程中，适用于需要高效处理高分辨率图像的移动设备、边缘计算和实时交互场景。该框架为大规模视觉-语言模型的资源优化部署提供了即插即用的解决方案，有助于降低推理成本并拓展LVLMs在计算受限环境中的应用范围。
