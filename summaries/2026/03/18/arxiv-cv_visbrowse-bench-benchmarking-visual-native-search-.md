---
title: "VisBrowse-Bench: Benchmarking Visual-Native Search for Multimodal Browsing Agents"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16289"
published: "2026-03-18"
summarized: "2026-03-18T18:10:39.488240"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了VisBrowse-Bench，一个用于评估多模态浏览代理视觉原生搜索能力的新型基准测试。该基准包含169个涵盖多个领域的视觉问答实例，通过文本-图像检索和联合推理进行多模态证据交叉验证，以评估模型在搜索过程中的视觉推理能力。实验结果显示，即使是最先进的模型Claude-4.6-Opus和o3-deep-research的准确率也分别仅为47.6%和41.1%，揭示了当前多模态浏览代理在视觉原生搜索方面仍存在显著挑战。

【方法概述 / Method】
本文设计了一个多阶段人工构建流程，由领域专家创建并经过严格人工验证的VQA数据集。研究者还提出了一种驱动浏览代理的工作流程，使其能够在搜索过程中主动收集视觉信息并进行推理，实现多模态证据的交叉验证。

【实验结果 / Results】
在VisBrowse-Bench上的全面评估表明，开源和闭源模型在该任务上表现均不理想：最佳模型Claude-4.6-Opus准确率为47.6%，而专有的Deep Research模型o3-deep-research仅为41.1%。这一结果凸显了现有多模态大语言模型在结合视觉信息进行网页浏览和推理时的能力瓶颈。

【应用价值 / Applications】
该研究为开发更强大的多模态浏览代理提供了标准化评估基准，特别适用于需要深度理解网页视觉内容的自动化信息检索场景，如学术研究、电商比价、新闻核实等领域，推动AI代理从纯文本浏览向真正的多模态感知与推理演进。
