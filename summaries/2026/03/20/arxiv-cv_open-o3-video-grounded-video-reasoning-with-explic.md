---
title: "Open-o3-Video: Grounded Video Reasoning with Explicit Spatio-Temporal Evidence"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.20579"
published: "2026-03-20"
summarized: "2026-03-20T16:15:05.630277"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Open-o3-Video，一个非代理式框架，用于在视频推理中整合显式的时空证据（包括关键时间戳、物体和边界框标注），使推理过程可追溯且可验证。为支持该能力，作者构建了高质量数据集STGR提供统一的时空监督信号，并采用冷启动强化学习策略，通过专门设计的奖励函数联合优化答案准确性、时间对齐和空间精度。在V-STAR基准上，该方法相比Qwen2.5-VL基线将mAM提升14.4%、mLGM提升24.2%，并在多个视频理解基准上取得一致增益。

【方法概述 / Method】
Open-o3-Video采用端到端训练框架，首先构建STGR数据集为视频片段提供时间戳、物体类别和边界框的联合标注作为监督信号；随后设计三目标奖励函数（答案正确性、时间定位精度、空间定位精度），结合冷启动强化学习策略进行模型优化，使模型学会生成带有显式时空锚定的推理轨迹。

【实验结果 / Results】
在V-STAR视频推理基准上，Open-o3-Video达到最先进性能，mAM（平均对齐度量）和mLGM（平均定位度量）分别较基线提升14.4%和24.2%；该方法在多个视频理解任务上均展现稳定提升，且生成的 grounded reasoning traces 支持置信度感知的测试时缩放，进一步提升答案可靠性。

【应用价值 / Applications】
该研究适用于需要可解释视频分析的场景，如司法取证、医疗影像诊断、自动驾驶决策验证等，其中推理过程的可追溯性至关重要；同时，显式时空证据支持人类审查和模型自我验证，为高 stakes 应用提供可信度保障，并可通过测试时缩放策略动态提升输出可靠性。
