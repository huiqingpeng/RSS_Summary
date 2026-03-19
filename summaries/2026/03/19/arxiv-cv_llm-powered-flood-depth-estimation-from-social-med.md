---
title: "LLM-Powered Flood Depth Estimation from Social Media Imagery: A Vision-Language Model Framework with Mechanistic Interpretability for Transportation Resilience"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17108"
published: "2026-03-19"
summarized: "2026-03-19T15:05:15.199590"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究提出FloodLlama，一个基于开源视觉-语言模型（VLM）的细粒度洪水深度估计系统，可从单张街景图像实现厘米级（0-40cm，1cm分辨率）连续深度预测。研究构建了约19万张合成图像数据集，采用渐进式课程学习和QLoRA微调LLaMA 3.2-11B Vision，实现了平均绝对误差低于0.97cm、5cm精度超过93.7%的性能。通过五阶段机械可解释性分析，识别出第23层为关键深度编码层，并开发出可减少76-80%可训练参数的选择性微调策略，同时在TikTok真实数据上验证了98.62%的准确率。

【方法概述 / Method】
研究采用合成数据生成管道，涵盖7种车型、4种天气条件和41个深度等级，结合渐进式课程训练实现从粗到细的学习。核心模型基于LLaMA 3.2-11B Vision，使用QLoRA进行高效微调，并创新性地引入深度相关的提示策略——简单提示用于浅水区，链式思维（CoT）推理用于深水区。通过机械可解释性框架定位关键层，实现分层选择性微调。

【实验结果 / Results】
在34,797次试验中，FloodLlama对深水区（>20cm）达到MAE<0.97cm、Acc@5cm>93.7%，浅水区（≤10cm）Acc@5cm>96.8%。Tier 3配置在底特律676帧真实TikTok数据上达到98.62%准确率，且在视觉遮挡条件下表现出强鲁棒性。选择性微调策略在保持精度的同时减少76-80%可训练参数。

【应用价值 / Applications】
该系统为交通韧性管理提供可扩展、无需基础设施的实时洪水感知方案，直接服务于电动汽车涉水安全评估、自动驾驶车辆动态路径规划，以及城市洪涝应急响应。基于社交媒体的众包数据管道（如TikTok）可实现低成本、广覆盖的街道级洪水监测，弥补传统传感器网络的部署盲区。
