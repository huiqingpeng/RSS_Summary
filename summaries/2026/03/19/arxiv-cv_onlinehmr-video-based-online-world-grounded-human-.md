---
title: "OnlineHMR: Video-based Online World-Grounded Human Mesh Recovery"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17355"
published: "2026-03-19"
summarized: "2026-03-19T15:08:44.562081"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了OnlineHMR，首个完全在线的视频人体网格恢复框架，能够同时满足因果性、保真度、时间一致性和效率四个在线处理核心标准。该方法通过双分支架构、因果键值缓存设计和滑动窗口学习策略实现流式推理，并结合人体中心增量SLAM进行在线世界坐标对齐。实验表明，该方法在EMDB基准和动态视频上达到与分块离线方法相当的性能，同时唯一支持真正的在线处理。

【方法概述 / Method】
OnlineHMR采用双分支架构：一个分支处理单帧人体姿态估计，另一个分支通过因果键值缓存机制聚合时序信息，避免访问未来帧。训练时采用精心设计的滑动窗口策略，推理时结合人体中心增量SLAM模块，通过物理合理的轨迹校正实现世界坐标系的在线对齐。

【实验结果 / Results】
在标准EMDB基准测试和高度动态的自采集视频上，OnlineHMR取得了与现有分块式（chunk-based）离线方法相当的重建精度，同时实现了真正的帧级在线推理能力。该方法在保持时间一致性的同时，显著降低了延迟，满足了实时交互应用的需求。

【应用价值 / Applications】
该研究可直接应用于AR/VR实时交互、远程临场（telepresence）和机器人感知-动作闭环等需要即时反馈的场景。通过消除对未来帧的依赖，OnlineHMR使人体运动捕捉系统能够部署在资源受限的边缘设备上，为沉浸式体验和实时人机交互提供了关键技术支撑。
