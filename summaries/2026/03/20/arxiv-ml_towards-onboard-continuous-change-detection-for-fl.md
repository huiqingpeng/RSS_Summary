---
title: "Towards Onboard Continuous Change Detection for Floods"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.13751"
published: "2026-03-20"
summarized: "2026-03-20T15:03:15.775385"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对自然灾害监测中的洪水检测任务，开发了一种可在小型卫星内存与计算限制下运行的星上连续变化检测系统。作者提出了一种面向Transformer模型的历史信息注入机制（HiT），在保持历史观测上下文的同时将数据存储量减少99%以上。基于STTORM-CD洪水数据集的测试表明，HiT机制在Prithvi-tiny基础模型中保持了与双时相基线相当的检测精度，并在Jetson Orin Nano上实现了43 FPS的推理速度，为不依赖地面处理基础设施的实时灾害评估提供了实用框架。

【方法概述 / Method】
本研究提出HiT（History Injection for Transformer）机制，通过压缩并注入历史特征而非完整图像，使模型在连续观测中保持时序上下文记忆。该方法将Prithvi-tiny基础模型与HiT机制结合，构建轻量级端到端变化检测架构，专为星载边缘计算设备优化。

【实验结果 / Results】
在STTORM-CD洪水数据集上的验证显示，HiT-Prithvi保持了与标准双时相检测基线相近的检测精度；在代表星载硬件的Jetson Orin Nano平台上，模型推理速度达到43 FPS，满足实时处理需求；同时历史数据存储量压缩至原始图像大小的不足1%，显著降低星上存储负担。

【应用价值 / Applications】
该研究为小型卫星星座的自主灾害监测提供了可行方案，支持洪水等突发自然灾害的实时星上检测与预警，减少对地面站数据传输与处理的依赖。其低存储、低延迟特性特别适用于通信受限或应急响应场景，可拓展至其他需要连续变化检测的地球观测应用。
