---
title: "Em-Garde: A Propose-Match Framework for Proactive Streaming Video Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19054"
published: "2026-03-20"
summarized: "2026-03-20T16:03:46.264180"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Em-Garde，一种用于主动流媒体视频理解的新型框架，通过将语义理解与流媒体感知解耦来解决现有方法在效率与准确性之间的困境。该框架在查询阶段利用指令引导的提案解析器将用户查询转换为结构化的感知视觉提案，在流媒体阶段通过轻量级提案匹配模块进行高效的嵌入匹配来触发响应。在StreamingBench和OVO-Bench上的实验表明，该模型在主动响应准确性和效率方面均优于现有方法，为严格计算约束下的主动视频理解提供了有效解决方案。

【方法概述 / Method】
Em-Garde采用"提出-匹配"（Propose-Match）的两阶段架构：离线阶段，Instruction-Guided Proposal Parser将用户自然语言查询解析为与视觉感知相关的结构化提案；在线流媒体阶段，Lightweight Proposal Matching Module通过嵌入空间中的高效相似度计算，实时匹配当前视频帧与预存提案，从而决定是否触发响应。这种解耦设计避免了逐帧进行复杂的语义推理，显著降低了计算开销。

【实验结果 / Results】
在StreamingBench和OVO-Bench两个主流基准测试上，Em-Garde在主动响应准确性方面取得一致提升，同时保持了较高的计算效率。实验验证了该框架能够在严格的计算资源约束下，有效平衡视频理解的准确性与实时性需求，优于现有的逐帧触发决策方法。

【应用价值 / Applications】
该研究适用于需要实时交互的智能监控、自动驾驶、机器人视觉和直播内容分析等场景，特别是在边缘设备或带宽受限环境下。Em-Garde的轻量级设计使其能够部署于资源受限的硬件平台，为主动式人机交互和实时视频分析提供了可行的工程解决方案，推动了流媒体视频理解技术的实际落地。
