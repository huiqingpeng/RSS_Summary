---
title: "Symphony: A Cognitively-Inspired Multi-Agent System for Long-Video Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17307"
published: "2026-03-19"
summarized: "2026-03-19T15:08:03.665520"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Symphony，一个受人类认知启发的多智能体系统，用于解决长视频理解（LVU）任务。现有多模态大语言模型（MLLM）智能体在处理高信息密度、长时序跨度的视频时存在不足，简单的任务分解和协作机制难以应对长链推理，而基于嵌入的检索方法容易丢失关键信息。Symphony通过模拟人类认知模式，将LVU分解为细粒度子任务，并引入基于反思的深度推理协作机制，同时采用VLM-based grounding方法分析视频片段相关性，在LVBench、LongVideoBench等基准上取得SOTA性能，较之前最优方法提升5.0%。

【方法概述 / Method】
Symphony采用认知启发的多智能体架构，核心包含两个创新组件：（1）基于反思的深度推理协作机制，模拟人类"思考-反思-修正"的认知循环，增强长链推理能力；（2）VLM-based grounding模块，利用视觉语言模型直接分析视频内容以评估片段相关性，替代传统的嵌入检索方式，从而更好地定位隐含意图和大时间跨度的复杂问题。

【实验结果 / Results】
Symphony在四个主流长视频理解基准（LVBench、LongVideoBench、VideoMME、MLVU）上均取得SOTA性能。其中在LVBench上较此前最优方法提升5.0%，显著优于现有LVU智能体方法。实验结果表明，细粒度任务分解结合反思机制能有效提升长链推理能力，而VLM-based grounding相比嵌入检索能更准确地捕获关键视频信息。

【应用价值 / Applications】
该研究可应用于需要深度理解长视频内容的场景，如监控视频分析、电影内容理解、教育视频问答、体育赛事解析等。其认知启发的协作机制为构建更可靠的多智能体系统提供了新思路，VLM-based grounding方法也为长视频的高效信息检索提供了替代方案，对提升多模态大模型在实际长视频任务中的可用性具有重要价值。
