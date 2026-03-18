---
title: "M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16844"
published: "2026-03-18"
summarized: "2026-03-18T18:21:18.430385"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了 M³，一种将多视角基础模型与单目高斯溅射 SLAM 相结合的新框架，通过引入专用的匹配头（Matching head）实现细粒度稠密对应关系，解决了现有基础模型前馈姿态估计精度不足的问题。该方法还集成了动态区域抑制和跨推理内参对齐技术以增强跟踪稳定性。在多个室内外基准数据集上的实验表明，M³ 在姿态估计和场景重建方面均达到了最先进的性能，相比 VGGT-SLAM 2.0 将 ATE RMSE 降低了 64.3%，在 ScanNet++ 数据集上 PSNR 比 ARTDECO 高出 2.11 dB。

【方法概述 / Method】
M³ 的核心创新在于为多视角基础模型设计了一个专用的匹配头，用于生成高精度的稠密像素对应关系，而非依赖基础模型的前馈姿态输出。该框架将这些细粒度对应关系整合到单目高斯溅射 SLAM 流程中，并引入动态区域抑制机制过滤动态物体干扰，同时通过跨推理内参对齐处理未标定相机的内参变化问题。

【实验结果 / Results】
M³ 在多样化的室内和室外基准测试中实现了最先进的姿态估计精度和场景重建质量。具体而言，与 VGGT-SLAM 2.0 相比，绝对轨迹误差（ATE RMSE）显著降低 64.3%；在 ScanNet++ 数据集上，重建质量的 PSNR 指标比 ARTDECO 提升 2.11 dB，证明了该方法在未标定单目视频流式重建任务中的优越性。

【应用价值 / Applications】
M³ 适用于需要实时高精度三维重建的场景，如增强现实（AR）、虚拟现实（VR）、机器人导航和自动驾驶中的即时定位与地图构建。该方法对未标定单目视频的支持使其在消费级设备上具有广泛部署潜力，动态环境处理能力也拓展了其在真实世界复杂场景中的应用范围。
