---
title: "LVOmniBench: Pioneering Long Audio-Video Understanding Evaluation for Omnimodal LLMs"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19217"
published: "2026-03-20"
summarized: "2026-03-20T16:06:02.506263"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了LVOmniBench，首个专门用于评估全模态大语言模型（OmniLLMs）长音频-视频理解能力的基准测试。该数据集包含275个时长10-90分钟的高质量视频及1,014个问答对，涵盖长期记忆、时间定位、细粒度理解和多模态感知等评估维度。实验发现当前OmniLLMs在处理长音频-视频输入时面临重大挑战，开源模型准确率普遍低于35%，而Gemini 3 Pro最高仅达约65%。

【方法概述 / Method】
研究团队从开放平台采集具有丰富音视频动态的高质量视频，通过严格的人工筛选与标注流程构建数据集。评估框架设计覆盖长期记忆、时间定位、细粒度理解和多模态感知四个核心能力维度，以全面检验模型对长时程跨模态信息的整合与推理能力。

【实验结果 / Results】
对主流OmniLLMs的广泛评估显示，现有模型在长音频-视频理解任务上表现欠佳：开源模型准确率普遍低于35%，商业模型Gemini 3 Pro达到约65%的峰值性能，但仍存在显著提升空间。结果表明长时程跨模态理解仍是当前全模态大模型亟待攻克的难题。

【应用价值 / Applications】
该基准测试填补了长时程音视频理解评估的空白，为开发能够处理真实场景（如长会议记录、电影分析、监控审查等）的先进OmniLLMs提供标准化评测工具。研究成果有望推动面向实际应用的长视频理解、多模态信息检索及智能内容分析等领域的技术发展。
