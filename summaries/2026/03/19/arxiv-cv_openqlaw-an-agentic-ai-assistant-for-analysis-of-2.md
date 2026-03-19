---
title: "OpenQlaw: An Agentic AI Assistant for Analysis of 2D Quantum Materials"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17043"
published: "2026-03-19"
summarized: "2026-03-19T15:04:05.582607"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了OpenQlaw，一个用于二维量子材料分析的Agentic AI助手系统。该系统通过将视觉识别与物理推理解耦，解决了现有领域特定多模态大语言模型（MLLMs）输出冗长、易造成认知过载的问题。OpenQlaw采用轻量级Agent框架NanoBot，并以QuPAINT作为物理感知多模态专家节点，实现了动态推理、持久记忆存储和自然交互，将孤立的推理转化为上下文感知的实验室助手，加速高通量器件制备流程。

【方法概述 / Method】
OpenQlaw基于NanoBot轻量级Agent框架构建，该框架受OpenClaw启发，并集成QuPAINT作为物理感知指令多模态平台。系统采用核心LLM Agent编排领域专家MLLM的架构，通过解析空间数据实现视觉识别与推理的分离，并配备持久记忆模块存储物理尺度比例和样品制备方法等关键信息。

【实验结果 / Results】
论文未提供具体的定量实验结果或性能指标对比数据，主要强调系统架构设计的创新性和功能实现，包括成功实现尺度感知物理计算、生成隔离视觉标注、以及通过记忆功能支持面积计算和制备方法比较等能力。

【应用价值 / Applications】
OpenQlaw可直接部署于实验室现场，通过多种消息渠道为材料研究人员提供实时辅助，适用于二维量子材料从光学识别到实际器件制备的全流程。该系统能够加速高通量器件制造，特别适用于需要动态物理计算、样品追溯和制备工艺优化的实际研发场景。
