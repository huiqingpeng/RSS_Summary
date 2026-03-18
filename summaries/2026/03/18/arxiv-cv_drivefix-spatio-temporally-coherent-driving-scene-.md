---
title: "DriveFix: Spatio-Temporally Coherent Driving Scene Restoration"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16306"
published: "2026-03-18"
summarized: "2026-03-18T18:10:57.419006"
ai_provider: "openai"
---

【论文摘要 / Abstract】
DriveFix 提出了一种多视角驾驶场景修复框架，旨在解决现有 4D 场景重建方法中缺乏时空协同的问题。该方法通过交错式扩散 Transformer 架构，显式建模时间依赖性和跨相机空间一致性，并结合历史上下文条件生成与几何感知训练损失，确保修复视图符合统一的三维几何结构。在 Waymo、nuScenes 和 PandaSet 数据集上的评估表明，该方法在重建和新视角合成任务中均达到最先进的性能。

【方法概述 / Method】
DriveFix 采用交错式扩散 Transformer（interleaved diffusion transformer）架构，包含专门设计的模块以同时处理时间依赖关系和跨相机空间一致性。该方法通过以历史上下文为条件进行生成，并引入几何感知训练损失，强制使修复后的多视角图像遵循统一的 3D 几何约束，从而实现高保真纹理的一致传播。

【实验结果 / Results】
DriveFix 在 Waymo、nuScenes 和 PandaSet 三个主流自动驾驶数据集上进行了广泛评估，在场景重建和新视角合成任务中均取得了 state-of-the-art 的性能表现。实验结果表明该方法显著减少了空间错位和时间漂移等伪影，有效提升了 4D 场景建模的时空连贯性。

【应用价值 / Applications】
该研究对自动驾驶系统的 4D 世界建模具有重要价值，可应用于高精地图构建、传感器数据增强、仿真环境生成等场景。通过提供时空一致的驾驶场景修复能力，DriveFix 有助于提升自动驾驶感知系统的鲁棒性和可靠性，推动其在真实世界中的部署应用。
