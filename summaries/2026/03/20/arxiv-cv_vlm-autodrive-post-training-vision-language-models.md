---
title: "VLM-AutoDrive: Post-Training Vision-Language Models for Safety-Critical Autonomous Driving Events"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18178"
published: "2026-03-20"
summarized: "2026-03-20T15:06:33.091629"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了VLM-AutoDrive，一种用于将预训练视觉-语言模型(VLMs)适配到安全关键自动驾驶事件检测的后训练框架。该框架通过整合元数据派生字幕、LLM生成描述、视觉问答对和思维链推理监督，解决了通用多模态大语言模型在驾驶场景中因领域和时间不对齐而导致的性能不足问题。在真实世界Nexar行车记录仪视频上的评估表明，该方法显著提升了碰撞和近碰撞检测性能，同时生成可解释的推理轨迹。

【方法概述 / Method】
VLM-AutoDrive采用模块化后训练策略，结合多种监督信号：从视频元数据提取的时序字幕、大语言模型生成的场景描述、视觉问答(VQA)数据对，以及思维链(CoT)推理监督。该方法以NVIDIA Cosmos-Reason1 7B为基础模型，通过领域对齐的微调实现时间局部化的异常检测能力。

【实验结果 / Results】
零样本设置下，Cosmos-Reason1 7B的碰撞检测召回率接近为零；经VLM-AutoDrive微调后，碰撞F1分数从0.00提升至0.69，整体准确率从35.35%提升至77.27%。在真实世界Nexar数据集上，该方法在碰撞和近碰撞检测任务中均取得显著性能增益，同时输出可解释的推理过程。

【应用价值 / Applications】
该研究为将通用视觉-语言模型适配到安全关键的时序感知任务提供了可扩展的技术路线，可应用于自动驾驶系统的异常事件检测、事故责任分析和驾驶决策解释。其生成的可解释推理轨迹有助于弥合感知、因果推理与驾驶决策之间的鸿沟，提升自动驾驶系统的安全性和透明度。
