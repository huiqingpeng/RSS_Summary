---
title: "Where MLLMs Attend and What They Rely On: Explaining Autoregressive Token Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.22496"
published: "2026-03-19"
summarized: "2026-03-19T16:25:53.580511"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了EAGLE，一个轻量级的黑盒解释框架，用于解释多模态大语言模型（MLLMs）中的自回归token生成过程。EAGLE能够将生成的token归因于紧凑的感知区域，同时量化语言先验和感知证据的相对影响，并通过统一充分性（insight score）和不可或缺性（necessity score）的目标函数进行优化。实验表明，EAGLE在忠实性、定位精度和幻觉诊断方面均优于现有方法，且显著降低了GPU内存需求。

【方法概述 / Method】
EAGLE采用基于稀疏化图像区域的贪婪搜索策略，通过优化统一充分性和不可或缺性的目标函数，实现对token生成的忠实且高效的归因。该框架还进行模态感知分析，能够解耦token生成所依赖的视觉和语言因素，提供细粒度的模型决策可解释性。

【实验结果 / Results】
在多个开源MLLM上的广泛实验表明，EAGLE在忠实性、空间定位精度和幻觉诊断任务上均一致优于现有方法。同时，EAGLE在计算效率方面表现突出，所需的GPU内存显著少于对比方法，证明了其在实际应用中的有效性和实用性。

【应用价值 / Applications】
EAGLE可用于提升MLLM的透明度和可信度，帮助开发者诊断模型幻觉问题、验证视觉-语言对齐质量，并支持模型调试与优化。其轻量级特性使其适用于资源受限环境下的实时解释需求，为多模态AI系统的安全部署和监管合规提供技术支撑。
