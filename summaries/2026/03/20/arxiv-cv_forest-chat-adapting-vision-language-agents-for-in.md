---
title: "Forest-Chat: Adapting Vision-Language Agents for Interactive Forest Change Analysis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.14637"
published: "2026-03-20"
summarized: "2026-03-20T16:17:27.359326"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Forest-Chat，一个由大语言模型（LLM）驱动的智能体系统，用于交互式森林变化分析。该系统整合了多层级变化解释（MCI）视觉语言骨干网络与LLM编排能力，支持变化检测、变化描述生成、目标计数、森林砍伐特征描述和变化推理等多种遥感图像变化解释（RSICI）任务。研究还构建了Forest-Change数据集，包含双时相卫星影像、像素级变化掩膜和语义变化描述。实验表明，Forest-Chat在Forest-Change数据集上取得了67.10%的mIoU和40.17%的BLEU-4分数，零样本条件下也能达到60.15%和34.00%的性能。

【方法概述 / Method】
Forest-Chat采用多层级变化解释（MCI）视觉语言骨干架构，结合LLM进行任务编排和协调。系统集成了AnyChange实现零样本变化检测，并利用多模态大语言模型进行零样本变化描述生成与精炼。此外，研究通过人工标注和基于规则的方法构建了Forest-Change数据集，为森林环境的模型适应与评估提供支持。

【实验结果 / Results】
在监督学习设置下，Forest-Chat在Forest-Change数据集上达到67.10% mIoU和40.17% BLEU-4，在LEVIR-MCI-Trees子集上达到88.13% mIoU和34.41% BLEU-4。零样本场景下，系统在Forest-Change上取得60.15% mIoU和34.00% BLEU-4，在LEVIR-MCI-Trees上为47.32% mIoU和18.23% BLEU-4。实验还验证了描述精炼对注入地理领域知识的价值，以及系统在JL1-CD-Trees数据集上有限的标签域迁移能力。

【应用价值 / Applications】
Forest-Chat为森林监测工作流提供了可交互、可解释的分析工具，使非专业用户能够通过自然语言查询进行复杂的森林动态分析。该系统可应用于森林砍伐监测、生态环境评估、林业资源管理等场景，降低了遥感图像变化分析的技术门槛，支持更广泛的森林保护与可持续发展决策。
