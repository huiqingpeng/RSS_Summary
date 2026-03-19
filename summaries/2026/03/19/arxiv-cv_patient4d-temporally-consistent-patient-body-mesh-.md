---
title: "Patient4D: Temporally Consistent Patient Body Mesh Recovery from Monocular Operating Room Video"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17178"
published: "2026-03-19"
summarized: "2026-03-19T15:06:31.208673"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Patient4D，一种针对手术室单目视频的患者身体网格恢复方法，专门解决手术铺巾遮挡和相机连续移动带来的挑战。该方法利用患者静止性先验，通过姿态锁定和刚性回退两个关键机制实现时间一致性重建。在合成手术序列和公开基准测试上，该方法将失败帧率从30.5%降至1.3%，显著优于现有基线方法。

【方法概述 / Method】
Patient4D采用基于静止性约束的重建流程，结合图像级基础模型进行感知，并通过轻量级几何机制强制跨帧时间一致性。核心组件包括：姿态锁定（Pose Locking）——利用稳定关键帧锚定姿态参数；刚性回退（Rigid Fallback）——在严重遮挡时通过轮廓引导的刚性对齐恢复网格。

【实验结果 / Results】
在4,680个合成手术序列和三个公开HMR视频基准上进行评估，Patient4D在手术铺巾遮挡条件下达到0.75的平均IoU。相比最佳基线方法，失败帧比例从30.5%大幅降低至1.3%，同时保持与现成HMR模型的兼容性。

【应用价值 / Applications】
该研究主要应用于手术增强现实（AR）场景，可为头戴式相机视角下的麻醉患者提供实时、稳定的3D身体网格重建。该技术有助于提升手术导航精度、实现患者体位监测，并为术中增强现实可视化提供可靠的几何基础，具有重要的临床实用价值。
