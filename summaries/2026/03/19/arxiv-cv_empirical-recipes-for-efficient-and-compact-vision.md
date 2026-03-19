---
title: "Empirical Recipes for Efficient and Compact Vision-Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16987"
published: "2026-03-19"
summarized: "2026-03-19T15:03:41.740202"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对资源受限环境下视觉-语言模型（VLMs）的部署需求，通过端到端效率分析和系统性的推理性能剖析，识别出紧凑型VLMs推理速度不达预期的关键瓶颈。基于这些发现，作者提出了一系列针对紧凑VLMs的优化方案，在保持精度的同时显著降低延迟，并将这些技术应用于构建ArgusVLM模型家族，在多样基准测试中实现了强性能与高效设计的平衡。

【方法概述 / Method】
作者采用实证分析方法，对紧凑VLMs进行端到端效率分析和推理性能剖析（profiling），系统识别计算瓶颈；在此基础上开发针对性的优化配方（recipes），涵盖架构无关的优化技术，并扩展至结构化感知输出能力以构建ArgusVLM模型。

【实验结果 / Results】
优化技术使InternVL3-2B的首token时间（TTFT）降低53%，SmolVLM-256M的TTFT降低93%；这些配方在多种VLM架构和常见服务框架中具有广泛适用性。ArgusVLM在多样化基准测试中展现出强劲性能，同时保持了紧凑高效的模型设计。

【应用价值 / Applications】
该研究为在边缘设备、实时系统等资源受限场景中部署高效VLMs提供了实用指导，其优化配方可直接应用于现有服务框架；ArgusVLM模型家族适用于需要结构化视觉感知输出的应用场景，如文档理解、视觉问答和自动化内容分析等。
