---
title: "vAccSOL: Efficient and Transparent AI Vision Offloading for Mobile Robots"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16685"
published: "2026-03-18"
summarized: "2026-03-18T18:24:07.956316"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了vAccSOL框架，用于在异构机器人和边缘平台上高效透明地执行基于AI的视觉工作负载。该框架整合了SOL神经网络编译器和vAccel轻量级执行框架，实现了硬件优化的推理和灵活的执行位置选择，无需修改机器人应用程序。实验表明，与PyTorch基线相比，vAccSOL在边缘卸载场景下可将机器人端功耗降低80%、边缘端功耗降低60%，并将视觉管线帧率提升24倍，显著延长电池供电机器人的工作时长。

【方法概述 / Method】
vAccSOL由两个核心组件构成：SOL编译器生成具有最小运行时依赖的优化推理库，vAccel框架则透明地将推理任务调度至机器人本地或附近边缘基础设施执行。这种设计支持异构硬件加速器的灵活利用，同时保持对上层应用的透明性。

【实验结果 / Results】
研究在商业四足机器人和12个深度学习模型（涵盖图像分类、视频分类和语义分割）的真实测试平台上进行评估。SOL编译器实现了与PyTorch相当或更优的推理性能；通过边缘卸载，vAccSOL在大幅降低功耗的同时，将视觉管线帧率提升最高达24倍。

【应用价值 / Applications】
该研究适用于巡检、巡逻和搜救等移动机器人场景，解决了嵌入式平台计算资源受限和能耗约束的核心挑战。vAccSOL使机器人能够在不修改现有应用的情况下灵活利用边缘计算资源，显著延长电池续航并提升视觉任务处理能力，对实际部署具有重要工程价值。
