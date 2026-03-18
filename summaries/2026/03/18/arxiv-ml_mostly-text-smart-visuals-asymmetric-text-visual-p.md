---
title: "Mostly Text, Smart Visuals: Asymmetric Text-Visual Pruning for Large Vision-Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16001"
published: "2026-03-18"
summarized: "2026-03-18T16:09:19.548326"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对大型视觉-语言模型（LVLMs）的网络剪枝问题，发现现有方法统一处理不同模态的校准数据，忽视了文本和视觉token的模态特异性行为。通过系统研究揭示：文本路径对剪枝更敏感，而视觉路径存在高度冗余（可达50%稀疏度）。基于这些发现，作者提出了一种非对称文本-视觉权重剪枝方法（ATV-Pruning），在标准多模态基准测试中展现出优于SOTA方法的性能。

【方法概述 / Method】
ATV-Pruning采用非对称策略处理双模态：首先自适应构建校准池，整合全部文本token和部分视觉token；其次设计层自适应选择策略筛选重要视觉token，从而建立准确的权重剪枝重要性度量。该方法通过解耦文本和视觉路径的权重，分别针对不同模态的敏感度特性进行差异化处理。

【实验结果 / Results】
实验表明视觉路径可承受高达50%的稀疏度而性能损失较小，而文本路径需要更谨慎的剪枝策略。ATV-Pruning在多个标准多模态基准测试中显著优于现有最先进方法，验证了非对称剪枝策略在保持模型性能的同时实现高效轻量化的有效性。

【应用价值 / Applications】
该研究为部署资源受限环境下的LVLMs提供了高效剪枝方案，特别适用于需要实时推理的移动设备、边缘计算等场景。通过智能区分文本和视觉组件的冗余特性，可在显著降低计算成本的同时保持多模态理解能力，推动大型视觉-语言模型在更广泛实际应用中的落地。
