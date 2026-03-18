---
title: "Consensus Entropy: Harnessing Multi-VLM Agreement for Self-Verifying and Self-Improving OCR"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2504.11101"
published: "2026-03-18"
summarized: "2026-03-18T18:25:40.312355"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了**Consensus Entropy (CE)**，一种无需训练、模型无关的度量方法，通过测量多视觉语言模型（VLM）输出间的共识熵来估计OCR结果的可靠性。核心洞见是：正确预测在输出空间中趋于收敛，而错误预测则发散。基于此，作者开发了**CE-OCR**框架，通过模型集成共识验证输出、选择最优结果，并通过自适应路由提升效率。实验表明，CE在质量验证上比VLM-as-Judge的F1分数提升42.1%，CE-OCR在相同成本下 consistently 优于自一致性及单模型基线。

【方法概述 / Method】

CE方法通过聚合多个VLM对同一图像的OCR输出，计算输出分布的熵值作为可靠性指标——低熵表示模型间高度共识（高可信度），高熵表示分歧（低可信度）。CE-OCR框架在此基础上实现三步流程：多模型并行推理、基于CE的验证与最优输出选择、以及根据熵阈值自适应路由（低熵样本用轻量模型，高熵样本用更强模型）。

【实验结果 / Results】

质量验证任务中，CE相比VLM-as-Judge的F1分数提升42.1%，展现出 robust 的错误检测能力。OCR性能方面，CE-OCR在同等计算成本下 consistently 超越自一致性（self-consistency）和单模型基线，实现了准确性与效率的权衡优化。关键优势在于CE完全无需训练数据或监督信号，可直接 plug-and-play 应用于现有VLMs。

【应用价值 / Applications】

该研究为**高质量LLM训练数据生成**提供了可靠的自动化质检方案，解决了OCR数据标注中的样本级错误检测难题。CE-OCR可部署于文档数字化、档案管理等需要高精度OCR的**生产环境**，通过自适应路由降低多模型推理成本。其训练无关特性使其能快速适配新兴VLM，适用于**模型即服务（MaaS）**场景下的动态质量监控与模型选型。
